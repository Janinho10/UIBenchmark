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

    current_app = d.app_current()
    print(current_app)
    
    wait()
    
    out = d(text="ALLOW").click()
    if not out:
        print("Success: clicked allow")
    wait()
    
    out = d(resourceId="android:id/button3").click()
    if not out:
        print("Success: closed 'What's New?'")
    wait()
    
    out = d(description="Filter").click()
    if not out:
        print("Success: Clicked on Filter")
    wait()
    
    out = d(text="GLONASS (Russia)").click()
    if not out:
        print("Success: clicked GLONASS (Russia)")
    wait()
    
    out = d(text="Galileo (European Union)").click()
    if not out:
        print("Success: clicked Galileo (European Union)")
    wait()
    
    out = d(text="QZSS (Japan)").click()
    if not out:
        print("Success: clicked QZSS (Japan)")
    wait()
    
    out = d(text="BeiDou/COMPASS (China)").click()
    if not out:
        print("Success: clicked BeiDou/COMPASS (China)")
    wait()
    
    out = d(text="SAVE").click()
    if not out:
        print("Success: saved GNSSs")
    wait()
    
    out = d(resourceId="com.android.gpstest:id/gps_switch").click()
    if not out:
        print("Success: clicked on Switch")
    
    
    print("Successful Replay!")
    
