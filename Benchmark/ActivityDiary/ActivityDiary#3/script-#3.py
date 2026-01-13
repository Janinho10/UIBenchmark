# bug reproduction script for bug #285 of ActivityDiary
import sys
import time
import subprocess
import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "de.rampro.activitydiary.debug"
    component_name = "de.rampro.activitydiary.debug/de.rampro.activitydiary.ui.main.MainActivity"
    
    start_cmd = f"adb -s {avd_serial} shell am start -n {component_name} -a android.intent.action.MAIN -c android.intent.category.LAUNCHER"
    subprocess.run(start_cmd, shell=True)
    wait()

    # click the Navigation
    out = d(className="android.widget.ImageButton", description="Open navigation").click()
    if not out:
        print("Success: press Navigation")
    wait()

    # click the Settings
    out = d(className="android.widget.CheckedTextView", text="Settings").click()
    if not out:
        print("Success: press Settings")
    wait()

    # scroll down the settings
    out = d(scrollable=True).scroll.to(text="Location Service")
    if out:
        print("Success: Scroll down")
    wait()

    # click Location Service
    out = d(className="android.widget.TextView", text="Location Service").click()
    if not out:
        print("Success: press Location Service")
    wait()

    # click Network
    out = d(className="android.widget.CheckedTextView", text="Network").click()
    if not out:
        print("Success: press Network")
    wait()

    # click Update period
    out = d(className="android.widget.TextView", text="Update period").click()
    if not out:
        print("Success: press update period")
    wait()

    # set the edittext to empty
    out = d(className="android.widget.EditText").set_text(text="")
    if out:
        print("Success: set text to empty")
    wait()

    # click Ok
    out = d(className="android.widget.Button", text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    print("Successful Replay!")
