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

    out = d(text="Immich").click()
    if not out:
        print("Success: opened Immich")
    wait()

    out = d(className="android.widget.EditText").click()
    if not out:
        print("Success: clicked on Text")
    wait()

    out = d(className="android.widget.Button").click()
    if not out:
        print("Success: clicked on settings")
    wait()

    out = d(description="Advanced\nAdvanced user's settings").click()
    if not out:
        print("Success: clicked on Advanced")
    wait()

    out = d(description="Back").click()
    if not out:
        print("Success: clicked on Back")
    wait()

    out = d(description="Asset Viewer\nManage your gallery viewer settings")
    if not out:
        print("Success: clicked on Asset Viewer")
    wait()

    out = d(description="Back").click()
    if not out:
        print("Success: clicked on Back")
    wait()

    out = d(description="Backup\nManage upload settings")
    if not out:
        print("Success: clicked on Backup")
    wait()

    out = d(description="Back").click()
    if not out:
        print("Success: clicked on Back")
    wait()

    out = d(description="Networking\nManage the server endpoint settings")
    if not out:
        print("Success: clicked on Networking")
    wait()

    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: scrolled to the bottom")
    wait()

    out = d(scrollable=True).scroll.toBeginning()
    if not out:
        print("Success: scrolled to the top")
    wait()  

    out = d(description="Back").click()
    if not out:
        print("Success: clicked on Back")
    wait()  

    out = d(description="Preferences\nManage the app's preferences")
    if not out:
        print("Success: clicked on Preferences")
    wait()

    out = d(description="Back").click()
    if not out:
        print("Success: clicked on Back")
    wait()

    out = d(description="Photo Grid\nPhoto grid layout settings")
    if not out:
        print("Success: clicked on Photo Grid")
    wait()

    out = d(description="Back").click()
    if not out:
        print("Success: clicked on Back")
    wait()

    out = d(description="Back").click()
    if not out:
        print("Success: clicked on Back")
    wait()