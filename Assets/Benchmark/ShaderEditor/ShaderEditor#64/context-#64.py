# bug reproduction script for bug #285 of ActivityDiary
import sys
import time
import subprocess
import uiautomator2 as u2

def get_requested_permissions(serial, package):
    cmd = f"adb -s {serial} shell dumpsys package {package}"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    permissions = []
    parsing = False
    
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("requested permissions:"):
            parsing = True
            continue
        if parsing:
            if line.startswith("android.permission."):
                perm = line.split(":")[0]
                permissions.append(perm)
            elif line == "" or line.startswith("install permissions:") or line.endswith(":"):
                break
    
    return permissions


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    
    package_name = "de.markusfisch.android.shadereditor"
    
    requested_perms = get_requested_permissions(avd_serial, package_name)
    for perm in requested_perms:
        subprocess.run(f"adb -s {avd_serial} shell pm grant {package_name} {perm}", shell=True, check=False, stderr=subprocess.DEVNULL)
    
    d.app_start(package_name)
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "de.markusfisch.android.shadereditor":
            break
        time.sleep(2)
    wait()
    
    out = d(textContains="FRAGMENT").set_text("#ifdef GL_FRAGMENT_PRECISION_HIGH"
                              "\nprecision highp float;" \
                                "\n#else" \
                                "\nprecision mediump float;" \
                                "\n#endif" \
                                "\n" \
                                "\nuniform vec2 resolution;" \
                                "\nuniform float time;" \
                                "\n" \
                                "\n#define T time" \
                                "\n" \
                                "\n#define hue(a) (.6+.6*cos(6.3*(a)+vec3(0,23,21)))" \
                                "\n" \
                                "void main(void) {" \
                                "\n\tvec2 uv = (" \
                                "\n\t\tgl_FragCoord.xy-.5*resolution" \
                                "\n\t)/min(resolution.x, resolution.y);" \
                                "\n" \
                                "\n\tvec3 col = vec3(0);" \
                                "\n" \
                                "\n\tf" \
                                "\n" \
                                "\n\tgl_FragColor = vec4(col, 1);" \
                                "\n}")

    if not out:
        print("Success: set text to recording text")
    wait()
    
    print("Successful Context!")
