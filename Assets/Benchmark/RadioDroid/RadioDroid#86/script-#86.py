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

    out = d.open_quick_settings()
    if not out:
        print("Success: opened quick settings")
    wait()

    out = d(description="Auto-rotate screen").click()
    if not out:
        print("Success: clicked on Auto-rotate")
    wait()

    out = d.swipe(fx=500, fy=1800, tx=500, ty=400, duration=1)
    if not out:
        print("Success: closed Settings")
    wait()

    out = d.set_orientation("r")
    if not out:
        print("Success: changed screen orientation")
    wait()

    out = d(description="More").click()
    if not out:
        print("Success: clicked on More button")
    wait()

    out = d(description="Set alarm").click()
    if not out:
        print("Success: clicked on set alarm")
    wait()

    out = d.set_orientation("n")
    if not out:
        print("Success: changed screen orientation")
    wait()

    out = d(text="CANCEL").click()
    if not out:
        print("Success: clicked on Cancel")
    wait()

    out = d(description="More").click()
    if not out:
        print("Success: clicked on More button")
    wait()

    out = d(description="Set alarm").click()
    if not out:
        print("Success: clicked on set alarm")
    wait()

    out = d.set_orientation("r")
    if not out:
        print("Success: changed screen orientation")
    wait()

    