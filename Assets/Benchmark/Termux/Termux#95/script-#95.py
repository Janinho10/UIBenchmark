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

    out = d(text="Termux").click()
    if not out:
        print("Success: clicked on Termux")
    wait()

    d(description="a").click()
    wait(0.5)

    d(description="p").click()
    wait(0.5)

    d(description="t").click()
    wait(0.5)

    d(description="Space").click()
    wait(0.5)

    d(description="u").click()
    wait(0.5)

    d(description="p").click()
    wait(0.5)

    d(description="d").click()
    wait(0.5)

    d(description="a").click()
    wait(0.5)

    d(description="t").click()
    wait(0.5)

    d(description="e").click()
    wait(0.5)

    d(description="Enter").click()
    wait(4)

    d(description="a").click()
    wait(0.5)

    d(description="p").click()
    wait(0.5)

    d(description="t").click()
    wait(0.5)

    d(description="u").click()
    wait(0.5)

    d(description="o").click()
    wait(0.5)

    d(description="g").click()
    wait(0.5)