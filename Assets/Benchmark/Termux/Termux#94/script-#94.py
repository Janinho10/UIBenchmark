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


    d(description="s").click()
    wait(0.5)

    d(description="c").click()
    wait(0.5)

    d(description="r").click()
    wait(0.5)

    d(description="e").click()
    wait(0.5)

    d(description="e").click()
    wait(0.5)

    d(description="n").click()
    wait(0.5)

    d(description="f").click()
    wait(0.5)

    d(description="e").click()
    wait(0.5)

    d(description="t").click()
    wait(0.5)

    d(description="c").click()
    wait(0.5)

    d(description="h").click()
    wait(0.5)

    d(description="Enter").click()
    wait()

    d(description="s").click()
    wait(0.5)

    d(description="c").click()
    wait(0.5)

    d(description="r").click()
    wait(0.5)

    d(description="e").click()
    wait(0.5)

    d(description="e").click()
    wait(0.5)

    d(description="n").click()
    wait(0.5)

    d(description="f").click()
    wait(0.5)

    d(description="e").click()
    wait(0.5)

    d(description="t").click()
    wait(0.5)

    d(description="c").click()
    wait(0.5)

    d(description="h").click()
    wait(0.5)

    d(description="Enter").click()