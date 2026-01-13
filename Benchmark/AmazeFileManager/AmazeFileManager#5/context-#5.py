import sys
import time
import uiautomator2 as u2
import subprocess

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "com.amaze.filemanager.debug"
    
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.WRITE_EXTERNAL_STORAGE", shell=True)
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.READ_EXTERNAL_STORAGE", shell=True)
    
    time.sleep(1)
    
    d.press("home")
    
    time.sleep(1)

    d(description="Apps list").click()
