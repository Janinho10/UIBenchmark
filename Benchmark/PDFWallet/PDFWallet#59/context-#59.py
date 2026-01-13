# bug reproduction script for bug #285 of ActivityDiary
import sys
import time
import subprocess
import os

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
    package_name = "com.michaeltroger.gruenerpass"
    
    
    requested_perms = get_requested_permissions(avd_serial, package_name)
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
    
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PRE_MADE_PDF_FOLDER = os.path.join(SCRIPT_DIR, "PDFWallet-PDFs")
    DEVICE_FOLDER = "/sdcard/Download/testdata/"

    d.shell(f"mkdir -p {DEVICE_FOLDER}")
    for file in os.listdir(PRE_MADE_PDF_FOLDER):
        d.push(f"{PRE_MADE_PDF_FOLDER}/{file}", DEVICE_FOLDER)
    wait()
    
    out = d.app_start("com.michaeltroger.gruenerpass")
    wait()
    
    d(description="Add").click()
    wait()
    
    d(description="Show roots").click()
    wait()
    
    d(text="Downloads").click()
    wait()
    
    d(text="testdata").click()
    wait()
    
    if d(description="List view").exists:
        d(resourceId="com.android.documentsui:id/sub_menu").click()
        wait()
    
    out = d(text="demo_pdf.pdf").click()
    if not out:
        print("Success: clicked on demo_pdf")
    wait()
    
    out = d(resourceId="com.michaeltroger.gruenerpass:id/deleteIcon").click()
    if not out:
        print("Success: clicked on delete")
    wait()
    
    out = d(text="OK").click()
    
    print("Successful Context!")
