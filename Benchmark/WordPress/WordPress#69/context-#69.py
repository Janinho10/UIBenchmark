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
    
    
if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "org.wordpress.android"
    
    requested_perms = get_requested_permissions(avd_serial, package_name)
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
        
    #Enable developer options
    subprocess.run(
        ["adb", "-s", avd_serial, "shell", "settings", "put", "global", "development_settings_enabled", "0"],
        check=True
    )
    
    d.app_start("com.android.settings")
    time.sleep(1)
    
    d(scrollable=True).scroll.to(text="Developer options")
    time.sleep(1)
    
    d(text="Developer options").click()
    time.sleep(1)
    
    d(scrollable=True).scroll.to(text="Don't keep activities")
    time.sleep(1)
    
    d.app_start(package_name)
    
    time.sleep(1)
    
    d(className="android.widget.Button", resourceId="org.wordpress.android:id/login_button").click()
    time.sleep(1)
    
    d(resourceId="android:id/button1").click()
    time.sleep(1)
    
    d.press("back")
