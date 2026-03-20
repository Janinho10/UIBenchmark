# bug reproduction script for bug #285 of ActivityDiary
import sys
import time
import subprocess

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    out = d(text="ADD").click()
    if not out:
        print("Success: clicked on ADD")
    wait()
    
    out = d(text="another_demo.pdf").click()
    if not out:
        print("Success: clicked on another_demo")
    wait()
    
    out = d(resourceId="com.michaeltroger.gruenerpass:id/add").click()
    if not out:
        print("Success: clicked on Add new PDF")
    wait()
    
    out = d(scrollable=True).scroll.to(text="qr.pdf")
    if not out:
        print("Success: Scroll to qr.pdf")
    wait()
    
    out = d(text="qr.pdf").click()
    if not out:
        print("Success: clicked on qr")
    wait()
    
    out = d(resourceId="com.michaeltroger.gruenerpass:id/add").click()
    if not out:
        print("Success: clicked on Add new PDF")
    wait()
    
    out = d(scrollable=True).scroll.to(text="demo.pdf")
    if not out:
        print("Success: Scroll to demo.pdf")
    wait()
    
    out = d(text="demo.pdf").click()
    if not out:
        print("Success: clicked on demo.pdf")
    wait()
    
    out = d(text="demo").click()
    if not out:
        print("Success: clicked on demo")
    wait()
    
    out = d(text="demo").click()
    if not out:
        print("Success: clicked on demo")
    wait()
    
    out = d(text="demo").set_text("my doc")
    if not out:
        print("Success: set text to my doc")
    wait()
    
    out = d(text="OK").click()
    if not out:
        print("Success: clicked OK")
    wait()
    
    out = d(description="More options").click()
    if not out:
        print("Success: clicked on More options")
    wait()
    
    out = d(text="Scroll to first PDF").click()
    if not out:
        print("Success: clicked on Scroll to first PDF")
    wait()

    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolld to second pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.backward()
    if not out:
        print("Success: scrolld to first pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolld to second pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.backward()
    if not out:
        print("Success: scrolld to first pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolld to second pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolld to third pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.backward()
    if not out:
        print("Success: scrolld to second pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.backward()
    if not out:
        print("Success: scrolld to first pdf")
    wait()
    
    out = d(description="Search").click()
    if not out:
        print("Success: clicked on Search")
    wait()
    
    out = d(focused=True).set_text("my")
    if not out:
        print("Success: set text to my")
    wait()
    
    out = d(description="Delete").click()
    if not out:
        print("Success: clicked on Delete")
    wait()
    
    out = d(text="OK").click()
    if not out:
        print("Success: clicked OK")
    wait()
    
    out = d(description="Collapse").click()
    if not out:
        print("Success: clicked on Collapse")
    wait()
    out = d(description="More options").click()
    if not out:
        print("Success: clicked on more options")
    wait()
    
    out = d(text="Switch layout").click()
    if not out:
        print("Success: clicked on Switch layout")
    wait()

    out = d(text="another_demo").click()
    if not out:
        print("Success: clicked on another_demo")
    wait()
    
    out = d(description="Navigate up").click()
    if not out:
        print("Success: clicked on Collapse")
    wait()
    
    out = d(text="qr").click()
    if not out:
        print("Success: clicked on qr")
    wait()
    
    out = d(description="Navigate up").click()
    if not out:
        print("Success: clicked on Navigate up")
    wait()
    
    out = d.open_notification()
    if not out:
        print("Success: opened drag down menu")
    wait()
    
    out = d.open_quick_settings()
    if not out:
        print("Success: opened settings")
    wait()
    
    out = d(text="Dark theme").click()
    if not out:
        print("Success: pressed Dark theme")
    wait()
    
    out = d().scroll.forward(direction="vertical")
    if not out:
        print("Success: scrolled down")
    wait()
    
    out = d().scroll.forward(direction="vertical")
    if not out:
        print("Success: scrolled down")
    wait()

    print("Successful Replay!")
