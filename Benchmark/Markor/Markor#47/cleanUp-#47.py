import sys
import time
import uiautomator2 as u2
import subprocess

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "net.gsantner.markor"
    
    subprocess.run(f"adb -s {avd_serial} shell rm -rf /storage/emulated/0/Documents/Markor/Q", shell=True)
    
