# bug reproduction script for bug #285 of ActivityDiary
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
    
    
    out = d(scrollable=True).scroll.forward(direction="vertical")
    if not out:
        print("Success: Scrolled up")
    wait()
    
    out = d(text="Bluetooth LE Spam").click()
    if not out:
        print("Success: opened Bluetooth LE Spam")
    wait()
    
    
    out = d(text="Fast Pair").click()
    if not out:
        print("Success: clicked on Fast Pair")
    wait()
    
    out = d(resourceId="de.simon.dankelmann.bluetoothlespam:id/advertisementFragmentPlayButton").click()
    if not out:
        print("Success: clicked on Play button")
    wait()
    
    out = d(text="Fast Pairing Device List").click()
    if not out:
        print("Success: Clicked on fast pairing device list")
    wait()
    
    for i in range(5):
        d(scrollable=True).scroll.forward(direction="vertical")
    wait()
    print("Successful Replay!")
