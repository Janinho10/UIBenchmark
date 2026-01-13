import sys
import time
import uiautomator2 as u2
import subprocess


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    

    #Enable 'Don't keep activities'
    subprocess.run(
        ["adb", "-s", avd_serial, "shell", "settings", "put", "global", "always_finish_activities", "0"],
        check=True
    )

   
