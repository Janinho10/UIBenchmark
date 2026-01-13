# bug reproduction script for bug #729 of osmeditor
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
    

    out = d(resourceId="android:id/button1").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="de.blau.android:id/location_current").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="de.blau.android:id/location_button_current").click()
    if not out:
        print("SUCCESS")
    wait(10)

    out = d(resourceId="de.blau.android:id/map_view").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="de.blau.android:id/floatingLock").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="de.blau.android:id/map_view").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="android:id/select_dialog_listview").child(textContains="Footway").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="de.blau.android:id/cab_stub").child(index="0").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Presets").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Preset search string").set_text("search")
    if out:
        print("SUCCESS")
    wait()

    out = d(className="android.widget.EditText", text="search").click(offset=(0.95, 0.5))
    if not out:
        print("SUCCESS")
    wait()

    print("Successful Replay!")
