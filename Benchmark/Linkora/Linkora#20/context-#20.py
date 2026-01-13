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
 

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    droidify_name = "com.looker.droidify"
    linkora_name = "com.sakethh.linkora"
    
    requested_perms = get_requested_permissions(avd_serial, droidify_name)
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {droidify_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
        
    requested_perms = get_requested_permissions(avd_serial, linkora_name)
     
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {linkora_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
        
    d.app_start(droidify_name)
    time.sleep(15)
    
    d(description="Search").click()
    time.sleep(2)
    
    d(focused=True).set_text("Linkora")
    time.sleep(2)
    
    d(resourceId="com.looker.droidify:id/name").click()

    time.sleep(2)
    
    d(text="Ignore this version").click()
    
