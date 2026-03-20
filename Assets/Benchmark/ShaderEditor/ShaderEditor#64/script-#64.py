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
                                "\n\tfor (float i=.0; i<4.; i++) {" \
                                "\n\t\tuv.x += sin(T*(i+1.)+uv.y*1.5)*.2;" \
                                "\n\t\tcol += abs(.05/uv.x*.5);"
                                "\n\t}" \
                                "\n" \
                                "\n\tgl_FragColor = vec4(col, 1);" \
                                "\n}")
    if not out:
        print("Success: set text")
    wait()
    
    out = d(resourceId="de.markusfisch.android.shadereditor:id/toggle_code").click()
    if not out:
        print("Success: toggled code")
    wait()
    
    out = d(resourceId="de.markusfisch.android.shadereditor:id/toggle_code").click()
    if not out:
        print("Success: toggled code")
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
                                "\n\tfor (float i=.0; i<4.; i++) {" \
                                "\n\t\tuv.x += sin(T*(i+1.)+uv.y*1.5)*.2;" \
                                "\n\t\tcol += abs(.05/uv.x*.5);"
                                "\n\t}" \
                                "\n" \
                                "\n\tcol *= hue(T*.25)*.4;" \
                                "\n\tcol = sqrt(col);" \
                                "\n" \
                                "\n\tgl_FragColor = vec4(col, 1);" \
                                "\n}")
    if not out:
        print("Success: set text")
    wait()
    
    out = d(resourceId="de.markusfisch.android.shadereditor:id/toggle_code").click()
    if not out:
        print("Success: toggled code")
    wait()
    
    print("Successful Replay!")
