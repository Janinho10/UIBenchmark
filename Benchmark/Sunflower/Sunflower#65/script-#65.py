# bug reproduction script for bug #239 of sunflower
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
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Plant list").click()
    if not out:
        print("SUCCESS")
    wait()

    x1, y1 = d(text="Beet").center()
    x2, y2 = d(text="Avocado").center()
    
    out = d.click(x1, y1)
    if not out:
        print("SUCCESS: 1 Tap")
    time.sleep(0.02)
    out = d.click(x2, y2)
    if not out:
        print("SUCCESS: 2 TAP")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("SUCCESS: Go Back")
    wait()
  
    d(className="android.widget.FrameLayout").gesture(
    (x1, y1),
    (x2, y2),
    (x1, y1),
    (x2, y2),
    steps=5
)

    print("Successful Replay!")
