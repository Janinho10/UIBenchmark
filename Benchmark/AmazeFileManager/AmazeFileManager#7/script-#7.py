# bug reproduction script for bug #1232 of AFM
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

    out = d(text="gz.tar.gz").right(resourceId="com.amaze.filemanager:id/properties").click()
    if not out:
        print("Success: click properties of the .tar.gz file")
    wait()

    out = d(text="Extract").click()
    if not out:
        print("Success: click extract")
    wait()


    print("Successful Replay!")
