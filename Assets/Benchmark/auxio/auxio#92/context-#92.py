import sys
import time
import subprocess
import uiautomator2 as u2
import os

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':
    avd_serial = "emulator-5554"
    d = u2.connect(avd_serial)

    base_dir = '/Users/jannis/Desktop/University/Bachelor/10_Semester/Bachelor_Arbeit/Pre_Presentation'
    local_mp3_path = os.path.join(base_dir, 'Dataset_extension', 'auxio', 'music.mp3')
    remote_music_dir = '/storage/emulated/0/music'
    remote_mp3_path = os.path.join(remote_music_dir, 'music.mp3')

    # Push music.mp3 to the music folder
    d.push(local_mp3_path, remote_mp3_path)
    print("Successfully pushed music.mp3 to the music folder.")

    d.app_start("com.github.libretube")
    wait()

    d(text="Pick folders").click()
    wait()

    d(text="New folder").click()
    wait()

    d(text="Music").click()
    wait()

    d(text="USE THIS FOLDER").click()
    wait()

    d(text="ALLOW").click()
    wait()

    d(text="Save").click()
    wait()

    d(text="And the Glory of the Lord || CeeNaija.com").click()
    wait()