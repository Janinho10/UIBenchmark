import sys
import time
import uiautomator2 as u2
import subprocess

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "com.ichi2.anki"
    
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.WRITE_EXTERNAL_STORAGE", shell=True)
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.READ_EXTERNAL_STORAGE", shell=True)

    d.app_start("com.ichi2.anki")
