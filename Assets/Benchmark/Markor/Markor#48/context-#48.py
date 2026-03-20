import sys
import time
import uiautomator2 as u2
import subprocess

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "net.gsantner.markor"
    
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.WRITE_EXTERNAL_STORAGE", shell=True)
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.READ_EXTERNAL_STORAGE", shell=True)
    
    d.watcher("permission_watcher").when("//*[@text='Allow']").click()
    d.watcher.start()
    
    d.app_start(package_name)
    
    d.app_start("net.gsantner.markor")
    time.sleep(2)

    d(resourceId="net.gsantner.markor:id/next").click()
    time.sleep(2)
    
    d(resourceId="net.gsantner.markor:id/next").click()
    time.sleep(2)
    
    d(resourceId="net.gsantner.markor:id/next").click()
    time.sleep(2)
    
    d(resourceId="net.gsantner.markor:id/next").click()
    time.sleep(2)
    
    d(resourceId="net.gsantner.markor:id/next").click()
    time.sleep(2)
    
    d(text="DONE").click()
    time.sleep(2)
