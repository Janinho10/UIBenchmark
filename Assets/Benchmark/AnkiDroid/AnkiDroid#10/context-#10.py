# context script for Bug #10 of ankidroid
import sys
import time
import subprocess
import uiautomator2 as u2


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    #Enable developer options
    print("Opening Settings...")
    d.app_start("com.android.settings")
    time.sleep(2)
    d(scrollable=True).scroll.toEnd()

    if d(text="About phone").exists:
        d(text="About phone").click()
    elif d(text="About emulated device").exists:
        d(text="About emulated device").click()
    else:
        print("Warning: Could not find 'About phone' directly.")
        
    time.sleep(1)

    d(scrollable=True).scroll.toEnd()

    build_num = d(text="Build number")
    if build_num.exists:
        for _ in range(7):
            build_num.click()
            time.sleep(0.1)
    else:
        print("Error: Could not find 'Build number'!")

    # Disable 'Don't keep activities' to be turned on in script#10
    subprocess.run(
            ["adb", "-s", avd_serial, "shell", "settings", "put", "global", "always_finish_activities", "0"],
            check=True
        )
        
    d.press("home")
    time.sleep(1)
    d(description="Apps").click()
