# bug reproduction script for bug #1145 of GPSTest
import os
import sys
import time

import uiautomator2 as u2



if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)

    d.app_start("com.android.gpstest")

    current_app = d.app_current()
    print(current_app)
    
    
