# bug reproduction script for bug #285 of ActivityDiary
import sys
import time
import subprocess
import uiautomator2 as u2

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

def scroll_to_country(d, country_name):
    max_attempts = 20
    for _ in range(max_attempts):
        if d(textContains=country_name).exists:
            d(textContains=country_name).click()
            return True
        

        w, h = d.window_size()
        d.swipe(w * 0.5, h * 0.8, w * 0.5, h * 0.2, duration=0.2)
        time.sleep(1)
    

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    w, h = d.window_size()

    
    out = d(className="android.widget.ImageButton").click()
    if not out:
        print("Success: clicked on shadowsocks")
    wait()
    
    out = d(text="Subscriptions").click()
    if not out:
        print("Success: clicked on Subscriptions")
    wait()
    
    out = d(description="Add a subscription").click()
    if not out:
        print("Success: clicked on added a subscription")
    wait()
    
    out = d(resourceId="com.github.shadowsocks:id/content").click()
    if not out:
        print("Success: clicked on Edit content")
    wait()
    
    out = d(description="https://shadowmere.akiel.dev/api/sub/").click()
    if not out:
        print("Success: Pasted link")
    wait()
    
    out = d(text="OK").click()
    if not out:
        print("Success: click OK")
    wait()
    
    out = d(description="Refresh servers from subscription").click()
    if not out:
        print("Success: refreshed subscriptions")
    wait()
    
    out = d(className="android.widget.ImageButton").click()
    if not out:
        print("Success: clicked on shadowsocks")
    wait()
    
    out = d(text="Profiles").click()
    if not out:
        print("Success: clicked on Profiles")
    wait()
    
    out = scroll_to_country(d, "United Kingdom")
    if not out:
        print("Success: Scrolled to United Kingdom")
    wait()
    
    out = d(textContains="United Kingdom").click()
    if not out:
        print("Success: clicked on United Kingdom")
    wait()
    
    out = d(description="Connect").click()
    if not out:
        print("Success: clicked on connect")
    wait()
    
    out = d(text="Connected, tap to check connection").click()
    if not out:
        print("Success: checked connection")
    wait()
    
    out = d.swipe(w * 0.5, h * 0.99, w * 0.5, h * 0.5, duration=0.1)
    if not out:
        print("Success: homescreen via gesture")
    wait()
    
    out = d.app_start("com.android.chrome")
    if not out:
        print("Success: start chrome")
    wait()
    
    out = d(focused=True).set_text("wtfismyip.com")
    if not out:
        print("Success: set text to wtfismyip.com")
    wait()
    
    out = d.press("enter")
    if not out:
        print("Success: prssed enter")
    wait()
    
    out = d.swipe(w * 0.2, h * 0.99, w * 0.8, h * 0.99, duration=0.1)
    if not out:
        print("Success: went back to previous")
    wait()
    
    out = d.open_notification()
    if not out:
        print("Success: opened notifications")
