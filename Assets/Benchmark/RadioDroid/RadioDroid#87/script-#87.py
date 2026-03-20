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

    out = d(text="RadioDroid").click()
    if not out:
        print("Success: clicked on RadioDroid")
    wait()

    out = d(description="Search").click()
    if not out:
        print("Success: clicked on Search")
    wait()

    out = d(focused=True).set_text("bbc radio")
    if not out:
        print("Success: set text to bbc radio")
    wait()

    out = d.press("Back")
    if not out:
        print("Success: get rid of keyboard")
    wait()

    out = d.set_orientation("r")
    if not out:
        print("Success: set orientation")
    wait()