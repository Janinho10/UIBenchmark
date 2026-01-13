# bug reproduction script for bug #10 of ankidroid
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

    current_app = d.app_current()
    print(current_app)
    
    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: scroll to bottom")
    wait()
    
    out = d(text="Settings").click()
    if not out:
        print("Success: click on Settings")
    wait()
    
    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: scroll to bottom")
    wait()
    
    out = d(text="Developer options").click()
    if not out:
        print("Success: click on Developer options")
    wait()
    
    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: scroll to bottom")
    wait()
    
    out = d(text="Don’t keep activities").click()
    if not out:
        print("Success: enable Don't keep activities")
    wait()
    
    out = d(description="Navigate up").click()
    if not out:
        print("Success: go back")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: press back")
    wait()
    
    out = d(resourceId="com.android.launcher3:id/apps_list_view").scroll.toBeginning()
    if not out:
        print("Success: scroll to Top")
    wait()
    
    out = d(text="AnkiDroid").click()
    if not out:
        print("Success: Click on AnkiDroid")
    wait()
    
    out = d(text="Allow").click()
    if not out:
        print("Success: Click on ALLOW")
    wait()
    
    out = d(resourceId="com.ichi2.anki:id/fab_expand_menu_button").click()
    if not out:
        print("Success: press fab button")
    wait()

    out = d(resourceId="com.ichi2.anki:id/add_note_action").click()
    if not out:
        print("Success: press add")
    wait()

    out = d(className="android.widget.LinearLayout",
            resourceId="com.ichi2.anki:id/CardEditorEditFieldsLayout")\
        .child(className="android.widget.RelativeLayout", index="1")\
        .child(resourceId="com.ichi2.anki:id/id_note_editText").set_text("test")
    if not out:
        print("Success: set front text")
    wait()

    out = d(resourceId="com.ichi2.anki:id/action_save").click()
    if not out:
        print("Success: press save")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press back")
    wait()

    out = d(text="Default").click()
    if not out:
        print("Success: press default")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: press more options")
    wait()

    out = d(text="Edit note").click()
    if not out:
        print("Success: press Edit Note")
    wait()

    out = d(className="android.widget.LinearLayout",
            resourceId="com.ichi2.anki:id/CardEditorEditFieldsLayout") \
        .child(className="android.widget.RelativeLayout", index="3") \
        .child(resourceId="com.ichi2.anki:id/id_note_editText").set_text("you")
    if not out:
        print("Success: set back text")
    wait()

    out = d(resourceId="com.ichi2.anki:id/action_save").click()
    if not out:
        print("Success: press save")
    wait()


    print("Successful Replay!")
