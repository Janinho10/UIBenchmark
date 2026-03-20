# bug reproduction script for bug #285 of ActivityDiary
import sys
import time

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

def open_app_drawer(d):
    d.press("home")
    time.sleep(1)
    
    width, height = d.window_size()
    d.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 0.1)
    time.sleep(2)
    
if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    open_app_drawer(d)
    wait()
    
    d.app_start("org.schabi.newpipe")
    
    wait()
    
    out = d(resourceId="org.schabi.newpipe:id/action_search").click()
    if not out:
        print("Success: clicked on Search")
    wait()
    
    out = d(resourceId="org.schabi.newpipe:id/toolbar_search_edit_text").long_click(1)
    if not out:
        print("Success: long-clicked the Search bar")
    wait()
    
    out = d(description="Paste").click()
    if not out:
        print("Success: clicked on paste")
    wait()
    
    out = d.press("enter")
    if not out:
        print("Success: pressed enter")
    wait()
    print("Successful Replay!")
