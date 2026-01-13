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
    
    out = d(text="START").click()
    if not out:
        print("Success: clicked on Start")
    wait()
    
    out = d.set_clipboard("Best download app")
    if not out:
        print("Success: set clipboard text")
    wait()
    
    out = d(text="PROCEED").click()
    if not out:
        print("Success: clicked on Proceed")
    wait()
    
    out = d(text="OK").click()
    if not out:
        print("Success: clicked on OK")
    wait()
    
    out = d(textContains="RDNS").click()
    if not out:
        print("Success: pressed RDNS Default")
    wait()
    
    d.press("back")
    if not out:
        print("Success: clicked on Back")
    wait()
    
    out = d(textContains="RDNS").click()
    if not out:
        print("Success: pressed RDNS Default")
    wait()
    
    out = d(text="System DNS").click()
    if not out:
        print("Success: clicked on System DNS")
    wait()
    
    out = d(text="Other DNS").click()
    if not out:
        print("Success: clicked on other DNS")
    wait()
    
    out = d(text="Dns Proxy").click()
    if not out:
        print("Success: clicked on Dns Proxy")
    wait()
    
    out = d(text="Google").click()
    if not out:
        print("Success: clicked on Google")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d(description="Logs").click()
    if not out:
        print("Success: clicked on Logs")
    wait()
    
    out = d.swipe(0.9, 0.5, 0.1, 0.5)
    if not out:
        print("Success: swiped from right to left")
    wait()
    
    out = d.swipe(0.1, 0.5, 0.9, 0.5)
    if not out:
        print("Success: swiped from left to right")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d(textContains="IP").click()
    if not out:
        print("Success: clicked on IP & Port rules")
    wait()
    
    out = d(text="Block port 80 (insecure HTTP) traffic").click()
    if not out:
        print("Success: clicked on Block port 80")
    wait()
    
    out = d(text="Block UDP except DNS and NTP").click()
    if not out:
        print("Success: clicked on Block UDP")
    wait()
    
    out = d(text="ip & port rules").click()
    if not out:
        print("Success: clicked on IP & Port Rules")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d(description="Network Logs").click()
    if not out:
        print("Success: clicked on Network Logs")
    wait()
    
    out = d(resourceId="com.celzero.bravedns:id/connection_app_name").click()
    if not out:
        print("Success: clicked on Entry")
    wait()
    
    out = d.press("Back")
    if not out:
        print("Success: go back")
    wait()
    
    out = d.press("Back")
    if not out:
        print("Success: go back")
    wait()
    
    out = d(resourceId="com.celzero.bravedns:id/home_fragment_bottom_sheet_icon").click()
    if not out:
        print("Success: opened bottom sheet")
    wait()
    
    print("Successful Replay!")

