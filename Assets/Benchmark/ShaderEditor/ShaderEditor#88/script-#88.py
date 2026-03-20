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
    wait()

    out = d(textContains="resolution").set_text(
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
    "\n\t\tvec3 q = p;"
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
    if not out:
        print("Success: set new text")
    wait()

    out = d(textContains="resolution").set_text(
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
    "\n\t\tvec3 q = p;"
    "\n\t\tfloat d = length(q)-1.;"
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
    if not out:
        print("Success: set new text")
    wait()

    out = d(textContains="resolution").set_text(
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
    "\n\t\tvec3 q = p;"
    "\n\t\tq = mod(q, 8.) - 4.;"
    "\n\t\tq = abs(q)-vec3(1);"
    "\n\t\tfloat d = length(q)-1.;"
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
    if not out:
        print("Success: set new text")
    wait()

    out = d(textContains="resolution").set_text(
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
    "\n\t\tvec3 q = p;"
    "\n\t\tq = mod(q, 8.) - 4.;"
    "\n\t\tq = abs(q)-vec3(1);"
    "\n\t\tfloat d = max(max(q.x,q.y),q.z);"
    "\n\t\td *= mix(.75,1.,fract((sin(T*dot(uv,uv)))*345678.));"
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
    if not out:
        print("Success: set new text")
    wait()

    out = d(textContains="resolution").set_text(
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
    "\n\t\tvec3 q = p;"
    "\n\t\tq = mod(q, 8.) - 4.;"
    "\n\t\tq = abs(q)-vec3(1);"
    "\n\t\tfloat d = max(max(q.x,q.y),q.z);"
    "\n\t\td *= mix(.75,1.,fract((sin(T*dot(uv,uv)))*345678.));"
    "\n"
    "\n\t\tif (d < 1e-2) d = 1e-1;"
    "\n"
    "\n\t\tp += rd*d;"
    "\n"
    "\n\t\tcol += pow(5e-4/d, .75)*vec3(1,2,3);"
    "\n\t}"
    "\n"
    "\n\tgl_FragColor = vec4(col, 1);"
    "\n}"
    )
    if not out:
        print("Success: set new text")
    wait()

    out = d(textContains="resolution").set_text(
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
    "\n\tro = vec3(0, sin(T), -3),"
    "\n\trd = normalize(vec3(uv, 1)),"
    "\n\tp = ro;"
    "\n"
    "\n\tfor (float i=.0; i<30.; i++) {"
    "\n\t\tvec3 q = p;"
    "\n\t\tq = mod(q, 8.) - 4.;"
    "\n\t\tq = abs(q)-vec3(1);"
    "\n\t\tfloat d = max(max(q.x,q.y),q.z);"
    "\n\t\td *= mix(.75,1.,fract((sin(T*dot(uv,uv)))*345678.));"
    "\n"
    "\n\t\tif (d < 1e-2) d = 1e-1;"
    "\n"
    "\n\t\tp += rd*d;"
    "\n"
    "\n\t\tcol += pow(5e-4/d, .75)*vec3(1,2,3);"
    "\n\t}"
    "\n"
    "\n\tgl_FragColor = vec4(col, 1);"
    "\n}"
    )
    if not out:
        print("Success: set new text")
    wait()

    out = d(textContains="resolution").set_text(
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
    "\n\tro = vec3(0, sin(T), exp(cos(T))-8.),"
    "\n\trd = normalize(vec3(uv, 1)),"
    "\n\tp = ro;"
    "\n"
    "\n\tfor (float i=.0; i<30.; i++) {"
    "\n\t\tvec3 q = p;"
    "\n\t\tq = mod(q, 8.) - 4.;"
    "\n\t\tq = abs(q)-vec3(1);"
    "\n\t\tfloat d = max(max(q.x,q.y),q.z);"
    "\n\t\td *= mix(.75,1.,fract((sin(T*dot(uv,uv)))*345678.));"
    "\n"
    "\n\t\tif (d < 1e-2) d = 1e-1;"
    "\n"
    "\n\t\tp += rd*d;"
    "\n"
    "\n\t\tcol += pow(5e-4/d, .75)*vec3(1,2,3);"
    "\n\t}"
    "\n"
    "\n\tgl_FragColor = vec4(col, 1);"
    "\n}"
    )
    if not out:
        print("Success: set new text")
    wait()

    out = d(resourceId="de.markusfisch.android.shadereditor:id/toggle_code").click()
    if not out:
        print("Success: toggled code")
    wait()

    out = d(resourceId="de.markusfisch.android.shadereditor:id/toggle_code").click()
    if not out:
        print("Success: toggled code")
    wait()

    out = d(textContains="resolution").set_text(
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
    "\n\tro = vec3(0, sin(T), 0),"
    "\n\trd = normalize(vec3(uv, 1)),"
    "\n\tp = ro;"
    "\n"
    "\n\tfor (float i=.0; i<30.; i++) {"
    "\n\t\tvec3 q = p;"
    "\n\t\tq = mod(q, 8.) - 4.;"
    "\n\t\tq = abs(q)-vec3(1);"
    "\n\t\tfloat d = max(max(q.x,q.y),q.z);"
    "\n\t\td *= mix(.75,1.,fract((sin(T*dot(uv,uv)))*345678.));"
    "\n"
    "\n\t\tif (d < 1e-2) d = 1e-1;"
    "\n"
    "\n\t\tp += rd*d;"
    "\n"
    "\n\t\tcol += pow(5e-4/d, .75)*vec3(1,2,3);"
    "\n\t}"
    "\n"
    "\n\tgl_FragColor = vec4(col, 1);"
    "\n}"
    )
    if not out:
        print("Success: set new text")
    wait()    

    out = d(textContains="resolution").set_text(
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
    "\n\tro = vec3(0, sin(T), 0),"
    "\n\trd = normalize(vec3(uv, 1)),"
    "\n\tp = ro;"
    "\n"
    "\n\tfor (float i=.0; i<30.; i++) {"
    "\n\t\tvec3 q = p;"
    "\n\t\tq.z += T*7.;"
    "\n\t\tq = mod(q, 8.) - 4.;"
    "\n\t\tq = abs(q)-vec3(1);"
    "\n\t\tfloat d = max(max(q.x,q.y),q.z);"
    "\n\t\td *= mix(.75,1.,fract((sin(T*dot(uv,uv)))*345678.));"
    "\n"
    "\n\t\tif (d < 1e-2) d = 1e-1;"
    "\n"
    "\n\t\tp += rd*d;"
    "\n"
    "\n\t\tcol += pow(5e-4/d, .75)*vec3(1,2,3);"
    "\n\t}"
    "\n"
    "\n\tgl_FragColor = vec4(col, 1);"
    "\n}"
    )
    if not out:
        print("Success: set new text")
    wait()

    out = d(resourceId="de.markusfisch.android.shadereditor:id/toggle_code").click()
    if not out:
        print("Success: toggled code")
    wait()