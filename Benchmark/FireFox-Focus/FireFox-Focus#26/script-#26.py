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

    d.app_start("org.mozilla.focus")
    wait()

    current_app = d.app_current()
    print(current_app)
    
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/skip").click()
    if not out:
        print("Success: Clicked Skip")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/menuView").click()
    if not out:
        print("Success: Opened 'More Options'-Menu")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/settings").click()
    if not out:
        print("Success: Opened Settings")
    wait()
    
    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: Scroll Down")
    wait()
    
    el = d.click(300, 1600)
    if not out:
        print("Success: Clicked 'Your Rights'")
    wait()
    
    out = d(description="licenses").click()
    if not out:
        print("Success: Opened licenses")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pess back")
    wait()
    
        
    print("Successful Replay!")
    
