import sys
import time
import uiautomator2 as u2
import subprocess
import os
    
def force_media_scan(serial, filepath):
    subprocess.run(
        ["adb", "-s", serial, "shell", "am", "broadcast",
         "-a", "android.intent.action.MEDIA_SCANNER_SCAN_FILE",
         "-d", f"file://{filepath}"],

        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
def prime_file_picker_location(d, serial, device_path):
    

    folder_path = os.path.dirname(device_path)
    internal_path = folder_path.replace("/sdcard/", "").replace("/", "%2F")
    
    document_uri = f"content://com.android.externalstorage.documents/document/primary%3A{internal_path}"
    
    print(f"Priming: Navigating system to {folder_path}...")
    
    subprocess.run([
        "adb", "-s", serial, "shell", "am", "start",
        "-a", "android.intent.action.VIEW",
        "-d", document_uri
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    time.sleep(3)
    
    d.app_stop("com.google.android.documentsui")
    d.app_stop("com.android.documentsui")
    d.press("home")
    time.sleep(1)
    
if __name__ == '__main__':
    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    yml_file = "clash.meta.yml"
    DEVICE_FOLDER = "/sdcard/Download/Clash"
 
    d.shell(f"mkdir -p {DEVICE_FOLDER}")
    time.sleep(1)
    local_path = os.path.join(SCRIPT_DIR, yml_file)
    remote_path = os.path.join(DEVICE_FOLDER, yml_file)
    
    d.push(local_path, remote_path)
    d.shell(f"touch {remote_path}")
    force_media_scan(avd_serial, remote_path)
    
    prime_file_picker_location(d, avd_serial, remote_path)
    
    time.sleep(1)
    
    d.app_start("com.github.metacubex.clash.meta")
