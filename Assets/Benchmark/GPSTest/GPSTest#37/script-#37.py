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
    
    
    out = d(resourceId="android:id/button3").click()
    if not out:
        print("Success: closed 'What's New?'")
    wait()
    
    out = d(description="Open navigation drawer").click()
    if not out:
        print("Success: Open Menu")
    wait()
    
    out = d(text="Settings").click()
    if not out:
        print("Success: opened Settings")
    wait()
    
    out = d(text="Use Dark Theme").click()
    if not out:
        print("Success: switched to Dark Theme")
    wait()
    
    out = d.press("Back")
    if not out:
        print("Success: Go Back")
    wait()
    
    d.app_start("com.android.gpstest")
    wait()
    
    out = d(description="Open navigation drawer").click()
    if not out:
        print("Success: Open Menu")
    wait()
    
    out = d.press("Back")
    if not out:
        print("Success: Go Back")
    wait()
    
    print("Successful Replay!")
    
