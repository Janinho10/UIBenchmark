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

    out = d(resourceId="org.oxycblt.auxio:id/playback_song").click()
    if not out:
        print("Success: clicked on playback song")
    wait()

    out = d(className="android.widget.SeekBar").drag_to(200, 100)
    if not out:
        print("Success: dragged slider")
    wait()

    out = d(resourceId="org.oxycblt.auxio:id/playback_more").click()
    if not out:
        print("Success: clicked song menu")
    wait()

    out = d(text="Add to playlist").click()
    if not out:
        print("Success: clicked on add to playlist")
    wait()

    out = d(text="Cancel")
    if not out:
        print("Success: clicked on Cancel")
    wait()

    out = d(className="android.widget.ImageButton").click()
    if not out:
        print("Success: closed Song")
    wait()

    out = d().swipe(direction="left")
    if not out:
        print("Success: swiped left")
    wait()

    out = d().swipe(direction="left")
    if not out:
        print("Success: swiped left")
    wait()

    out = d().swipe(direction="left")
    if not out:
        print("Success: swiped left")
    wait()

    out = d().swipe(direction="left")
    if not out:
        print("Success: swiped left")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: clicked on description")
    wait()

    out = d(text="Settings").click()
    if not out:
        print("Success: clicked on Settings")
    wait()

    out = d(text="Look and Feel").click()
    if not out:
        print("Success: clicked on 'Look and Feel'")
    wait()

    out = d(text="Theme").click()
    if not out:
        print("Success: clicked on Theme")
    wait()

    out = d(text="Dark").click()
    if not out:
        print("Success: clicked on Dark")
    wait()

    out = d.swipe(fx=0, fy=500, tx=100, ty=500, steps=1)
    if not out:
        print("Success: Gesture back")
    wait()

    out = d.swipe(fx=0, fy=500, tx=100, ty=500, steps=1)
    if not out:
        print("Success: Gesture back")
    wait()

    out = d(resourceId="org.oxycblt.auxio:id/playback_song").click()
    if not out:
        print("Success: clicked on playback song")
    wait()    

