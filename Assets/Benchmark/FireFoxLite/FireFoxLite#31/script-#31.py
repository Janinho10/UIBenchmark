# bug reproduction script for bug #4881 of firefoxlite
# this one requires a 1080*1920 screen.
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

    d.app_start("org.mozilla.rocket.debug.ting")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "org.mozilla.rocket.debug.ting":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()


    out = d(resourceId="org.mozilla.rocket.debug.ting:id/bottom_bar_home").click()
    if not out:
        print("Success: press shop")
    wait()

    out = d(text="Enter a product name").set_text("desk")
    if not out:
        print("Success: enter desk")
    wait(4)
    
    x = (918 + 1080) // 2
    y = (1634 + 1799) // 2

    out = d.click(x, y)
    
    #out = d.press("search")
    if not out:
        print("Success: Query")
    
    wait(8)
    
    #out = d(className="android.webkit.WebView", scrollable=True).scroll.to(description="Alle akzeptieren Alle akzeptieren")
    
    out = d(className="androidx.viewpager.widget.ViewPager", resourceId="org.mozilla.rocket.debug.ting:id/view_pager").swipe("up")
    if not out:
        print("Success: scroll")
    wait()
    
    out = d(className="androidx.viewpager.widget.ViewPager", resourceId="org.mozilla.rocket.debug.ting:id/view_pager").swipe("up")
    if not out:
        print("Success: scroll")
    wait()
    
    out = d(description="Alle akzeptieren Alle akzeptieren").click()
    if out:
        print("Success: accepted Cookies")
    wait(6)

    #out = d(text="desk", resourceId="org.mozilla.rocket.debug.ting:id/suggestion_item").click()
    #if not out:
   #     print("Success: press desk")
   # wait(15)

    d(description="Videos").click()
    print("Success: press Videos")
    wait()

    #out = d(className="android.webkit.WebView").swipe("up")
    #if out:
    #    print("Success: scroll down")
    #wait()

    d.click(200, 700)
    print("Success: press Video")
    wait(15)

    d.click(549, 608)
    print("Success: press Video")
    wait(5)

    d.click(1000, 800)
    print("Success: press Video")
    wait(1)

    d.click(1000, 800)
    print("Success: press Video")
    wait()

    print("Successful Replay!")
