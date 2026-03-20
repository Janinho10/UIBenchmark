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

    out = d(text="Suntimes").click()
    if not out:
        print("Success: clicked on Suntimes")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: clicked on More options")
    wait()

    out = d(text="Settings").click()
    if not out:
        print("Success: clicked on Settings")
    wait()

    out = d(text="General Settings").click()
    if not out:
        print("Success: clicked on General Settings")
    