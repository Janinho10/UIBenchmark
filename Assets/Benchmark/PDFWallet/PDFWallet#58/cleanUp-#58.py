import sys
import subprocess
import uiautomator2 as u2
import time

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    
    d = u2.connect(avd_serial)

    package_name = "com.michaeltroger.gruenerpass"
    DEVICE_FOLDER = "/sdcard/Download/testdata/"

    
    subprocess.run(f"adb -s {avd_serial} shell rm -rf {DEVICE_FOLDER}", shell=True)
    d.open_quick_settings()
    wait()
    
    # Click edit button (pencil icon)
    if d(resourceId="android:id/edit").exists:
        d(resourceId="android:id/edit").click()
        wait()
        if d(text="Dark theme").exists:             
             width, height = d.window_size()
             # Drag from tile center to bottom center
             d(text="Dark theme").drag_to(width // 2, height - 100, duration=1.0)
             print("Removed Dark theme tile.")
             wait()
        
        # Go back to save changes
        d.press("back")
        wait()
        
    d.press("home")
