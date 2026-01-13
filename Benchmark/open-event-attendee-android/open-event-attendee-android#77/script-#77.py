# bug reproduction script for bug #2198 of attendee
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

    out = d(resourceId="com.eventyay.attendee:id/searchFragment").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Anything").click()
    if not out:
        print("SUCCESS")
    wait()

    print("Successful Replay!")
