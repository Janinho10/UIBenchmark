import sys
import time
import uiautomator2 as u2
import subprocess
import os
    
    
if __name__ == '__main__':
    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    DEVICE_FOLDER = "/sdcard/Download/Clash"
 
    d.shell(f"rm -rf {DEVICE_FOLDER}")
