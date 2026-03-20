# bug reproduction script for bug #224 of MaterialFBook
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

    x, y = d(className="android.webkit.WebView").center()
    d.long_click(x, y, duration=1)
    print("Success: long click web page")
    wait()


    print("Successful Replay!")
