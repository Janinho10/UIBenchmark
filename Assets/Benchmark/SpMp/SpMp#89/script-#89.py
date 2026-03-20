import sys
import time
import subprocess
import uiautomator2 as u2
import os

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

if __name__ == '__main__':
    avd_serial = "emulator-5554"
    d = u2.connect(avd_serial)

    out = d.swipe_ext("up")
    if not out:
        print("Success: swiped up")
    wait()

    out = d(text="Neo Store").click()
    if not out:
        print("Success: clicked on Neo Store")
    wait()

    out = d(text="SpMp").click()
    if not out:
        print("Success: clicked on SpMp")
    wait()

    w, h = d.window_size()

    out = d.swipe(w // 2, int(h * 0.99), w // 2, int(h * 0.2), 0.2)
    if not out:
        print("Success: swiped up")
    wait()

    out = d.swipe_ext("up")
    if not out:
        print("Success: swiped up")
    wait()

    out = d(text="SpMp").click()
    if not out:
        print("Success: clicked on SpMp")
    wait(10)

    out = d.swipe_ext("up")
    if not out:
        print("Success: swiped down")
    wait()

    out = d.swipe(fx=500, fy=400, tx=500, ty=1800, duration=0.5)
    if not out:
        print("Success: scrolled to beginning")
    wait()

    out = d.swipe_ext("up")
    if not out:
        print("Success: swiped down")
    wait()

    out = d(className="android.view.View", index=0).click()
    if not out:
        print("Success: clicked on Playlist")
    wait()

    out = d(className="android.view.View", index=11).click()
    if not out:
        print("Success: clicked on Song")
    wait()

    out = d(className="android.widget.Button", index=14).click()
    if not out:
        print("Success: clicked on more options")
    wait()

    out = d(text="Download").click()
    if not out:
        print("Success: clicked on Download")
    wait()

    out = d(text="Download").click()
    if not out:
        print("Success: clicked on Download")
    wait()

    out = d.swipe(fx=500, fy=400, tx=500, ty=1800, duration=0.5)
    if not out:
        print("Success: swiped down")
    wait()

    out = d.swipe(fx=0, fy=500, tx=100, ty=500, steps=1)
    if not out:
        print("Success: Gesture back")
    wait()

    out = d(className="android.widget.Button", index=2).click()
    if not out:
        print("Success: clicked on button")
    wait()

    out = d(className="android.widget.Button", index=1).click()
    if not out:
        print("Success: clicked on Songs")
    wait()
