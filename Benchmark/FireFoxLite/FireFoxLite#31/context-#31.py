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
    
    package_name = "org.mozilla.rocket.debug.ting"
    activity_name = "org.mozilla.focus.activity.MainActivity"
    component = f"{package_name}/{activity_name}"
    
    
    requested_perms = get_requested_permissions(avd_serial, package_name)
    
     
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
        
    
    #Turn on Developer Settings
    subprocess.run(
        ["adb", "-s", avd_serial, "shell", "settings", "put", "global", "development_settings_enabled", "1"],
        check=True
    )
    #Enable 'Don't keep activities'
    subprocess.run(
        ["adb", "-s", avd_serial, "shell", "settings", "put", "global", "always_finish_activities", "1"],
        check=True
    )

    d.shell(f"am start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -n {component}")
    
    time.sleep(2)
    
    if d(textContains="OK").exists:
        d(text="OK").click()
        
        time.sleep(2)
        
        d.press("home")
        
        d.shell(f"am start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -n {component}")
        
        time.sleep(2)
        
        d.click(x=50, y=50)
    
        time.sleep(2)
    
    d.press("home")
    
    time.sleep(2)
        
    open_app_drawer(d)
