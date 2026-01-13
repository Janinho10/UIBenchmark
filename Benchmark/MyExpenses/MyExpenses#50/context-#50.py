import sys
import time
import uiautomator2 as u2
import subprocess

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "org.totschnig.myexpenses.debug"
    
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.WRITE_EXTERNAL_STORAGE", shell=True)
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.READ_EXTERNAL_STORAGE", shell=True)

    d.app_start("org.totschnig.myexpenses.debug")
    time.sleep(2)
    
    d(resourceId="org.totschnig.myexpenses.debug:id/suw_navbar_next").click()
    
    time.sleep(2)
    
    d(resourceId="org.totschnig.myexpenses.debug:id/suw_navbar_next").click()
    
    time.sleep(2)
    
    d(resourceId="org.totschnig.myexpenses.debug:id/suw_navbar_done").click()
    
    time.sleep(2)
