import sys
import time
import subprocess
import uiautomator2 as u2
import os

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

def get_requested_permissions(serial, package):
    cmd = f"adb -s {serial} shell dumpsys package {package}"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    permissions = []
    parsing = False
    
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("requested permissions:"):
            parsing = True
            continue
        if parsing:
            if line.startswith("android.permission."):
                perm = line.split(":")[0]
                permissions.append(perm)
            elif line == "" or line.startswith("install permissions:") or line.endswith(":"):
                break
    
    return permissions

def add_app_icon_to_home(d, app_label="aFreeRDP"):
    # go to home screen
    d.press("home")
    time.sleep(1)

    # open app drawer (common gesture on many launchers)
    d.swipe(0.5, 0.9, 0.5, 0.1, 0.2)
    time.sleep(1)

    icon = d(text=app_label)
    if not icon.exists:
        print(f"Could not find app icon '{app_label}' in app drawer")
        return

    w, h = d.window_size()
    icon.drag_to(w * 0.6, h * 0.3)
    time.sleep(0.5)

    # confirm by going home
    d.press("home")
    print(f"Added '{app_label}' to home screen.")

if __name__ == '__main__':
    avd_serial = "emulator-5554"
    d = u2.connect(avd_serial)

    package_name = "com.forrestguice.suntimeswidget"
    
    requested_perms = get_requested_permissions(avd_serial, package_name)
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
    wait()

    add_app_icon_to_home(d, app_label="Suntimes")

    