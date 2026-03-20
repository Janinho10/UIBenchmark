# bug reproduction script for bug #67 of openlauncher
import os
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

    d.app_start("com.benny.openlauncher")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.benny.openlauncher":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    #out = d(text="SKIP").click()
    #if not out:
    #    print("SUCCESS")
    #wait()
    
    out = d(resourceId="com.benny.openlauncher:id/ib_next").click()
    
    wait()
    
    out = d(resourceId="com.benny.openlauncher:id/ib_next").click()
    
    wait()
    
    out = d(resourceId="com.benny.openlauncher:id/btn_finish").click()
    
    wait()

    w, h = d.window_size()

# Swipe from top center down to middle
    d.swipe(w // 2, 0, w // 2, h // 2, 0.5)
    wait()
    
    out = d(className="android.widget.Switch", text="Off").click()
    wait()
    
    out = d(description="Priority only").click()
    wait()
    
    out = d(text="DONE").click()
    wait()
    
    out = d.click(500, 500)
    wait()
    
    d.swipe(0.0, 0.5, 0.5, 0.5)
    print("SUCCESS")
    wait()

    out = d(resourceId="com.benny.openlauncher:id/minBar").child(index="6").click()
    if not out:
        print("SUCCESS")
    wait()

    print("Successful Replay!")
