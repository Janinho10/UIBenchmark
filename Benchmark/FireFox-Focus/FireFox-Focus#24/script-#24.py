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
    
    out = d(resourceId="org.mozilla.focus:id/next").click()
    if not out:
        print("Success: Clicked Next")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/next").click()
    if not out:
        print("Success: Clicked Next")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/next").click()
    if not out:
        print("Success: Clicked Next")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/finish").click()
    if not out:
        print("Success: Clicked 'OK, got It!'")
    wait()
    
    
    out = d(description="f").click()
    if not out:
        print("Success: clicked 'f'")
    wait(1)
    
    out = d(description="i").click()
    if not out:
        print("Success: clicked 'i'")
    wait()
    
    out = d.click(25, 150)
    if not out:
        print("Success: tap input bar")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/clearView").click()
    if not out:
        print("Success: Pressed Erase button")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: Go back")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: Go back")
    
    print("Successful Replay!")
    
