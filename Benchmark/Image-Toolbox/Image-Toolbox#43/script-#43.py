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
    
    out = d(text="Image Toolbox").click()
    if not out:
        print("Success: Opened Image Toolbox")
    wait()
    
    out = d.swipe(0.95, 0.5, 0.05, 0.5, 0.2)
    if not out:
        print("Success: opened Settings")
    wait()
    
    out = d.swipe(0.05, 0.5, 0.95, 0.5, 0.2)
    if not out:
        print("Success: close Settings")
    wait()
    
    out = d(text="Create").click()
    if not out:
        print("Success: clicked on create")
    wait()
    
    out = d(text="Image").click()
    if not out:
        print("Success: clicked on Image")
    wait()

    out = d(text="Tools").click()
    if not out:
        print("Success: clicked on Tools")
    wait()
    
    out = d(text="Edit").click()
    if not out:
        print("Success: clicked on Edit")
    wait()
    
    print("Successful Replay!")
