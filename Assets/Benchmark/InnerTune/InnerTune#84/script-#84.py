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

    out = d(description="Search").click()
    if not out:
        print("Success: opened Google")
    wait()

    out = d(resourceId="com.google.android.apps.nexuslauncher:id/input").set_text("fdroid")
    if not out:
        print("set text to fdroid")
    wait()

    out = d.press("Enter")
    if not out:
        print("Success: pressed enter")
    wait()

    out = d(text="F-Droid").click()
    if not out:
        print("Success: clicked on F-Droid")
    wait()

    out = d(scrollable=True).scroll.to(text="Find Apps")
    if not out:
        print("Success: scrolled to Search")
    wait()

    out = d(className="android.widget.EditText").click()
    if not out:
        print("Success: clicked on Text Input")
    wait()

    out = d(focused=True).set_text("Innertune")
    if not out:
        print("Success: set text to Innertune")
    wait()

    out = d.press("Enter")
    if not out:
        print("Success: pushed Enter")
    wait()

    out = d(text="InnerTune").click()
    if not out:
        print("Success: clicked on InnerTune")
    wait()

    for _ in range(15):
        if d(textContains="com.zionhuang.music").exists:
            print("Success: scrolled to APK")
            break
        wait()
        d.swipe_ext("up", scale=0.8)
    wait()

    out = d.press("Home")
    if not out:
        print("Success: pressed Home button")
    wait()

    out = d(scrollable=True).swipe("up")
    if not out:
        print("swiped up")
    wait()

    out = d(text="Inner Tune").click()
    if not out:
        print("Success: clicked on Inner Tune")
    wait()

    out = d(scrollable=True).scroll.horiz.toBeginning()
    if not out:
        print("Success: swiped to beginning")
    wait()

    out = d(className="android.view.View", index=1).click()
    if not out:
        print("Success: clicked on Playlist")
    wait()

    out = d(scrollable=True).scroll.vert.forward()
    if not out:
        print("Success: scrolled down")
    wait()

    out = d(scrollable=True).scroll.vert.backward()
    if not out:
        print("Success: scrolled up")
    wait()

    out = d.swipe(fx=0, fy=500, tx=100, ty=500, steps=1)
    if not out:
        print("Success: Gesture Back")
    wait()

    out = d.xpath('//android.widget.EditText/following-sibling::*[1]').click()
    if not out:
        print("Success: clicked on Settings")
    wait()

    out = d(text="Player and audio").click()
    if not out:
        print("Success: clicked on 'Player and audio'")
    wait()

    out = d.swipe(fx=0, fy=500, tx=100, ty=500, steps=1)
    if not out:
        print("Success: Gesture Back")
    wait()