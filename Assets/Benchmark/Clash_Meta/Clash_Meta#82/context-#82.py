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

if __name__ == '__main__':
    avd_serial = "emulator-5554"
    d = u2.connect(avd_serial)

    package_name = "com.github.metacubex.clash.meta"
    
    requested_perms = get_requested_permissions(avd_serial, package_name)
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)

    local_folder = os.path.join(os.path.dirname(__file__), 'clash_for_android-main')
    local_file = os.path.join(os.path.dirname(__file__), 'configuration.yaml')
    remote_folder = '/storage/emulated/0/clash_for_android-main'
    remote_file = '/storage/emulated/0/configuration.yaml'
    
    # Push folder using adb
    result_folder = subprocess.run(['adb', '-s', avd_serial, 'push', local_folder, remote_folder], capture_output=True, text=True)
    if result_folder.returncode == 0:
        print("Successfully pushed clash_for_android-main folder to emulator.")
    else:
        print("Failed to push folder:", result_folder.stderr)
    
    # Push file using adb
    result_file = subprocess.run(['adb', '-s', avd_serial, 'push', local_file, remote_file], capture_output=True, text=True)
    if result_file.returncode == 0:
        print("Successfully pushed configuration.yaml to emulator.")
    else:
        print("Failed to push file:", result_file.stderr)
        
    d.app_start("com.github.metacubex.clash.meta")
    wait()

    d(text="Profile").click()
    wait()

    d(resourceId="com.github.metacubex.clash.meta:id/add_view").click()
    wait()

    d(text="File").click()
    wait()

    d(text="Name").click()
    wait()

    d(resourceId="com.github.metacubex.clash.meta:id/text_field").set_text("clash for android")
    wait()

    d(text="OK").click()
    wait()

    d(text="Browse Files").click()
    wait()

    d(resourceId="com.github.kr328.clash:id/menu_view").click()
    wait()

    d(text="Import").click()
    wait()

    d(description="Show roots").click()
    wait()

    d(textContains="sdk").click()
    wait()

    d(text="configuration.yaml").click()
    wait()

    d.press("back")

