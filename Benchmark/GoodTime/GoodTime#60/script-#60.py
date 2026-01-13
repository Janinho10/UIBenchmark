import sys
import time
import subprocess
import uiautomator2 as u2

def wait(seconds=2):
    for i in seconds:
        time.sleep(1)
        print("wait ")
        
def gesture_back(d):
    width, height = d.window_size()
    
    d.swipe(width * 0.98, height / 2, width * 0.5, height / 2, duration=0.1)

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    goodtime = "com.apps.adrcotfas.goodtime"
    
    d.app_start(goodtime)
    wait()
    
    width, height = d.window_size()
    
    out = d(text="25.00").click()
    if not out:
        print("Success: started timer")
    wait()
    
    out = d.swipe(width / 2, height * 0.4, width / 2, height * 0.5, duration=0.05)
    if not out:
        print("Success: stopped timer")
    wait()
    
    out = d(description="Navigate up").click()
    if not out:
        print("Success: clicked on Options")
    wait()
    
    out = d(text="Settings").click()
    if not out:
        print("Success: clicked on Settings")
    wait()
    
    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: scrolled to end")
    wait()
    
    out = gesture_back(d)
    if not out:
        print("gesture back")



