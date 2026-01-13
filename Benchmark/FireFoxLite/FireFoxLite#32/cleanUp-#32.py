import sys
import time
import uiautomator2 as u2
import subprocess

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    
    #Turn off Developer Settings
    #subprocess.run(
    #    ["adb", "-s", avd_serial, "shell", "settings", "put", "global", "development_settings_enabled", "0"],
    #    check=True
    #)
    #Disable 'Don't keep activities'
    subprocess.run(
        ["adb", "-s", avd_serial, "shell", "settings", "put", "global", "always_finish_activities", "0"],
        check=True
    )
