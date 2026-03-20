# bug reproduction script for bug #1232 of AFM
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
    wait()

    out = d(className="android.widget.TextView", resourceId="com.amaze.filemanager:id/search").click()
    if not out:
        print("Success: click search")
    wait()

    out = d(className="android.widget.EditText", resourceId="com.amaze.filemanager:id/search_edit_text").set_text(text="data")
    if out:
        print("Success: input data")
    wait()

    out = d(className="com.android.inputmethod.keyboard.Key", description="Search").click()
    if not out:
        print("Success: click search button")
    wait()
    
    out = d(resourceId="com.amaze.filemanager:id/second", index=1).long_click()
    if not out:
        print("Success: long click data")
    wait()
    
    out = d(resourceId="com.amaze.filemanager:id/second", index=2).long_click()
    if not out:
        print("Success: long click metadata")
    wait()
    
    out = d(description="More options").click()
    if not out:
        print("Success: Open options")
    wait()
    
    out = d(className="android.widget.LinearLayout", index=2).click()
    if not out:
        print("Success: Clicked on 'Hide'")
    wait()
    
    out = d(description="Navigate up").click()
    if not out:
        print("Success: Opened up Menu")
    wait()
    
    out = d(className="androidx.appcompat.widget.LinearLayoutCompat", index=1).click()
    if not out:
        print("Success: Clicked on 'Internal Storage'")
    wait()
    
    out = d(resourceId="com.amaze.filemanager:id/search").click()
    if not out:
        print("Success: Clicked on Search")
    wait()
    
    out = d(resourceId="com.amaze.filemanager:id/search_edit_text").set_text(text="data")
    if not out:
        print("Set text to Data")
    wait()
    
    out = d(className="com.android.inputmethod.keyboard.Key", description="Search").click()
    if not out:
        print("Success: click search button")
    wait()
    

    print("Successful Replay!")
