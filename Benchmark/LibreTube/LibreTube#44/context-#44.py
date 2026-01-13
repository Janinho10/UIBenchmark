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
    
    package_name = "com.github.libretube"
    
    requested_perms = get_requested_permissions(avd_serial, package_name)
    
     
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
     
    out = d(description="Search").click()
    if not out:
        print("Success: clicked on Search")
    time.sleep(1)

    out = d(text="Search apps, web and more").set_text("libretube")
    if not out:
        print("Success: set search term 'libretube'")
    time.sleep(1)

    out = d(resourceId="com.google.android.inputmethod.latin:id/key_pos_ime_action").click()
    if not out:
        print("Success: pressed 'enter'")
    time.sleep(1)

    out = d(text="LibreTube").click()
    if not out:
        print("Success: clicked on 'LibreTube'")
    time.sleep(1)
     
    if d(resourceId="com.android.chrome:id/terms_accept").exists:
        print("Clicking Chrome 'Accept & continue'...")
        d(resourceId="com.android.chrome:id/terms_accept").click()
    time.sleep(2) # Wait for animation

    if d(text="No thanks").exists:
        print("Clicking 'No thanks' for Sync...")
        d(text="No thanks").click()
    elif d(resourceId="com.android.chrome:id/negative_button").exists:
        d(resourceId="com.android.chrome:id/negative_button").click()

    time.sleep(1)
    d.app_stop("com.android.chrome")
    
    time.sleep(1)
    
    d.app_start("com.github.libretube")
    
    time.sleep(1)
    
    d(resourceId="com.github.libretube:id/radio_button").click()
    
    time.sleep(1)

    d(text="OK").click()
    
    time.sleep(1)
    
    d.press("home")
    
    time.sleep(1)
    
    d.press("back")
