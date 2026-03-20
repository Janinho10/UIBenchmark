# bug reproduction script for bug #3222 of collect
import os
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

    current_app = d.app_current()
    print(current_app)
    wait()
    
    out = d(description="More options").click()
    if not out:
        print("Success: press more options")
    wait()

    out = d(text="General Settings").click()
    if not out:
        print("Success: press General Settings")
    wait()

    out = d(text="Form management").click()
    if not out:
        print("Success: press Form management")
    wait()

    out = d(text="Hide old form versions").click()
    if not out:
        print("Success: press Hide old form versions")
    wait()

    d.press("back")
    d.press("back")
    print("Success: doulbe back")

    out = d(text="Fill Blank Form").click()
    if not out:
        print("Success: press Fill Blank Form")
    wait()

    print("Successful Replay!")
