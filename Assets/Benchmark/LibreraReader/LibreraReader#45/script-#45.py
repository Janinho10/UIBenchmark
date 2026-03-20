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
    wait()
    
    out = d(text="FOLDER").click()
    if not out:
        print("Success: clicked on FOLDER")
    wait()
    
    out = d(text="RECENT").click()
    if not out:
        print("Success: clicked on RECENT")
    wait()
    
    out = d(text="FAVORITES").click()
    if not out:
        print("Success: clicked on FAVORITES")
    wait()
    
    out = d(text="BOOKMARKS").click()
    if not out:
        print("Success: clicked on BOOKMARKS")
    wait()
    
    out = d(text="NETWORK").click()
    if not out:
        print("Success: clicked on NETWORK")
    wait()
    
    out = d(scrollable=True).scroll.horiz.toBeginning()
    if not out:
        print("Success: scrolled back to beginning")
    wait()
    
    out = d(text="LIBRARY").click()
    if not out:
        print("Success: clicked on LIBRARY")
    wait()
    
    out = d.press("recent")
    if not out:
        print("Success: opened recent")
    wait()
    
    out = d(scrollable=True).scroll.horiz.backward()
    if not out:
        print("Success: scrolled to Play Store")
    wait()
    
    w, h = d.window_size()
    
    out = d.click(w / 2, h / 2)
    if not out:
        print("Success: clicked on Play Store")
    wait()
    
    out = d(scrollable=True).scroll.to(text="Data safety")
    if not out:
        print("Success: scrolled to Data safety")
    wait()
    
    out = d(description="Screenshot 1 of 8").click()
    if not out:
        print("Success: clicked on the first screenshot")
    wait()
    
    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolled to second screenshot")
    wait()
    
    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolled to third screenshot")
    wait()
    
    out = d(scrollable=True).scroll.horiz.forward()
    if not out:
        print("Success: scrolled to fourth screenshot")
    wait()
    
    out = d.press("back")
    if not out:
        print("Success: pressed back")
    wait()
    
    out = d.press("recent")
    if not out:
        print("Success: opened recent")
    wait()
    
    out = d(scrollable=True).scroll.horiz.backward()
    if not out:
        print("Success: scrolled to Librera")
    wait()
    
    out = d.click(w / 2, h / 2)
    if not out:
        print("Success: clicked on Librera")
    wait()
    
    while True:
        if d(descriptionContains="kenta pogo1741503846169-2 pdf").exists:
            break
        d(className="androidx.recyclerview.widget.RecyclerView").scroll.forward(direction="vertical")
    print("Success: scrolled to kenta book")
    wait()
    
    out = d(descriptionContains="kenta pogo1741503846169-2 pdf").click()
    if not out:
        print("Success: clicked on kenta book")
    wait()
    
    out = d(text="Book mode").click()
    if not out:
        print("Success: clicked on Book mode")
    wait()
    
    out = d(resourceId="com.foobnix.pro.pdf.reader:id/bookClose").click()
    if not out:
        print("Success: closed the book")
    wait()
    
    print("Successful Replay!")
