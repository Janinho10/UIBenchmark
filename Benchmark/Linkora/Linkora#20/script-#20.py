import sys
import time
import subprocess
import uiautomator2 as u2

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)
        
def gesture_back(d):
    width, height = d.window_size()
    
    d.swipe(width * 0.98, height / 2, width * 0.5, height / 2, duration=0.1)

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    
    out = d(scrollable=True).scroll.to(text="SHOW MORE")
    if not out:
        print("Success: scrolled to show more")
    wait()
    
    out = d(text="SHOW MORE").click()
    if not out:
        print("Success: clicked on SHOW MORE")
    wait()
    
    out = d(scrollable=True).scroll.toBeginning()
    if not out:
        print("Success: scrolled to Launch")
    wait()
 
    out = d(text="Launch").click()
    if not out:
        print("Success: clicked on Launch")
    wait()

    out = d.swipe(width * 0.8, height / 2, width * 0.5, height / 2, duration=0.1)
    if not out:
        print("Success: failed to swipe left")
    wait()
    
    out = d.swipe(width * 0.8, height / 2, width * 0.3, height / 2, duration=0.1)
    if not out:
        print("Success: succeeded in swiping right")
    wait()
    
    out = d(text="Search").click()
    if not out:
        print("Success: click Search")
    wait()
    
    out = d(text="Collections").click()
    if not out:
        print("Success: clicked Collections")
    wait()
    
    out = d(text="Search").click()
    if not out:
        print("Success: clicked Search")
    wait()

    out = d.swipe(width / 2, height * 0.8, width / 2, height * 0.2, duration=0.2)
    if not out:
        print("Success: Scrolled Down")
    wait()
    
    out = d.swipe(width / 2, height * 0.2, width / 2, height * 0.8, duration=0.2)
    if not out:
        print("Success: Scrolled Up")
    wait()
    
    out = d(text="Theme").click()
    if not out:
        print("Success: clicked Theme")
    wait()
    
    out = gesture_back(d)
    if not out:
        print("gesture back")
    wait()

    out = d(text="General").click()
    if not out:
        print("Success: clicked on General")
    wait()
    
    out = gesture_back(d)
    if not out:
        print("gesture back")
    wait()

    out = d(text="Advanced").click()
    if not out:
        print("Success: clicked on Advanced")
    wait()
    
    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: scrolled to End")
    wait()

    out = gesture_back(d)
    if not out:
        print("gesture back")
    wait()
    
    out = d(text="Link Layout").click()
    if not out:
        print("Success: clicked on Link Layout")
    wait()
