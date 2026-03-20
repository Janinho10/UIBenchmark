import sys
import time
import uiautomator2 as u2
import subprocess

if __name__ == '__main__':
    #TODO: Disable pop-ups, open contacts app in background, open app app overview
    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "com.amaze.filemanager.debug"
    
    contacts_package ="com.android.contacts"
    
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.WRITE_EXTERNAL_STORAGE", shell=True)
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.READ_EXTERNAL_STORAGE", shell=True)
    
    d.app_start(contacts_package, stop=True)
    
    time.sleep(1)
    
    d.press("home")
    
    time.sleep(1)
    
    d.swipe(0.5, 0.8, 0.5, 0.1)
