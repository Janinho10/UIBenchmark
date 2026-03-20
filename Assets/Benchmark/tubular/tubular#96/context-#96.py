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

    out = d(text="Chrome").click()
    if not out:
        print("Success: clicked on Chrome icon")
    wait()

    out = d(resourceId="com.android.chrome:id/search_box").click()
    if not out:
        print("Success: clicked on search bar")
    wait()