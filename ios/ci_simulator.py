#!/usr/bin/env python3
"""Build the pinned, unmodified Swiftgram baseline for the iOS simulator only."""
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def run(*args, cwd=None):
    subprocess.run(args, cwd=cwd, check=True)


def main():
    versions = json.loads((HERE / 'versions.json').read_text())
    pin = (HERE / 'UPSTREAM_COMMIT').read_text().strip()
    if not re.fullmatch(r'[0-9a-f]{40}', pin):
        sys.exit('Invalid upstream commit pin')
    if platform.system() != 'Darwin' or platform.machine() != 'arm64':
        sys.exit('This baseline job requires an Apple Silicon macOS runner')
    actual = subprocess.check_output(['xcodebuild', '-version'], text=True).splitlines()[0]
    if actual != f"Xcode {versions['xcode']}":
        sys.exit(f"Expected Xcode {versions['xcode']}; found {actual}")
    if int(platform.mac_ver()[0].split('.')[0]) < int(versions['macos']):
        sys.exit(f"Expected macOS {versions['macos']} or later")
    api_id = os.environ.get('TELEGRAM_API_ID', '')
    api_hash = os.environ.get('TELEGRAM_API_HASH', '')
    if not api_id.isdigit() or int(api_id) <= 0 or not re.fullmatch(r'[0-9a-fA-F]{32}', api_hash):
        sys.exit('Set the owner TELEGRAM_API_ID and TELEGRAM_API_HASH Actions secrets')
    root = Path(os.environ['RUNNER_TEMP']) / 'swiryyyyx-swiftgram'
    if root.exists():
        sys.exit('Build destination already exists; refusing to overwrite it')
    run('git', 'init', str(root))
    run('git', 'remote', 'add', 'origin', 'https://github.com/Swiftgram/Telegram-iOS.git', cwd=root)
    run('git', 'fetch', '--depth=1', 'origin', pin, cwd=root)
    run('git', 'checkout', '--detach', 'FETCH_HEAD', cwd=root)
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    if head != pin:
        sys.exit('Upstream checkout does not match pin')
    run('git', 'submodule', 'update', '--init', '--recursive', '--jobs', '4', cwd=root)
    config = json.loads((root / 'build-system/template_minimal_development_configuration.json').read_text())
    config.update(bundle_id='ua.swiryyyyx.client', api_id=api_id, api_hash=api_hash,
                  team_id='', app_specific_url_scheme='swiryyyyx', sg_config='')
    config_path = root / 'build-system/swiryyyyx-ci.json'
    config_path.touch(mode=0o600)
    config_path.write_text(json.dumps(config))
    try:
        run(sys.executable, '-u', 'build-system/Make/Make.py',
            '--cacheDir=' + str(Path(os.environ['RUNNER_TEMP']) / 'swiryyyyx-bazel-cache'),
            'build', '--configurationPath=' + str(config_path), '--xcodeManagedCodesigning',
            '--configuration=debug_sim_arm64', '--buildNumber=' + os.environ.get('GITHUB_RUN_NUMBER', '1'),
            cwd=root)
    finally:
        config_path.unlink(missing_ok=True)
    print('Pinned simulator baseline compiled. This is not an iPhone IPA or a feature-port validation.')


if __name__ == '__main__':
    main()
