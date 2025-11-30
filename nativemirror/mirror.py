import subprocess, cv2, numpy as np

def start_mirror(serial):
    cmd = ["adb", "-s", serial, "exec-out", "screenrecord", "--output-format=h264", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return p
