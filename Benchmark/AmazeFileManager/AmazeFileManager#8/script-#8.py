# bug reproduction script for bug #1232 of AFM
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
    d.app_start("com.amaze.filemanager.debug", "com.amaze.filemanager.ui.activities.MainActivity")
    wait()

    current_app = d.app_current()
    print(current_app)
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: Tapped on menu")
    wait()
    
    out =d(resourceId="com.amaze.filemanager.debug:id/design_navigation_view").scroll.toEnd()
    if not out:
        print("Success: scroll down")
    wait()
    
    out = d(text="Settings").click()
    if not out:
        print("Success: clicked on settings")
    wait()
    
    out = d.press("recent")
    if not out:
        print("Success: Opened Overview")
    wait()
    
    out = d.swipe(200, 1200, 900, 1200, 0.5)
    if not out:
        print("Success: swiped right")
    wait()
    
    out = d(resourceId="com.google.android.apps.nexuslauncher:id/icon").click()
    if not out:
        print("Success: opened options")
    wait()
    
    out = d(className="android.widget.LinearLayout", index=1).click()
    if not out:
        print("Success: clicked on split screen")
    wait()
    

    
    out = d(className="android.widget.FrameLayout", index=0).swipe("left")
    if not out:
        print("Success: swiped left")
    wait()
    
    out = d(description="Amaze Debug Amaze").click()
    if not out:
        print("Success: clicked on amaze")
    wait()
    
    out = d(description="Navigate up").click()
    if not out:
        print("Success: clicked back")
    wait()
    
    print("Successful Replay!")
    
