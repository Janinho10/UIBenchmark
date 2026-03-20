# bug reproduction script for bug #285 of ActivityDiary
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
    d.app_start("com.carriez.flutter_hbb")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.carriez.flutter_hbb":
            break
        time.sleep(2)
    wait()
    
    out = d(descriptionContains="Share").click()
    if not out:
        print("Success: clicked on Share Screen")
    wait()
    
    out = d(description="Start Service").click()
    if not out:
        print("Success: clicked on Start Service")
    wait()
    
    out = d(description="OK").click()
    if not out:
        print("Success: clicked on OK")
    wait()
    
    out = d(text="Cancel").click()
    if not out:
        print("Success: clicked on Cancel")
    wait()
    
    out = d(index=0, description="OPEN").click()
    if not out:
        print("Success: clicked on OPEN")
    wait()
    
    out = d(description="OK").click()
    if not out:
        print("Success: clicked on OK")
    wait()
    
    out = d(text="Start now").click()
    if not out:
        print("Success: clicked on Cancel")
    wait()
    
    out = d(index=1, description="OPEN").click()
    if not out:
        print("Success: clicked on OPEN")
    wait()
    
    out = d(description="Open System Setting").click()
    if not out:
        print("Success: opened System Setting")
    wait()
    
    out = d(text="RustDesk Input").click()
    if not out:
        print("Success: clicked on RustDesk Input")
    wait()
    
    out = d(text="OFF").click()
    if not out:
        print("Success: turned on RustDesk Input")
    wait()
    
    out = d(text="OK").click()
    if not out:
        print("Success: clicked on OK")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d(descriptionContains="Share").click()
    if not out:
        print("Success: clicked on Share Screen")
    wait()
    
    out = d(index=2, description="OPEN").click()
    if not out:
        print("Success: clicked on Open")
    wait()
    
    out = d(text="Allow").click()
    if not out:
        print("Success: clicked on Allow")
    wait()

    print("Successful Replay!")
