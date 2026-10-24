#!/usr/bin/env python3
"""Prepare the pinned Swiftgram baseline on a Mac; does not sign in, build, or change system settings."""
import argparse,json,platform,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--destination',type=Path,default=Path.home()/'Developer'/'swiryyyyX-ios')
 p.add_argument('--clone',action='store_true',help='Fetch the pinned baseline and its submodules after preflight')
 args=p.parse_args();versions=json.loads((HERE/'versions.json').read_text())
 pin=(HERE/'UPSTREAM_COMMIT').read_text().strip()
 if platform.system()!='Darwin':sys.exit('A Mac is required for Xcode. No changes were made.')
 try:
  xcode=subprocess.check_output(['xcodebuild','-version'],text=True).splitlines()[0].split()[-1]
 except (FileNotFoundError,subprocess.CalledProcessError):sys.exit('Install/open Xcode first, then run this check again.')
 if xcode!=versions['xcode']:sys.exit(f"Pinned Swiftgram expects Xcode {versions['xcode']}; installed: {xcode}. Review toolchain before proceeding.")
 if int(platform.mac_ver()[0].split('.')[0])<int(versions['macos']):sys.exit('The selected baseline requires macOS '+versions['macos'])
 subprocess.run(['git','--version'],check=True)
 print('Toolchain check passed; Swiftgram baseline:',pin)
 if not args.clone:return
 target=args.destination.expanduser().resolve()
 if target.exists():sys.exit('Destination already exists; no files were overwritten. Choose a new destination.')
 target.parent.mkdir(parents=True,exist_ok=True)
 subprocess.run(['git','clone','--filter=blob:none','--no-checkout',versions['upstream'],str(target)],check=True)
 subprocess.run(['git','fetch','--depth=1','origin',pin],cwd=target,check=True)
 subprocess.run(['git','checkout','--detach',pin],cwd=target,check=True)
 subprocess.run(['git','submodule','update','--init','--recursive','--jobs','4'],cwd=target,check=True)
 print('Prepared baseline. Next: create our development configuration and verify a simulator build.')
 print('No iOS feature port, IPA, signing certificate, or push configuration is claimed by this preparation.')
if __name__=='__main__':main()
