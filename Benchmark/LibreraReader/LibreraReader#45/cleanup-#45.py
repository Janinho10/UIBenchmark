import os
import sys
import uiautomator2 as u2
import time
import subprocess


if __name__ == '__main__':
    avd_serial = sys.argv[1] if len(sys.argv) > 1 else "emulator-5554"
    d = u2.connect(avd_serial)
    target_dir = "/sdcard/"
    
    d.shell(f"rm -rf {target_dir}")
