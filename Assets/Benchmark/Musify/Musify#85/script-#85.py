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

    out = d(scrollable=True).swipe("up")
    if not out:
        print("swiped up")
    wait()

    out = d(text="Musify").click()
    if not out:
        print("Success: clicked on Musify")
    wait()

    out = d(className="android.view.View", scrollable=True, instance=0).scroll.horiz()
    if not out:
        print("Success: scrolled horizontally")
    wait()

    out = d(description="Search\nTab 2 of 4").click()
    if not out:
        print("Success: clicked on Search")
    wait()

    out = d(className="android.widget.EditText").click()
    if not out:
        print("Success: clicked on Search bar")
    wait()

    out = d(focused=True).set_text("hindi")
    if not out:
        print("Success: set text to hindi")
    wait()

    out = d(description="hindi").click()
    if not out:
        print("Success: clicked on hindi")
    wait()