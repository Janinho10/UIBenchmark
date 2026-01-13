import sys
import time
import uiautomator2 as u2
import subprocess

def open_app_drawer(d):
    d.press("home")
    time.sleep(1)
    
    width, height = d.window_size()
    d.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 0.1)
    time.sleep(2)

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "org.mozilla.focus"
    
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.WRITE_EXTERNAL_STORAGE", shell=True)
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.READ_EXTERNAL_STORAGE", shell=True)
        
    open_app_drawer(d)
