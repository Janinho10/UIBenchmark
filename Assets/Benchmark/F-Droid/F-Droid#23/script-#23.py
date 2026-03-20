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
    
    out = d(text="F-Droid").click()
    if not out:
        print("Success: F-Droid")
    wait()
    
    out = d(description="Search").click()
    if not out:
        print("Success: clicked on Search")
    wait()
    
    out = d(text="Search apps").click()
    if not out:
        print("Success: clicked on Search bar")
    wait()
    
    out = d(text="Search apps").set_text("fossify")
    if not out:
        print("Success: set text to fossify")
    wait()
    
    out = d(resourceId="org.fdroid.fdroid:id/app_list").scroll.to(text="Fossify Gallery Gallery with Photo editor. No Ads, Open-source, Private. No strings attached.")
    if not out:
        print("Success: scrolled to Gallery")
    wait()
    
    out = d(text="Fossify Gallery Gallery with Photo editor. No Ads, Open-source, Private. No strings attached.").click()
    if not out:
        print("Success: clicked on Gallery")
    wait()
    
    print("Successful Replay!")
