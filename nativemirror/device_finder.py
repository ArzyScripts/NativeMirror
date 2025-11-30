import subprocess

def list_devices():
    out = subprocess.getoutput("adb devices")
    lines = out.splitlines()[1:]
    devices = []
    for l in lines:
        if l.strip() and "device" in l:
            serial = l.split()[0]
            devices.append(serial)
    return devices
