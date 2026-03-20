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
    
    out = d(text="Search").click()
    if not out:
        print("Success: Opened Search settings")
    wait()
    
    out = d.click(150, 250)
    if not out:
        print("Success: Clicked 'Google'")
    wait()
    
    out = d(className="android.widget.LinearLayout", index=1).click()
    if not out:
        print("Success: Open add another search engine")
    wait()
    
    out = d(text="Search engine name").set_text("test")
    if not out:
        print("Success: set text")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/learn_more").click()
    if not out:
        print("Success: clicked on the i")
    wait(10)
    
    out = d.press("back")
    if not out:
        print("Success: press back")
        
    print("Successful Replay!")
    
