# bug reproduction script for bug #1145 of GPSTest
import os
import sys
import time
import subprocess

import uiautomator2 as u2



if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "com.android.gpstest"
    
    #permissions = [
    #    "android.permission.ACCESS_FINE_LOCATION",
    #    "android.permission.ACCESS_COARSE_LOCATION"
    #]
    
   # for perm in permissions:
   #     subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}",
   #                        shell=True, check=False, stderr=subprocess.DEVNULL)

    d.app_start(package_name)

    current_app = d.app_current()
    print(current_app)
