# bug reproduction script for bug #285 of ActivityDiary
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


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "com.celzero.bravedns"
    
    requested_perms = get_requested_permissions(avd_serial, package_name)
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
    wait()
    
    d.app_start(package_name)
    
    out = d(text="SKIP").click()
    if not out:
        print("Success: pressed SKIP")
    wait()
    
    print("Successful Context!")
