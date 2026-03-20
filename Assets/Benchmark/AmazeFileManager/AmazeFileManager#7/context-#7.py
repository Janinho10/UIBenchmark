import sys
import time
import uiautomator2 as u2
import subprocess
import tarfile
import os

if __name__ == '__main__':

    #Disable pop-ups, move to storage/emulated/0/Download, and create gz.rar.gz file

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "com.amaze.filemanager"
    
    #Disable Pop-Ups
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.WRITE_EXTERNAL_STORAGE", shell=True)
    subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} android.permission.READ_EXTERNAL_STORAGE", shell=True)

    #create gz.tar.gz-file
    local_filename = "gz.tar.gz"
    dummy_content_name = "test_content.txt"
    
    #Create a dummy text file to put inside the archive
    with open(dummy_content_name, "w") as f:
        f.write("This is some dummy content for the archive.")

    with tarfile.open(local_filename, "w:gz") as tar:
        tar.add(dummy_content_name)
    #Remove dummy file
    if os.path.exists(dummy_content_name):
        os.remove(dummy_content_name)
    
    #push gz.tar.gz-file to device
    remote_dir = "/storage/emulated/0/Download"
    subprocess.run(f"adb -s {avd_serial} shell mkdir -p {remote_dir}", shell=True)
    subprocess.run(f"adb -s {avd_serial} push {local_filename} {remote_dir}/{local_filename}", shell=True)
    os.remove(local_filename)
    
    d.app_start(package_name, stop=True)
    time.sleep(2)
    
    d(text="Download").click()
    
