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
        print("Success: Clicked 'f'")
    wait(1)
    
    out = d(description="a").click()
    if not out:
        print("Success: Clicked 'a'")
    wait(1)
    
    out = d(description="c").click()
    if not out:
        print("Success: Clicked 'c'")
    wait(1)
    
    out = d(description="Go").click()
    if not out:
        print("Success: Clicked 'Go'")
    wait(10)
    
    out = d.press("home")
    if not out:
        print("Success: pressed home")
    wait()
    
    d.open_notification()
    
    wait()
    
    out = d.click(540, 521)
    if not out:
        print("Success: Erased browsing history")
    wait()
    
    out = d.press("recent")
    if not out:
        print("Success: Opened Recents")
    wait()
     
    out = d.press("home")
    if not out:
        print("Success: pressed home")
    
        
    print("Successful Replay!")
