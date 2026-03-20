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
    #d.press("power")
    wait()
    
    out = d().long_click(2)
    if not out:
        print("Success: Opened Settings")
    wait()
    
    out = d(text="Dark").click()
    if not out:
        print("Success: clicked on Dark")
    wait()
    
    out = d(text="Light").click()
    if not out:
        print("Success: clicked on Light")
    wait()
    

    
    out = d().scroll.forward(direction="vertical")
    
    if not out:
        print("Success: scrolled down")
    wait()
    
    d.press("Back")
    
    wait()
    
    out = d().scroll.forward(direction="vertical")
    
    if not out:
        print("Success: scrolled down")
    wait()
    
    out = d().scroll.backward(direction="vertical")
    if not out:
        print("Success: scrolled up")
    wait()
    
    d.press("Back")
    
    out = d(text="Play Store").click()
    if not out:
        print("Success: Clicked on Play Store")
    wait()
    
    out = d(text="Search").click()
    if not out:
        print("Success: Clicked on Search Tab")
    wait()
    
    out = d.click(400.0, 150.0)
    if not out:
        print("Success: Clicked on Search Bar")
    wait()
    
    out = d(description='Search for "minimal launcher" ').click()
    
    if not out:
        print("Success: Clicked on 'minimal launcher'-search")
    wait()
    
    out = d(index=0, descriptionContains="Olauncher. Minimal AF Launcher").click()
    if not out:
        print("Success: Clicked on OLauncher")
    wait()
    print("Successful Replay!")
