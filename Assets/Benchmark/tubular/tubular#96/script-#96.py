import sys
import time
import subprocess
import uiautomator2 as u2
import os

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

if __name__ == '__main__':
    avd_serial = "emulator-5554"
    d = u2.connect(avd_serial)

    out = d(focused=True).set_text("tubular fdroid")
    if not out:
        print("Success: set text")
    wait()

    d.press("Enter")
    wait()

    out = d(text="Tubular | F-Droid – Freies und quelloffenes Android-App- ...").click()
    if not out:
        print("Success: clicked on Tubular")
    wait()

    max_attempts = 10
    attempts = 0
    while attempts < max_attempts:
        if d(textContains="Download APK").exists():
            print("Found Download APK")
            break
        d(scrollable=True).scroll.toEnd()
        attempts += 1
        wait(1)
    
    if attempts == max_attempts:
        print("Download APK not found after maximum attempts")
    wait()

    out = d(textContains="Download APK").click()
    if not out:
        print("Success: clicked on Download")
    wait()

    out = d(text="Download anyway").click()
    if not out:
        print("Success: clicked on Download anyway")
    wait()

    out = d(text="Open").click()
    if not out:
        print("Success: click on Open")
    wait()

    out = d(text="Allow").click()
    if not out:
        print("Success: click on Allow")
    wait()

    out = d(text="Popup").click()
    if not out:
        print("Success: clicked on Popup")
    wait()

    out = d.swipe(fx=0, fy=500, tx=100, ty=500, steps=1)
    if not out:
        print("Success: Gesture back")
    wait()

    out = d(description="Open Drawer").click()
    if not out:
        print("Success: opened Drawer")
    wait()

    out = d.click(x=800, y=500)
    if not out:
        print("Success: clicked somewhere")
    wait()