import sys
import time
import uiautomator2 as u2
import subprocess

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "de.danoeh.antennapod.debug"
    
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.WRITE_EXTERNAL_STORAGE", shell=True)
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.READ_EXTERNAL_STORAGE", shell=True)
    
    d.app_start(package_name, stop=True)
    time.sleep(3)
    
    d(resourceId="de.danoeh.antennapod.debug:id/nav_list").child_by_text(
        "Add Podcast",
        resourceId="de.danoeh.antennapod.debug:id/txtvTitle"
    ).click()
    time.sleep(2)

    d(description="Crime Junkie - Audiochuck").click()
    time.sleep(2)
    
    d(text="Subscribe").click()
    time.sleep(2)
    
    
    d(resourceId="de.danoeh.antennapod.debug:id/txtvTitle", index=1).click()
    time.sleep(2)

    d(resourceId="de.danoeh.antennapod.debug:id/butAction1Text").click()
    time.sleep(2)
    
    d(text="Always").click()
    time.sleep(2)
    
    d.press("back")
    time.sleep(2)
    
    d(description="Pause").click()
    time.sleep(2)
