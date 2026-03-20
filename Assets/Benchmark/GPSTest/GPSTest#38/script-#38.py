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
    
    out = d(text="Keep Screen On").click()
    if not out:
        print("Success: Keep Screen on option")
    wait()
    
    
    print("Successful Replay!")
