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

    d.app_start("com.zionhuang.music")
    wait()


    d(scrollable=True).scroll.horiz.toEnd()
    wait()

    d.press("Home")
    wait()

    