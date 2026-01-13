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


    

    out = d(resourceId="de.danoeh.antennapod.debug:id/txtvTitle", index=1).click()
    if not out:
        print("Success: click an episode")
    wait()

    out = d(resourceId="de.danoeh.antennapod.debug:id/butAction1Text").click()
    if not out:
        print("Success: stream")
    wait()
    

    out = d(resourceId="de.danoeh.antennapod.debug:id/txtvTitle", index="0").click()
    if not out:
        print("Success: enter the playback interface")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: click more options")
    wait()

    out = d(text="Share…").click()
    if not out:
        print("Success: click Share")
    wait()

    out = d.press("home")
    if not out:
        print("Success: minimize the app")
    wait()


    print("Successful Replay!")
