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
    
    wait()
    
    out = d.app_start("com.android.vending")
    if not out:
        print("Success: opened app store")
    wait()
    
    out = d(text="Search").click()
    if not out:
        print("Success: clicked on search")
    wait()
    
    out = d(textContains="Search apps").click()
    if not out:
        print("Success: clicked the Search bar")
    wait()
    
    out = d(focused=True).set_text("deepl")
    if not out:
        print("Success: set text to deepl")
    wait()
    
    out = d.press("enter")
    if not out:
        print("Success: pressed enter")
    wait()
    
    out = d(descriptionContains="DeepL").click()
    if not out:
        print("Success: clicked on DeepL")
    wait()
    
    out = d(text="Install").click()
    if not out:
        print("Success: clicked on Install")
    wait()
    
    print("Successful Replay!")
