import sys
import time
import uiautomator2 as u2
import subprocess

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "de.rampro.activitydiary.debug"
    
    
    d.press("home")
    time.sleep(1)

    d(description="Apps").click()
