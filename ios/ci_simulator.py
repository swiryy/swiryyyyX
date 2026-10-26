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
    patch = HERE / 'swiryyyyX-ios.patch'
    run('git', 'apply', '--check', str(patch), cwd=root)
    run('git', 'apply', str(patch), cwd=root)
    tests = Path(os.environ['RUNNER_TEMP']) / 'swirix-hidden-tests'
    run('swiftc', '-swift-version', '5',
        str(root / 'Swiftgram/SGSimpleSettings/Sources/SwirixHiddenChats.swift'),
        str(root / 'Tests/SwirixHiddenChatsTests.swift'), '-o', str(tests))
    run(str(tests))
    # The upstream build subcommand does not expose the provisioning switch that
    # generateProject already supports. Enable that existing Bazel setting only
    # for the simulator configurations; never bypass signing for device builds.
    make_path = root / 'build-system/Make/Make.py'
    make_source = make_path.read_text()
    start = make_source.index('\ndef build(bazel, arguments):')
    anchor = '    bazel_command_line.set_configuration(arguments.configuration)'
    position = make_source.index(anchor, start)
    make_source = (make_source[:position] +
                   "    if arguments.configuration in ('debug_sim_arm64', 'release_sim_arm64'):\n"
                   "        bazel_command_line.set_disable_provisioning_profiles()\n\n" +
                   make_source[position:])
    make_path.write_text(make_source)
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
    import shutil
    artifacts = Path(os.environ['RUNNER_TEMP']) / 'swiryyyyx-artifacts'
    artifacts.mkdir()
    shutil.copyfile(root / 'bazel-bin/Telegram/Swiftgram.ipa', artifacts / 'swiryyyyX-simulator.zip')
    print('Experimental swiryyyyX simulator port compiled. Device signing and real iPhone validation remain pending.')


if __name__ == '__main__':
    main()
