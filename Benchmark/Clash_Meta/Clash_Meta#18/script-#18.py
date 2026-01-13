import sys
import time
import uiautomator2 as u2
import subprocess
import os

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
    

    d.app_start("com.github.metacubex.clash.meta")
    wait()
    
    out = d(text="Profile").click()
    if not out:
        print("Success: clicked on Profile")
    wait()
    
    out = d(description="New").click()
    if not out:
        print("Success: clicked on New Profile")
    wait(2)

    out = d(text="File").click()
    if not out:
        print("Success: clicked on File")
    wait()
    
    out = d(text="Name").click()
    if not out:
        print("Success: clicked on Name")
    wait()
    
    out = d(focused="True").set_text("Main")
    if not out:
        print("Success: set text to Main")
    wait()
    
    out = d(text="OK").click()
    if not out:
        print("Success: clicked on OK")
    wait()
    
    out = d(text="Browse Files").click()
    if not out:
        print("Success: clicked on Browse Files")
    wait()
    
    out = d(resourceId="com.github.metacubex.clash.meta:id/menu_view").click()
    if not out:
        print("Success: clicked on more options")
    wait()
    
    out = d(text="Import").click()
    if not out:
        print("Success: clicked on Import")
    wait()
    
    out = d(text="Allow").click()
    if not out:
        print("Success: clicked on Allow")
    wait()
    
    out = d(text="clash.meta.yml").click()
    if not out:
        print("Success: clicked on File")
    wait()
    
    out = d(description="Close").click()
    if not out:
        print("Success: clicked on back")
    wait()
    
    out = d(description="Save").click()
    if not out:
        print("Success: clicked on Save")
    wait()
    
    out = d(text="Main").click()
    if not out:
        print("Success: clicked on Main")
    wait()
    
    out = d(description="Close").click()
    if not out:
        print("Success: clicked on back")
    wait()

    out = d(text="Settings").click()
    if not out:
        print("Success: clicked on Settings")
    wait()
    
    out = d(text="App").click()
    if not out:
        print("Success: clicked on App")
    wait()
    
    out = d(text="Auto Restart").click()
    if not out:
        print("Success: clicked on Auto Restart")
    wait()
    
    out = d(text="Show Traffic").click()
    if not out:
        print("Success: clicked on Show Traffic")
    wait()

    out = d(description="Close").click()
    if not out:
        print("Success: clicked on back")
    wait()
    
    out = d(description="Close").click()
    if not out:
        print("Success: clicked on back")
    wait()

    out = d(text="Stopped").click()
    if not out:
        print("Success: clicked on Stopped")
    wait()


    out = d(text="OK").click()
    if not out:
        print("Success: clicked on OK")
    wait()

    out = d(text="Allow").click()
    if not out:
        print("Success: clicked on Allow")
    wait()
    
    out = d.open_quick_settings()
    if not out:
        print("Success: opened Quick Settings")
    wait()
    
    out = d(description="Open settings.").click()
    if not out:
        print("Success: opened settings")
    wait()
    
    out = d(text="Network & internet").click()
    if not out:
        print("Success: clicked on Network & internet")
    wait()
    
    out = d(text="VPN").click()
    if not out:
        print("Success: clicked on VPN")
    wait()
    
    out = d(description="Settings").click()
    if not out:
        print("Success: clicked on Settings")
    wait()
    
    out = d(text="Always-on VPN").click()
    if not out:
        print("Success: turned on VPN")
    wait()
    
    out = d(description="Navigate up").click()
    if not out:
        print("Success: clicked on back")
    wait()
    
    
    out = d(description="Navigate up").click()
    if not out:
        print("Success: clicked on back")
    wait()
    
    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: scrolled to the bottom")
    wait()
    
    out = d(text="Private DNS").click()
    if not out:
        print("Success: clicked on Private DNS")
    wait()
    
    out = d(text="Off").click()
    if not out:
        print("Success: clicked on Off")
    wait()
    
    out = d(text="Save").click()
    if not out:
        print("Success: clicked on Save")
    wait()
    
    out = gesture_back(d)
    if not out:
        print("Success: swiped back")
    wait()
    
    out = gesture_back(d)
    if not out:
        print("Success: swiped back")
    wait()
    
    out = d.open_notification()
    if not out:
        print("Success: opened Notification")
    wait()
    
    out = d(text="Main").long_click(1)
    if not out:
        print("Success: long tapped Main")
    wait()
    
    out = d(description="More settings").click()
    if not out:
        print("Success: clicked on more Settings")
    wait()
    
    out = d(description="Clash Status").click()
    if not out:
        print("Success: clicked on Clash Status")
    wait()
    
    out = gesture_back(d)
    if not out:
        print("Success: swiped back")
    wait()

    out = d.open_notification()
    if not out:
        print("Success: opened Notification")
    wait()
    
