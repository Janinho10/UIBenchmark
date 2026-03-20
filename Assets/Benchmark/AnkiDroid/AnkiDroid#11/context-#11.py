# bug reproduction script for bug #4200 of ankidroid
import sys
import time
import subprocess
import uiautomator2 as u2


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    #Enable developer options
        
    d.press("home")
    time.sleep(1)
    d(description="Apps").click()
