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
    
    out = d(text="openScale").click()
    if not out:
        print("Success: opened openScale")
    wait()
    
    out = d(text="Enter your name").set_text("name ")
    if not out:
        print("Success: Entered name into name")
    wait()
    
    out = d(text="Enter value in cm").click()
    if not out:
        print("Success: clicked on Height")
    wait()
    
    out = d(text="Enter value in cm").set_text(57)
    if not out:
        print("Success: set text to 57")
    wait()
    
    out = d(resourceId="com.health.openscale:id/txtBirthday").click()
    if not out:
        print("Success: clicked on Birthday")
    wait()
    
    out = d.set_orientation("left")
    if not out:
        print("Success: changed screen orientation(left)")
    wait()
    
    out = d.set_orientation("natural")
    if not out:
        print("Success: changed screen orientation(natural)")
    wait()
    
    out = d(resourceId="com.health.openscale:id/txtBirthday").click()
    if not out:
        print("Success: clicked on Birthday")
    wait()
    
    out = d.set_orientation("left")
    if not out:
        print("Success: changed screen orientation(left)")
    wait()
    
    out = d.set_orientation("natural")
    if not out:
        print("Success: changed screen orientation(natural)")
    wait()
    
    print("Successful Replay!")
