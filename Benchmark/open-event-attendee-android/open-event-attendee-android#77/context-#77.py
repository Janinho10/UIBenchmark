import sys
import time
import uiautomator2 as u2
import subprocess

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "com.eventyay.attendee"
    
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.WRITE_EXTERNAL_STORAGE", shell=True)
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.READ_EXTERNAL_STORAGE", shell=True)
    
    d.watcher("permission_watcher").when("//*[@resource-id='com.eventyay.attendee:id/skipTextView']").click()
    d.watcher.start()
    
    d.shell(f"am start -W -n com.eventyay.attendee/org.fossasia.openevent.general.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER")
    
    time.sleep(2)
    
    d(text="PICK A CITY").click()
    time.sleep(2)

    d(text="Enter location").set_text("Delhi")
    time.sleep(5)
    
    d(resourceId="com.eventyay.attendee:id/placeName", text="Delhi").click()
    time.sleep(2)
    
    
