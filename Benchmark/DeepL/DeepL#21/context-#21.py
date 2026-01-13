# bug reproduction script for bug #285 of ActivityDiary
import sys
import time

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    """
    d.app_start("com.google.android.googlequicksearchbox")
    wait()

    current_app = d.app_current()
    print(current_app)
    wait()
    
    out = d(text="Search").click()
    wait()
    
    out = d(text="Search…").set_text("DeepL")
    wait()
    
    out = d(resourceId="com.google.android.inputmethod.latin:id/key_pos_ime_action").click()
    wait()
    """
    d.shell('am start -a android.intent.action.WEB_SEARCH -e query "DeepL"')
    wait()
    
    out = d(text="DeepL Translate").click()
    wait()
    
    
    out = d(text="Accept & continue").click()
    wait()
    
    out = d(text="No thanks").click()
    
