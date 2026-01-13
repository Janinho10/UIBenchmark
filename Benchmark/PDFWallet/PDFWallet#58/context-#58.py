# bug reproduction script for bug #285 of ActivityDiary
import sys
import time
import subprocess
import uiautomator2 as u2
import os

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

def force_media_scan(serial, filepath):
    """Refreshes Android's database so the file appears in apps immediately."""
    print(f"Scanning {filepath}...")
    subprocess.run(
        ["adb", "-s", serial, "shell", "am", "broadcast",
         "-a", "android.intent.action.MEDIA_SCANNER_SCAN_FILE",
         "-d", f"file://{filepath}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

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
        
        local_path = os.path.join(PRE_MADE_PDF_FOLDER, file)
        remote_path = os.path.join(DEVICE_FOLDER, file)
        
        d.push(local_path, remote_path)
        d.shell(f"touch {remote_path}")
        force_media_scan(avd_serial, remote_path)
    wait()
    
    
    out = d.open_quick_settings()
    if not out:
        print("Success: opened quick settings")
    wait()
    
    out = d(resourceId="android:id/edit").click()
    if not out:
        print("Success: clicked on edit")
    wait()
    
    out = d(scrollable=True).scroll.to(text="Dark Theme")
    if not out:
        print("Success: scrolled to Dark Theme")
    wait()
    
    w, h = d.window_size()
    d(text="Dark theme").drag_to(w // 2, int(h * 0.2), duration=1.0)
    
    out = d.press("home")
    wait(1)
    out = d.app_start(package_name)
    wait(3)
    
    out = d(text="ADD").click()
    if not out:
        print("Clicked on Add")
    wait()
        
    if not d(text="testdata").exists:
            
        if d(description="Show roots").exists:
                d(description="Show roots").click()
                wait(2)
                
        if d(text="Downloads").exists:
                d(text="Downloads").click()
                wait(2)
                
        if d(text="testdata").exists:
                d(text="testdata").click()
                wait(2)

        if d(textContains=".pdf").exists:
            d(textContains=".pdf").click()
            wait(2)
            
            if d(resourceId="com.michaeltroger.gruenerpass:id/deleteIcon").exists:
                d(resourceId="com.michaeltroger.gruenerpass:id/deleteIcon").click()
                wait(1)
                if d(text="OK").exists:
                    d(text="OK").click()
                    wait(1)

    # 5. Final Cleanup
    print("Context Complete. Closing app...")
    d.app_stop(package_name)
    d.press("home")
    
    out = d.app_start(package_name)
    
    print("Successful Context!")
