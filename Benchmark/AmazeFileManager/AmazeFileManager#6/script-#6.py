# bug reproduction script for bug #1887 of AFM
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
    d.app_start("com.amaze.filemanager.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
   
    wait()
    

    out = d(className="android.widget.TextView", text="Android").click()
    if not out:
        print("Success: press Android")
    wait()

    out = d(className="android.widget.TextView", text="data").click()
    if not out:
        print("Success: press data")
    wait()

    out = d(className="android.widget.TextView", resourceId="com.amaze.filemanager.debug:id/search").click()
    if not out:
        print("Success: press search")
    wait()

    out = d(className="android.widget.EditText", resourceId="com.amaze.filemanager.debug:id/search_edit_text").set_text(text="com")
    if out:
        print("Success: set folder name")
    wait()


    out = d(description="Search").click()
    if not out:
        print("Success: press data")
    wait()


    print("Successful Replay!")
