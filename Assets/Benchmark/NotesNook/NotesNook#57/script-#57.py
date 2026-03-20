# bug reproduction script for bug #285 of ActivityDiary
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
    
    
    out = d(text="Notesnook").click()
    if not out:
        print("Success: clicked on Notesnook")
    wait()
    
    out = d(text="Create a new note").click()
    if not out:
        print("Success: clicked on new Note")
    wait()
    
    out = d(index=4, className="android.widget.Button").click()
    if not out:
        print("Success: clicked to open more options")
    wait()
    
    out = d(text="New note").click()
    if not out:
        print("Success: clicked on new Note")
    wait()
    
    out = d(className="android.widget.Button", packageName="com.streetwriters.notesnook", text="")[4].click()
    if not out:
        print("Success: clicked on insert")
    wait()
    
    out = d.click(500, 500)
    if not out:
        print("Success: clicked on screen")
    wait()
    
    out = d(text="More").click()
    if not out:
        print("Success: clicked on More")
    wait()
    
    out = d(text="More").click()
    if not out:
        print("Success: clicked on More")
    wait()
    
    out = d(scrollable=True).scroll.horiz.toEnd(steps=3)
    if not out:
        print("Success: swiped to the left")
    wait()
    
    out = d(scrollable=True).scroll.horiz.toBeginning(steps=3)
    if not out:
        print("Success: swiped to the right")
    wait()
    
    out = d(className="android.widget.Button", packageName="com.streetwriters.notesnook", text="").click()
    if not out:
        print("Success: clicked on back")
    wait()

    out = d(resourceId="left").click()
    if not out:
        print("Success: clicked on Overview")
    wait()
    
    out = d(resourceId="tab-home").click()
    if not out:
        print("Success: clicked on tab-home")
    wait()
    
    out = d(resourceId="tab-notebooks").click()
    if not out:
        print("Success: clicked on tab-notebooks")
    wait()
    
    out = d(resourceId="tab-tags").click()
    if not out:
        print("Success: clicked on tab-tags")
    wait()
    
    out = d(resourceId="sidemenu-settings-icon").click()
    if not out:
        print("Success: clicked on Menu")
    wait()
    
    wait(1)

    out = d(resourceId="sidemenu-settings-icon").click()
    if not out:
        print("Success: clicked on Menu")
    wait()
    
    out = d(resourceId="sidemenu-settings-icon").click()
    if not out:
        print("Success: clicked on Menu")
    wait()

    out = d(text="Settings").click()
    if not out:
        print("Success: clicked on Settings")
    wait()
    
    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: scrolled to bottom")
    wait()
    
    out = d(scrollable=True).scroll.toBeginning()
    if not out:
        print("Success: scrolled to Beginning")
    wait()

    out = d(resourceId="left").click()
    if not out:
        print("Success: clicked on back")
    wait()
    
    out = d.click(0.9, 0.5)
    if not out:
        print("Success: left details")
    wait()
