import sys
import time
import subprocess
import uiautomator2 as u2

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
    
def drag_app_to_home(d, app_name, dest_x_ratio, dest_y_ratio):
    open_app_drawer(d)
    
    app_icon = d(text=app_name)
    
    width, height = d.window_size()
    dest_x = int(width * dest_x_ratio)
    dest_y = int(height * dest_y_ratio)
    
    app_icon.drag_to(dest_x, dest_y, duration=2.0)
    
    time.sleep(2)



if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    goodtime = "com.apps.adrcotfas.goodtime"
    
    requested_perms = get_requested_permissions(avd_serial, goodtime)
    
     
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {goodtime} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
        
    drag_app_to_home(d, "Goodtime", 0.7, 0.5)
    time.sleep(1)
    
    d.app_start(goodtime)
    time.sleep(1)
    d(description="Next").click()
    time.sleep(1)
    d(description="Next").click()
    time.sleep(1)
    d(description="Next").click()
    time.sleep(1)
    d(text="OK").click()
    time.sleep(1)
    d(text="OK").click()
    time.sleep(1)
    d(text="OK").click()
    time.sleep(1)
    
    d(text="OK").click()
    
    d.press("home")
