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
    
    
    out = d(description="a").click()
    if not out:
        print("Success: clicked 'a'")
    wait(1)
    
    out = d(description="m").click()
    if not out:
        print("Success: clicked 'm'")
    wait(1)
    
    out = d(description="a").click()
    if not out:
        print("Success: clicked 'a'")
    wait(1)
    
    out = d(resourceId="org.mozilla.focus:id/urlView").click()
    if not out:
        print("Success: autocompleted")
    wait()
    
    out = d(description="Go").click()
    if not out:
        print("Success: clicked 'Go'")
    wait(10)
    
    out = d(resourceId="org.mozilla.focus:id/display_url").long_click()
    if not out:
        print("Success: opened custom URL addition")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/quick_add_autocomplete_button").click()
    if not out:
        print("Success: added to custom URLs")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/display_url").long_click()
    if not out:
        print("Success: opened custom URL addition")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/quick_add_autocomplete_button").click()
    if not out:
        print("Success: added to custom URLs")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: Go back")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/menuView").click()
    if not out:
        print("Success: Opened Menu")
    wait()
    
    out = d(resourceId="org.mozilla.focus:id/settings").click()
    if not out:
        print("Success: opended Settings")
    wait()
    
    out = d(text="URL Autocomplete").click()
    if not out:
        print("Success: opened Autocomplete menu")
    wait()
    
    out = d(className="android.widget.LinearLayout", index=3).click()
    if not out:
        print("Success: Turned on Autocomplete")
    wait()
    
    out = d(className="android.widget.LinearLayout", index=4).click()
    if not out:
        print("Success: Opened Custom URLs")
    wait()
    
    
        
    print("Successful Replay!")
