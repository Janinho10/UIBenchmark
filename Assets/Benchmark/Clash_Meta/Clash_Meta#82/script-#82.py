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

    out = d(text="Browse Files").click()
    if not out:
        print("Success: clicked on Browse Files")
    wait()

    out = d(text="Provider Files").click()
    if not out:
        print("Success: clicked on Provider Files")
    wait()

    out = d(resourceId="com.github.kr328.clash:id/new_view").click()
    if not out:
        print("Success: clicked on add files")
    wait()

    out = d(text="proxy_provider").click()
    if not out:
        print("Success: clicked on proxy provider")
    wait()

    out = d(text="umum.yaml").click()
    if not out:
        print("Success: clicked on umum.yaml")
    wait()

    out = d(text="OK")
    if not out:
        print("Success: clicked on OK")
    wait()

    out = d(resourceId="com.github.kr328.clash:id/new_view").click()
    if not out:
        print("Success: clicked on add files")
    wait()

    out = d(text="trafficIndo.yaml").click()
    if not out:
        print("Success: clicked on trafficIndo.yaml")
    wait()

    out = d(text="OK")
    if not out:
        print("Success: clicked on OK")
    wait()

    out = d(resourceId="com.github.kr328.clash:id/new_view").click()
    if not out:
        print("Success: clicked on add files")
    wait()

    out = d(text="streaming.yaml").click()
    if not out:
        print("Success: clicked on streaming.yaml")
    wait()

    out = d(text="OK")
    if not out:
        print("Success: clicked on OK")
    wait()

    out = d(resourceId="com.github.kr328.clash:id/new_view").click()
    if not out:
        print("Success: clicked on add files")
    wait()

    out = d(text="sosmed.yaml").click()
    if not out:
        print("Success: clicked on sosmed.yaml")
    wait()

    out = d(text="OK")
    if not out:
        print("Success: clicked on OK")
    wait()

    out = d(resourceId="com.github.kr328.clash:id/new_view").click()
    if not out:
        print("Success: clicked on add files")
    wait()

    out = d(text="gaming.yaml").click()
    if not out:
        print("Success: clicked on gaming.yaml")
    wait()

    out = d(text="OK")
    if not out:
        print("Success: clicked on OK")
    wait()

    out = d(resourceId="com.github.kr328.clash:id/activity_bar_close_view").click()
    if not out:
        print("Success: clicked on back")
    wait()

    out = d(resourceId="com.github.kr328.clash:id/activity_bar_close_view").click()
    if not out:
        print("Success: clicked on back")
    wait()