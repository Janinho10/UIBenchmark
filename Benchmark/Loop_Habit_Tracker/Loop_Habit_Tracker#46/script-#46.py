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
    
    wait()
    
    out = d.app_start("org.isoron.uhabits")
    
    wait()
    
    out = d(description="Add habit").click()
    if not out:
        print("Success: clicked on add habit")
    wait()
    
    out = d(text="Name").click()
    if not out:
        print("Success: clicked on Name")
    wait()
    
    out = d(text="Name").set_text("Meditation")
    if not out:
        print("Success: set text to Meditation")
    wait()
    
    out = d(text="SAVE").click()
    if not out:
        print("Success: clicked on Save")
    wait()
    
    out = d(description="Add habit").click()
    if not out:
        print("Success: clicked on add habit")
    wait()
    
    out = d(text="Name").click()
    if not out:
        print("Success: clicked on Name")
    wait()
    
    out = d(text="Name").set_text("Reading Book")
    if not out:
        print("Success: set text to Reading Book")
    wait()
    
    out = d(text="SAVE").click()
    if not out:
        print("Success: clicked on Save")
    wait()
    
    out = d(index=3).long_click()
    if not out:
        print("Success: long clicked on Meditation date")
    wait()
    
    out = d(resourceId="org.isoron.uhabits:id/listView").child(index=1).child(resourceId="org.isoron.uhabits:id/checkmarkPanel").child(index=0).long_click()
    if not out:
        print("Success: long clicked on Reading book date")
    wait()
    
    out = d(description="More options").click()
    if not out:
        print("Success: Opened more options")
    wait()
    
    out = d(text="Night mode").click()
    if not out:
        print("Success: clicked on Night mode")
    wait()
    
    out = d(description="More options").click()
    if not out:
        print("Success: Opened more options")
    wait()
    
    out = d(text="Settings").click()
    if not out:
        print("Success: clicked on Settings")
    wait()
    
    out = d().scroll.toEnd()
    if not out:
        print("Success: scrolled to end of settings")
    wait()
    
    out = d(description="Navigate up").click()
    if not out:
        print("Success: clicked on back")
    wait()
    
    out = d(text="Reading Book").long_click(1)
    if not out:
        print("Success: long clicked on Reading book")
    wait()
    
    out = d(description="Add habit").click()
    if not out:
        print("Success: clicked on edit habit")
    wait()
    
    out = d(text="DISCARD").click()
    if not out:
        print("Success: clicked on Discard")
    wait()
    
    out = d(text="Reading Book").long_click(1)
    if not out:
        print("Success: long clicked on Reading book")
    wait()
    
    out = d(description="Filter").click()
    if not out:
        print("Success: clicked on Color Filter")
    wait()
    
    out = d(index=2).click()
    if not out:
        print("Success: clicked on yellow color")
    wait()
    
    out = d(text="Reading Book").long_click(1)
    if not out:
        print("Success: long clicked on Reading book")
    wait()
    
    out = d(description="More options").click()
    if not out:
        print("Success: clicked on More options")
    wait()
    
    out = d(text="Delete").click()
    if not out:
        print("Success: clicked on Delete")
    wait()
    
    out = d(text="OK").click()
    if not out:
        print("Success: clicked on OK")
    wait()
    
    print("Successful Replay!")
