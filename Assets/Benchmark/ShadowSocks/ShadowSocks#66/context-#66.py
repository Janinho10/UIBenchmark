# bug reproduction script for bug #285 of ActivityDiary
import sys
import time
import subprocess
import uiautomator2 as u2

def setup_watchers(d):
    """Registers watchers with the updated U2 v3+ syntax."""
    
    # 1. Register watchers using singular .watcher
    d.watcher("CHROME_WELCOME").when(d(text="Accept & continue")).click()
    d.watcher("CHROME_SYNC").when(d(text="No thanks")).click()
    d.watcher("ALLOW_NOTIFS").when(d(text="Allow")).click()

    def complex_accept_logic(ui_device):
        print("Agreement detected. Scrolling...")
        for _ in range(2):
            ui_device.swipe(0.5, 0.8, 0.5, 0.2)
            time.sleep(0.5)
        
        btn = ui_device(textMatches="(?i)Accept|Agree|OK|Continue|I Agree")
        if btn.exists:
            btn.click()
            print("Agreement accepted.")

    # 2. Correct syntax for the ToS handler
    d.watcher("TOS_HANDLER").when(d(textMatches="(?i)Terms|Privacy|Agreement")).call(complex_accept_logic)

    # 3. FIX: Start the background thread (U2 v3 syntax)
    # The 'interval' defines how often (seconds) it scans the screen
    d.watcher.start(interval=1.0)
    print("Watchers are now monitoring the screen...")

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

def set_clipboard_adb(serial, text):
    safe_text = text.replace("'", "'\\''")

    cmd = f"adb -s {serial} shell service call clipboard 2 s16 {safe_text}"
    subprocess.run(cmd, shell=True)

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    setup_watchers(d)
    
    package_name = "com.github.shadowsocks"
    
    requested_perms = get_requested_permissions(avd_serial, package_name)
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
        
    set_clipboard_adb("emulator-5554", "https://shadowmere.akiel.dev/api/sub/")
    
    d.app_start("com.android.chrome")
    wait(5)
    
    d(resourceId="com.android.chrome:id/search_box_text").click()
    wait()
    
    d.send_keys("https://shadowmere.akiel.dev/api/sub/", clear=True)
    wait()
    
    d(resourceId="com.android.chrome:id/url_bar").long_click()
    wait()
    
    d(text="Select all").click()
    wait()
    
    d(text="Copy").click()
    wait()
    
    d(description="Switch input method").click()
    wait()
    
    d(text="Gboard").click()
    wait()
    
    d(description="Clear input").click()
    
    d.app_start(package_name)
    wait()
    
    d.watcher.remove()
