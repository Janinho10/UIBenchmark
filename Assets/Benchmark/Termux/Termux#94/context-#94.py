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

    package_name = "com.termux"

    d.app_start(package_name)
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

    d(description="Space").click()
    wait(0.5)

    d(description="i").click()
    wait(0.5)

    d(description="n").click()
    wait(0.5)

    d(description="s").click()
    wait(0.5)

    d(description="t").click()
    wait(0.5)

    d(description="a").click()
    wait(0.5)

    d(description="l").click()
    wait(0.5)

    d(description="l").click()
    wait(0.5)

    d(description="Enter").click()
    wait(0.5)