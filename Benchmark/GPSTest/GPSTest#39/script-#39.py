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
    
    out = d(className="android.widget.Button", resourceId="com.android.packageinstaller:id/permission_allow_button").click()
    if not out:
        print("Success: clicked allow")
    
    wait()
    
    
    out = d(resourceId="android:id/button3").click()
    if not out:
        print("Success: closed 'What's New?'")
    wait()
    
    out = d(description="Open navigation drawer").click()
    if not out:
        print("Success: Open Menu")
    wait()
    
    out = d(text="Help").click()
    if not out:
        print("Success: opened Help")
    wait()
    
    out = d(text="About").click()
    if not out:
        print("Success: Opened About page")
    wait()
    
    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: Scrolled to bottom")
    wait()
    
    out = d(description="Navigate up").click()
    if not out:
        print("Success: Clicked back")
    
    
    print("Successful Replay!")
    
