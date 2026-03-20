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
    #d.app_start("com.github.libretube")
    #wait()

    #current_app = d.app_current()
    #print(current_app)
    #while True:
    #    if current_app['package'] == "com.github.libretube":
    #        break
    #    time.sleep(2)
    #wait()

    out = d(description="Search").click()
    if not out:
        print("Success: clicked on Search")
    wait()

    out = d(text="Search apps, web and more").set_text("libretube")
    if not out:
        print("Success: set search term 'libretube'")
    wait()

    out = d(resourceId="com.google.android.inputmethod.latin:id/key_pos_ime_action").click()
    if not out:
        print("Success: pressed 'enter'")
    wait()

    out = d(text="LibreTube").click()
    if not out:
        print("Success: clicked on 'LibreTube'")
    wait()

    out = d(text="DOWNLOAD").click()
    if not out:
        print("Success: clicked on 'DOWNLOAD'")
    wait(4)
    
    out = d(scrollable=True).scroll.to(text="Assets")
    if not out:
        print("Success: scrolled to 'Assets'")
    wait()
    
    out = d.press("Home")
    if not out:
        print("Success: pressed Home button")
    wait()
    
    out = d.swipe_ext("up", scale=0.7, duration=0.1)
    if not out:
        print("Success: swiped up")
    wait()
    
    out = d(description="LibreTube").click()
    if not out:
        print("Success: opened LibreTube")
    wait()
    
    out = d(description="Library").click()
    if not out:
        print("Success: clicked on Library")
    wait()
    
    out = d(description="Subscriptions").click()
    if not out:
        print("Success: clicked on Subscriptions")
    wait()
    
    out = d(packageName="com.github.libretube", description="Home").click()
    if not out:
        print("Success: clicked on Home")
    wait()
    
    out = d(description="More options").click()
    if not out:
        print("Success: opened more options")
    wait()
    
    out = d(className="android.widget.LinearLayout", index=0).click()
    if not out:
        print("Success: clicked on settings")
    wait()
    
    out = d(text="Audio and video").click()
    if not out:
        print("Success: clicked on 'Audio and video'")
    wait()
    
    out = d.press("Back")
    if not out:
        print("Success: clicked Back")
    wait()
    
    out = d(text="Appearance").click()
    if not out:
        print("Success: clicked on 'Appearance'")
    wait()
    
    out = d.press("Back")
    if not out:
        print("Success: clicked Back")
    wait()
    
    out = d(text="Instance").click()
    if not out:
        print("Success: clicked on 'Instance'")
    wait()
    
    out = d.press("Back")
    if not out:
        print("Success: clicked Back")
    wait()
    
    out = d(text="General").click()
    if not out:
        print("Success: clicked on 'Instance'")
    wait()
    
    out = d.press("Back")
    if not out:
        print("Success: clicked Back")
    wait()

    print("Successful Replay!")
