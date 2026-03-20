import sys
import time
import subprocess
import uiautomator2 as u2

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


def add_app_icon_to_home(d, app_label="aFreeRDP"):
    # go to home screen
    d.press("home")
    time.sleep(1)

    # open app drawer (common gesture on many launchers)
    d.swipe(0.5, 0.9, 0.5, 0.1, 0.2)
    time.sleep(1)

    icon = d(text=app_label)
    if not icon.exists:
        print(f"Could not find app icon '{app_label}' in app drawer")
        return

    w, h = d.window_size()
    icon.drag_to(w * 0.6, h * 0.3)
    time.sleep(0.5)

    # confirm by going home
    d.press("home")
    print(f"Added '{app_label}' to home screen.")

if __name__ == '__main__':
    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)

    add_app_icon_to_home(d, app_label="SimpleX")
    wait()

    d.app_start("chat.simplex.app")
    wait()

    d(text="Create your profile").click()
    wait()

    d(focused=True).set_text("TechyNoob")
    wait()

    d(text="Create").click()
    wait()

    d(text="Don't create address").click()
    wait()

    d(text="Use chat").click()
    wait()

    d(text="OK").click()
    wait()

    d(className="android.view.View", index=1).click()
    wait()

    d(text="OK").click()
    wait()

    d.press("Home")

