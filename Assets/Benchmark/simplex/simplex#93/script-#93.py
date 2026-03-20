import sys
import time
import subprocess
import uiautomator2 as u2

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

    if __name__ == '__main__':
        avd_serial = sys.argv[1]
        d = u2.connect(avd_serial)

        out = d(text="SimpleX").click()
        if not out:
            print("Success: clicked SimpleX icon")
        wait()

        out = d(description="profile image placeholder")[1].click()
        if not out:
            print("Success: opened settings")
        wait()

        out = d(scrollable=True).scroll.toEnd()
        if not out:
            print("Success: scrolled to the End")
        wait()

        out = d(scrollable=True).scroll.toBeginning()
        if not out:
            print("Success: scrolled to the Beginning")
        wait()

        out = d(text="Your chat profiles").click()
        if not out:
            print("Success: clicked on Your chat profiles")
        wait()

        out = d.swipe(fx=0, fy=500, tx=100, ty=500, steps=1)
        if not out:
            print("Success: Gesture back")
        wait()

        out = d(text="Chat preferences").click()
        if not out:
            print("Success: clicked on Chat preferences")
        wait()

        out = d(scrollable=True).scroll.toEnd()
        if not out:
            print("Success: scrolled to the End")
        wait()

        out = d.swipe(fx=0, fy=500, tx=100, ty=500, steps=1)
        if not out:
            print("Success: Gesture back")
        wait()