# bug reproduction script for bug #1145 of GPSTest
import os
import sys
import time

import uiautomator2 as u2

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)

    d.app_start("com.android.gpstest")
    wait()

    current_app = d.app_current()
    print(current_app)
    
    wait()
    
    out = d(description="Open navigation drawer").click()
    if not out:
        print("Success: Open Menu")
    wait()
    
    out = d(text="Sky").click()
    if not out:
        print("Success: Opened Sky")
    wait()
    
    out = d.press("back")
    if out:
        print("Success: Pressed back")
    wait()
    
    print("Successful Replay!")
    
