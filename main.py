from nativemirror.device_finder import list_devices
from nativemirror.mirror import start_mirror

def menu():
    print("NativeMirror CLI")
    while True:
        print("\nA) Refresh devices")
        print("Q) Quit")
        ch = input("> ").upper()
        if ch == "A":
            devs = list_devices()
            if not devs:
                print("No devices found.")
            else:
                for i,d in enumerate(devs):
                    print(f"{i+1}) {d}")
                sel = int(input("Select: ")) - 1
                serial = devs[sel]
                print("Starting mirror…")
                p = start_mirror(serial)
                print("Mirroring running (raw h264)…")
        elif ch == "Q":
            break

if __name__ == "__main__":
    menu()
