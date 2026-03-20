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

    out = d(text="Profile").click()
    if not out:
        print("Success: clicked on Profile")
    wait()

    out = d(resourceId="com.github.kr328.clash:id/add_view").click()
    if not out:
        print("Success: clicked on add profile")
    wait()

    out = d(text="File").click()
    if not out:
        print("Success: clicked on File")
    wait()

    out = d(text="Name").click()
    if not out:
        print("Success: clicked on Name")
    wait()

    out = d(resourceId="com.github.metacubex.clash.meta:id/text_field").set_text("clash for android")
    if not out:
        print("Success: set text to 'clash for android'")
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: clicked on OK")
    wait()

    out = d(text="Browse Files").click()
    if not out:
        print("Success: clicked on Browse Files")
    wait()

    out = d(resourceId="com.github.kr328.clash:id/menu_view").click()
    if not out:
        print("Success: clicked on menu")
    wait()

    out = d(text="Import").click()
    if not out:
        print("Success: clicked Import")
    wait()

    out = d(text="clash_for_android-main").click()
    if not out:
        print("Success: clicked on clash for android")
    wait()

    out = d(text="main.yaml").click()
    if not out:
        print("Success: clicked on main.yaml")
    wait()

    out = d(resourceId="com.github.kr328.clash:id/activity_bar_close_view").click()
    if not out:
        print("Success: clicked on back")
    wait()