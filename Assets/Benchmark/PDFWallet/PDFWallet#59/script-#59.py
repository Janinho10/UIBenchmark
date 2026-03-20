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
    
    #d.service("uiautomator").stop()
    #wait(3)
    
    out = d(description="Add").click()
    if not out:
        print("Success: clicked on Add")
    wait()
    
    out = d(text="demo_pdf.pdf").click()
    if not out:
        print("Success: clicked on demo_pdf")
    wait()
    
    out = d(description="Add").click()
    if not out:
        print("Success: clicked on Add")
    wait()
    
    out = d(text="another_demo_pdf.pdf").click()
    if not out:
        print("Success: clicked on another_demo_pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.backward()
    if not out:
        print("Success: scrolld to first pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolld to second pdf")
    wait()
    
    out = d(description="Add").click()
    if not out:
        print("Success: clicked on Add")
    wait()
    
    out = d(text="demo_certificate_en.pdf").click()
    if not out:
        print("Success: clicked on demo_certificate_en.pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.backward()
    if not out:
        print("Success: scrolld to first pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.backward()
    if not out:
        print("Success: scrolld to first pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolld to second pdf")
    wait()
    
    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolld to third pdf")
    wait()
    
    out = d(resourceId="com.michaeltroger.gruenerpass:id/handle", instance=1).drag_to(0, 0, duration=1.5)
    if not out:
        print("Success: drag to the front")
    wait()
    
    out = d(resourceId="com.michaeltroger.gruenerpass:id/name").click()
    if not out:
        print("Success: clicked on Name")
    wait()
    
    out = d(focused=True).set_text("My certificate")
    if not out:
        print("Success: set text to My certificate")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolld to second pdf")
    wait()
    
    out = d(resourceId="com.michaeltroger.gruenerpass:id/name").click()
    if not out:
        print("Success: clicked on Name")
    wait()
    
    out = d(focused=True).set_text("manual")
    if not out:
        print("Success: set text to manual")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolld to third pdf")
    wait()
    
    out = d(resourceId="com.michaeltroger.gruenerpass:id/name").click()
    if not out:
        print("Success: clicked on Name")
    wait()
    
    out = d(focused=True).set_text("Bus ticket")
    if not out:
        print("Success: set text to Bus ticket")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d(resourceId="com.michaeltroger.gruenerpass:id/deleteIcon").click()
    if not out:
        print("Success: clicked on delete")
    wait()
    
    out = d(text="OK").click()
    if not out:
        print("Success: clicked on OK")
    wait()
    
    out = d(scrollable=True).scroll.horiz.backward()
    if not out:
        print("Success: scrolld to second pdf")
    wait()
    
    print("Successful Replay!")
