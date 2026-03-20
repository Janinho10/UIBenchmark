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

    out = d(text="ALLOW").click()
    if not out:
        print("Success: Clicked on Allow")
    wait()
    
    out = d(resourceId="android:id/button3").click()
    if not out:
        print("Success: closed 'What's New?'")
    wait()
    
    out = d(description="Open navigation drawer").click()
    if not out:
        print("Success: Open Menu")
    wait()
    
    out = d(text="Accuracy").click()
    if not out:
        print("Success: clicked Accuracy")
    wait()
    
    out = d(resourceId="com.android.gpstest:id/ground_truth_lat_text").click()
    if not out:
        print("Success: Tap latitude text")
    wait()
    
    out = d.click(950, 1250)
    
    wait(1)
    
    out = d.click(950, 1250)
    
    wait(1)
    
    out = d.click(950, 1250)
    
    wait()
    
    out = d(resourceId="com.android.gpstest:id/ground_truth_long_text").click()
    if not out:
        print("Success: Tap longitude text")
    wait()
    
    out = d.click(950, 1250)
    
    wait(1)
    
    out = d.click(950, 1250)
    
    wait(1)
    
    out = d.click(950, 1250)
    
    wait()
    
    out = d(resourceId="com.android.gpstest:id/ground_truth_alt_text").click()
    if not out:
        print("Success: Tap Altitude text")
    wait()
    
    out = d.click(950, 1250)
    
    wait(1)
    
    out = d.click(950, 1250)
    
    wait(1)

    out = d.click(950, 1250)
        
    print("Successful Replay!")
