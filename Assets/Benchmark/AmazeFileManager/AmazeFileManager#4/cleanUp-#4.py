#Deletes test file from /storage/emulated/0/Alarms

import sys
import time
import uiautomator2 as u2
import subprocess

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    file_path = "/storage/emulated/0/Alarms/test"


    subprocess.run(f"adb -s {avd_serial} shell rm -rf {file_path}", shell=True)
