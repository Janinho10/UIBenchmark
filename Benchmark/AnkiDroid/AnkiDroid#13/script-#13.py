# bug reproduction script for bug #4977 of ankidroid
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
    out = d(resourceId="com.ichi2.anki:id/fab_expand_menu_button").click()
    if not out:
        print("Success: press fab button")
    wait()

    out = d(resourceId="com.ichi2.anki:id/add_shared_action").click()
    if not out:
        print("Success: press add")
    wait(5)

    d.press("back")
    print("Success: press back")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press navigation")
    wait()

    out = d(text="Card browser").click()
    if not out:
        print("Success: Card browser")
    wait()

    print("Successful Replay!")
