import sys
import time
import uiautomator2 as u2
import subprocess

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

def open_app_drawer(d):
    d.press("home")
    time.sleep(1)
    
    width, height = d.window_size()
    d.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 0.1)
    time.sleep(2)

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "com.benny.openlauncher"
    
    requested_perms = get_requested_permissions(avd_serial, package_name)
     
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
        
    open_app_drawer(d)
