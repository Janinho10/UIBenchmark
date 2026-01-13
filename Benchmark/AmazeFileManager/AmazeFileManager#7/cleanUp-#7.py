import sys
import time
import uiautomator2 as u2
import subprocess
import tarfile
import os

if __name__ == '__main__':

    #remove gz.tar.gz file from device

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "com.amaze.filemanager"
    
    target_archive = "/storage/emulated/0/Download/gz.tar.gz"
    
    subprocess.run(f"adb -s {avd_serial} shell rm -f {target_archive}", shell=True)
