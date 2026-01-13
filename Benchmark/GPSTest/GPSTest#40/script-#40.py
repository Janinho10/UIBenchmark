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
    
    out = d(text="Settings").click()
    if not out:
        print("Success: opened Settings")
    wait()
    
    out = d(text="Language").click()
    if not out:
        print("Success: click Language")
    wait()
    
    out = d(text="中文").click()
    if not out:
        print("Success: changed Language")
    wait()
    
    out = d.press("back")
    if out:
        print("Success: pressed back")
    wait()
    
    out = d(description="打开导航栏").click()
    if not out:
        print("Success: Open Menu")
    wait()
    
    out = d(text="帮助").click()
    if not out:
        print("Success: opened About")
    wait()
    
    out = d(text="关于").click()
    if not out:
        print("Success: opened Help")
    wait()
    
        
    print("Successful Replay!")
    
