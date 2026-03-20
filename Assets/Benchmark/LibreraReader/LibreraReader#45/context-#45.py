import os
import sys
import uiautomator2 as u2
import time
import subprocess

from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL_FOLDER = os.path.join(SCRIPT_DIR, "Librera-#45-PDFs")
DEVICE_FOLDER = "/sdcard/Download/temp_pdfs/"

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
    
    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "com.foobnix.pro.pdf.reader"
    
    requested_perms = get_requested_permissions(avd_serial, package_name)
    
     
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)

    wait()

    d.shell(f"mkdir -p {DEVICE_FOLDER}")

    for file in os.listdir(LOCAL_FOLDER):
        d.push(f"{LOCAL_FOLDER}/{file}", DEVICE_FOLDER)
        
    print("Success: pushed dummy entries to device")
    wait()
    
    d.app_start("com.android.vending")
    wait()
    
    out = d(text="Search").click()
    if not out:
        print("Success: clicked on Search")
    wait()
    
    out = d(textContains="Search apps & games").click()
    if not out:
        print("Success: clicked on Search bar")
    wait()
    
    out = d(focused=True).set_text("Librera Pro")
    if not out:
        print("Success: Set text to Librera Pro")
    wait()
    
    out = d.press("enter")
    if not out:
        print("Success: pressed enter")
    wait()
    
    out = d(descriptionContains="Librera PRO").click()
    if not out:
        print("Success: clicked on Librera PRO")
    wait()

    d.app_start("com.foobnix.pro.pdf.reader")
