# NativeMirror Installation Guide

USB Android screen mirroring using Python + ADB. This guide will help beginners set up NativeMirror easily.

---

## 🔖 Tags

`Android` `Mirroring` `USB` `Screen Mirroring` `ADB` `Python` `NativeMirror` `Windows Tools` `Tech Utilities`

---

## 📥 How to Install NativeMirror (Beginner-Friendly)

Follow these steps carefully. You **do not need prior Python knowledge** — NativeMirror will handle the setup automatically.

### **1️⃣ Download the Project**

* Click the **Code → Download ZIP** button on the GitHub repo
* Or download the release ZIP if available

### **2️⃣ Extract the ZIP**

* Right-click → **Extract All…**
* Choose an easy location like Desktop or Documents

### **3️⃣ Run the Launcher**

* Open the extracted folder
* Double-click:

```
run_nativemirror.bat
```

This launcher will:

* ✔ Check if Python is installed
* ✔ If Python is missing, download and install it automatically
* ✔ Install all required Python packages from `requirements.txt`
* ✔ Launch NativeMirror
* ✔ Prepare ADB for device detection

---

## 📱 Connecting Your Phone

1. Connect your phone to the PC using a USB cable
2. Make sure **USB Debugging** is enabled on the phone

   * Settings → About Phone → Tap Build Number 7× → Developer Options → USB Debugging → Enable
3. Run `run_nativemirror.bat`
4. Press **A** to refresh devices
5. Select your device from the list
6. NativeMirror will start mirroring your screen

**Tip:** If the phone screen is broken but USB Debugging was enabled previously, it will still work.

---

## 🖥 Features

* Mirrors Android screen over USB
* Works even with broken or black LCD screens
* Automatic Python installation if missing
* Automatic package installation
* Device detection and selection menu

---

## 🔧 Troubleshooting

* **No device found:**

  * Press **A** to refresh
  * Reconnect USB cable
  * Ensure USB Debugging is enabled
  * Use a known working USB cable

* **Device shows “Unknown”:**

  * The phone may still be mirrored as long as ADB can detect it

* **Python window closes instantly:**

  * Always run `run_nativemirror.bat` to see errors and logs

---

## 🧱 Project Structure

```
NativeMirror/
│ run_nativemirror.bat
│ install_python.ps1
│ requirements.txt
│ main.py
│ README.md
└─ nativemirror/
   │ device_finder.py
   │ mirror.py
   │ __init__.py
```

---

## 🚀 Notes

* NativeMirror requires **USB Debugging ON** for mirroring to work
* If USB Debugging is off, you may need an OTG mouse/keyboard to enable it
* The first run may take a few minutes while Python and dependencies are installed

---

# ❤️ Credits

Created by **ArzyScripts**
Powered by Python + ADB
