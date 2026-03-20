import sys
import subprocess
import uiautomator2 as u2
import time

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    
    d = u2.connect(avd_serial)

    package_name = "com.michaeltroger.gruenerpass"
    DEVICE_FOLDER = "/sdcard/Download/testdata/"

    
    subprocess.run(f"adb -s {avd_serial} shell rm -rf {DEVICE_FOLDER}", shell=True)
    
