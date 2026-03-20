import sys
import time
import subprocess
import uiautomator2 as u2

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':
    avd_serial = 'emulator-5554'
    d = u2.connect(avd_serial)

    out = d(text="aFreeRDP").click()
    if not out:
        print("Success: clicked on 'aFreeRDP' icon")
    wait()

    out = d(text="Add Connection").click()
    if not out:
        print("Success: clicked on Add Connection")
    wait()

    out = d(text="Credentials", index=0).click()
    if not out:
        print("Success: clicked on Credentials")
    wait()

    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()

    out = d(text="Screen").click()
    if not out:
        print("Success: clicked on Screen")
    wait()

    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()

    out = d(text="Performance").click()
    if not out:
        print("Success: clicked on Performance")
    wait()

    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()

    out = d(text="Advanced").click()
    if not out:
        print("Success: clicked on Advanced")
    wait()

    out = d(text="Security").click()
    if not out:
        print("Success: clicked on Security")
    wait()

    out = d(resourceId="android:id/button2").click()
    if not out:
        print("Success: clicked on 'Cancel'")
    wait()

    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()

    out = d(text="Debug Settings").click()
    if not out:
        print("Success: clicked on 'Debug Settings'")
    wait()

    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()

    print("Finished Scenario!")