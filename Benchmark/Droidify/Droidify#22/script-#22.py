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
    d.app_start("org.fdroid.fdroid")
    wait()

    current_app = d.app_current()
    print(current_app)
   
    
    out = d(text="Settings").click()
    if not out:
        print("Success: clicked on Settings")
    wait()
    
    out = d(text="About F-Droid").click()
    if not out:
        print("Success: clicked on About F-Droid")
    wait()
    
    out = d(text="OK").click()
    if not out:
        print("Success: clicked on OK")
    wait()
    
    
    out = d.press("home")
    if not out:
        print("Success: pressed home button")
    wait()
    
    out = d(text="Droid-ify").click()
    if not out:
        print("Success: clicked on Droid-ify")
    wait()
    
    out = d(description="More options").click()
    if not out:
        print("Success: clicked on more options")
    wait()
    
    out = d(text="Settings").click()
    if not out:
        print("Success: clicked on Settings")
    wait()
    
    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: scrolled to bottom")
    wait()
    
    out = d(text="Droid-ify").click()
    if not out:
        print("Success: Clicked on Droid-ify")
    wait()
    
    out = d().scroll.forward(direction="vertical")
    if not out:
        print("Success: Scrolled to Screenshots")
    wait()
    
    out = d.press("Back")
    if not out:
        print("Success: pressed Back")
    wait()
    
    out = d.press("Back")
    if not out:
        print("Success: pressed Back")
    wait()
    
    out = d(text="All applications").click()
    if not out:
        print("Success: clicked on all applications")
    wait()
    
    out = d().scroll.toEnd()
    if not out:
        print("Success: scrolled through all application types")
    wait()
    
    out = d(description="Installed").click()
    if not out:
        print("Success: clicked on Installed")
    wait()
    
    out = d(description="Updates").click()
    if not out:
        print("Success: clicked on Updates")
    wait()
    
    out = d(description="Installed").click()
    if not out:
        print("Success: clicked on Installed")
    wait()
    
    out = d(description="Explore").click()
    if not out:
        print("Success: clicked on Explore")
    wait()
    
    out = d().scroll.forward(direction="vertical")
    if not out:
        print("Success: scrolled down")
    wait()
    
    out = d(resourceId="com.looker.droidify:id/scroll_up").click()
    if not out:
        print("Success: clicked on scroll up button")
    wait()
    
    out = d(description="Sync repositories").click()
    if not out:
        print("Success: synched repositories")
    wait()
    
    out = d(description="More options").click()
    if not out:
        print("Success: clicked on more options")
    wait()
    
    out = d(text="Repositories").click()
    if not out:
        print("Success: clicked on Repositories")
    wait()
    
    out = d().scroll.toEnd()
    if not out:
        print("Success: scrolled down")
    wait()
    
    out = d().scroll.toBeginning()
    if not out:
        print("Success: scrolled to Beginning")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d(description="More options").click()
    if not out:
        print("Success: clicked on more options")
    wait()
    
    out = d(text="Settings").click()
    if not out:
        print("Success: clicked on Settings")
    wait()
    
    out = d(text="Theme").click()
    if not out:
        print("Success: clicked on Theme")
    wait()
    
    out = d(text="Cancel").click()
    if not out:
        print("Success: closed pop-up")
    wait()
    
    out = d().scroll.to(text="Installer")
    if not out:
        print("Success: scrolled to Installer")
    wait()
    
    out = d(text="Installer").click()
    if not out:
        print("Success: clicked on Installer")
    wait()
    
    out = d(text="Cancel").click()
    if not out:
        print("Success: clicked on Cancel")
    wait()
    
    out = d().scroll.toBeginning()
    if not out:
        print("Success: scrolled to Beginning")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d.press("home")
    if not out:
        print("Success: pressed home")
    
    print("Successful Replay!")
