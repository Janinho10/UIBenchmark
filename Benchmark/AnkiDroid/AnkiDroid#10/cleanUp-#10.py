# bug reproduction script for bug #4200 of ankidroid
import sys
import time
import subprocess
import uiautomator2 as u2

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    #Turn off developer options
    #subprocess.run(
    #        ["adb", "-s", avd_serial, "shell", "settings", "put", "global", "development_settings_enabled", "0"],
    #        check=True
    #    )
    #Disable 'Don't keep activities'
    subprocess.run(
            ["adb", "-s", avd_serial, "shell", "settings", "put", "global", "always_finish_activities", "0"],
            check=True
        )
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
