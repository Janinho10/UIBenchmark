# bug reproduction script for bug #4200 of ankidroid
import sys
import time
import subprocess
import uiautomator2 as u2

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    d(text="OK").click()
       
    time.sleep(1)
       
    d(text="AnkiDroid").click()
        
    time.sleep(1)
       
    d(text="Default").click()
       
    time.sleep(1)
       
    d(description="More options").click()
       
    time.sleep(1)

    d(text="Delete note").click()
   
    time.sleep(1)
   
    d(text="Delete").click()
