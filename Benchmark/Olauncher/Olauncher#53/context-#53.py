import sys
import time
import subprocess

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "app.olauncher"
    
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.WRITE_EXTERNAL_STORAGE", shell=True)
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.READ_EXTERNAL_STORAGE", shell=True)
    
    d.app_start("app.olauncher")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "app.olauncher":
            break
        time.sleep(2)
    wait()
    
    out = d(resourceId="app.olauncher:id/homeApp4").long_click(1)
    if not out:
        print("Success: clicked on fourth app")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    text = "Play Store"

    while True:
        if d(text=text).exists:
            print("Success: scrolled to Play Store")
            break
        d(scrollable=True).scroll.forward(direction="vertical")
    
    out = d(text="Play Store").click()
    if not out:
        print("Success: clicked on Play Store")
    wait()
    
    d.press("power")
    
    wait()
    
    print("Successful Replay!")
