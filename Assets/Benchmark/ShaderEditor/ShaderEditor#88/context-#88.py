import sys
import time
import subprocess
import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

if __name__ == '__main__':
    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)

    d.app_start("de.markusfisch.android.shadereditor")
    wait()

    d(textContains="resolution").set_text(
    "precision mediump float;"
    "\nuniform vec2 resolution;"
    "\nuniform float time;"
    "\n"
    "\n#define T time"
    "\n"
    "\nvoid main(void) {"
    "\n\tvec2 uv = ("
    "\n\t\tgl_FragCoord.xy-.5 * resolution"
    "\n\t)/min(resolution.x, resolution.y);"
    "\n"
    "\n\tvec3 col = vec3(0),"
    "\n\tro = vec3(0, 0, -3),"
    "\n\trd = normalize(vec3(uv, 1)),"
    "\n\tp = ro;"
    "\n"
    "\n\tfor (float i=.0; i<30.; i++) {"
    "\n\t\tfloat d = length(p)-1.;"
    "\n"
    "\n\t\tif (d < 1e-2) d = 1e-1;"
    "\n"
    "\n\t\tp += rd*d;"
    "\n"
    "\n\t\tcol += pow(5e-4/d, .75);"
    "\n\t}"
    "\n"
    "\n\tgl_FragColor = vec4(col, 1);"
    "\n}"
)
    

