# bug reproduction script for bug #4451of ankidroid
import sys
import time

import uiautomator2 as u2

# Among Android 6.0, 7.1 and 10.0, this bug is only reproducible on Android 6.0.

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)


    d.app_start("net.gsantner.markor")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "net.gsantner.markor":
            break
        time.sleep(2)
    wait(3)
    
    out = d(resourceId="net.gsantner.markor:id/ui__filesystem_item__root", index=1).click()
    if not out:
        print("Success: Clicked on Q")
    
    wait()
    
    """

    out = d(resourceId="net.gsantner.markor:id/document__fragment__edit__content_editor__scrolling_parent").set_text("test file")
    if not out:
        print("Success: add file content")
    wait()

    out = d.press("back")
    if not out:
        print("Success: click back")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: click back")
    wait()
    
    """

    out = d(resourceId="net.gsantner.markor:id/ui__filesystem_item__title", text="hello.md").long_click(1)
    if not out:
        print("Success: long click the new file")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: click More options")
    wait()

    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[2]').click()
    if not out:
        print("Success: click move")
    wait()

    out = d(resourceId="net.gsantner.markor:id/ui__filesystem_item__title").click()
    if not out:
        print("Success: choose another folder (the parent folder)")
    wait()
    
    out = d(resourceId="net.gsantner.markor:id/ui__filesystem_item__title").click()
    if not out:
        print("Success: choose another folder (the parent folder)")
    wait()
    
    out = d(resourceId="net.gsantner.markor:id/ui__filesystem_item__title").click()
    if not out:
        print("Success: choose another folder (the parent folder)")
    wait()

    out = d(resourceId="net.gsantner.markor:id/ui__filesystem_item__root", index=3).click()
    if not out:
        print("Success: clicked on Folder")
    wait()
    
    out = d(resourceId="net.gsantner.markor:id/ui__filesystem_dialog__button_ok").click()
    if not out:
        print("Success: clicked on select this folder")
    wait()

    print("Successful Replay!")
