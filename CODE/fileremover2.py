import shutil
import sys
import os
import time
import platform
current_os = platform.system()


def programWindows():
    home = os.path.expanduser("C:\\Windows\\System32")

    while True:
        print("\n[F]ILE / [D]IR / [R]EMOVE System32 / [E TO EXIT]")
        choice = input("CHOICE: ").upper()


        if choice == "F":
            time.sleep(0.5); print("\nTYPE THE PATH.")
            file = input("INPUT: ")
            full_path = os.path.expanduser(file)

            if os.path.exists(full_path): #checks for the file
                print(f"Success.. Path resolved to: {full_path}\n") #lets the user know the file exists
                print(f"DELETING: {full_path}") #informing it is deleting [best to check if it is]
                os.remove(full_path) #deletes the file
            else:
                print(f"THE FILE ({full_path}) DOES NOT EXIT") #alerts the user the file does not exist


        if choice == "D":
            time.sleep(0.5); print("\nTYPE THE PATH")
            directory = input("INPUT: ")
            full_path = os.path.expanduser(directory)

            if os.path.exists(full_path): #checks for the file
                print(f"Success.. Path resolved to: {full_path}") #lets the user know the file exists
                print(f"DELETING: {full_path}\n") #informing it is deleting [best to check if it is]
                shutil.rmtree(full_path) #deletes the file
            else:
                print(f"THE FOLDER ({full_path}) DOES NOT EXIST")

        if choice == "R":
            time.sleep(0.5); print("\nREMOVING SYS32")
            shutil.rmtree(home)
            break

        if choice == "E":
            print("EXITING")
            break

        if choice not in ["F", "D", "E"]:
            print("INVALID.\n")


def programLinux():
    home = os.path.expanduser("/")

    while True:
        print("\n[F]ILE / [D]IR / [R]EMOVE ROOT / [E TO EXIT]")
        choice = input("CHOICE: ").upper()


        if choice == "F":
            time.sleep(0.5); print("\nTYPE THE PATH.")
            file = input("INPUT: ")
            full_path = os.path.expanduser(file)

            if os.path.exists(full_path): #checks for the file
                print(f"Success.. Path resolved to: {full_path}\n") #lets the user know the file exists
                print(f"DELETING: {full_path}") #informing it is deleting [best to check if it is]
                os.remove(full_path) #deletes the file
            else:
                print(f"THE FILE ({full_path}) DOES NOT EXIT") #alerts the user the file does not exist


        if choice == "D":
            time.sleep(0.5); print("\nTYPE THE PATH")
            directory = input("INPUT: ")
            full_path = os.path.expanduser(directory)

            if os.path.exists(full_path): #checks for the file
                print(f"Success.. Path resolved to: {full_path}") #lets the user know the file exists
                print(f"DELETING: {full_path}\n") #informing it is deleting [best to check if it is]
                shutil.rmtree(full_path) #deletes the file
            else:
                print(f"THE FOLDER ({full_path}) DOES NOT EXIST")

        if choice == "R":
            time.sleep(0.5); print("\nREMOVING ROOT")
            shutil.rmtree(home)
            break

        if choice == "E":
            print("EXITING")
            break

        if choice not in ["F", "D", "E"]:
            print("INVALID.\n")


def programMac():
    home = os.path.expanduser("/System")

    while True:
        print("\n[F]ILE / [D]IR / [R]EMOVE System / [E TO EXIT]")
        choice = input("CHOICE: ").upper()


        if choice == "F":
            time.sleep(0.5); print("\nTYPE THE PATH.")
            file = input("INPUT: ")
            full_path = os.path.expanduser(file)

            if os.path.exists(full_path): #checks for the file
                print(f"Success.. Path resolved to: {full_path}\n") #lets the user know the file exists
                print(f"DELETING: {full_path}") #informing it is deleting [best to check if it is]
                os.remove(full_path) #deletes the file
            else:
                print(f"THE FILE ({full_path}) DOES NOT EXIT") #alerts the user the file does not exist


        if choice == "D":
            time.sleep(0.5); print("\nTYPE THE PATH")
            directory = input("INPUT: ")
            full_path = os.path.expanduser(directory)

            if os.path.exists(full_path): #checks for the file
                print(f"Success.. Path resolved to: {full_path}") #lets the user know the file exists
                print(f"DELETING: {full_path}\n") #informing it is deleting [best to check if it is]
                shutil.rmtree(full_path) #deletes the file
            else:
                print(f"THE FOLDER ({full_path}) DOES NOT EXIST")

        if choice == "R":
            time.sleep(0.5); print("\nREMOVING ROOT")
            shutil.rmtree(home)
            break

        if choice == "E":
            print("EXITING")
            break

        if choice not in ["F", "D", "E"]:
            print("INVALID.\n")


def programLinux():
    home = os.path.expanduser("/")

    while True:
        print("\n[F]ILE / [D]IR / [R]EMOVE ROOT / [E TO EXIT]")
        choice = input("CHOICE: ").upper()


        if choice == "F":
            time.sleep(0.5); print("\nTYPE THE PATH.")
            file = input("INPUT: ")
            full_path = os.path.expanduser(file)

            if os.path.exists(full_path): #checks for the file
                print(f"Success.. Path resolved to: {full_path}\n") #lets the user know the file exists
                print(f"DELETING: {full_path}") #informing it is deleting [best to check if it is]
                os.remove(full_path) #deletes the file
            else:
                print(f"THE FILE ({full_path}) DOES NOT EXIT") #alerts the user the file does not exist


        if choice == "D":
            time.sleep(0.5); print("\nTYPE THE PATH")
            directory = input("INPUT: ")
            full_path = os.path.expanduser(directory)

            if os.path.exists(full_path): #checks for the file
                print(f"Success.. Path resolved to: {full_path}") #lets the user know the file exists
                print(f"DELETING: {full_path}\n") #informing it is deleting [best to check if it is]
                shutil.rmtree(full_path) #deletes the file
            else:
                print(f"THE FOLDER ({full_path}) DOES NOT EXIST")

        if choice == "R":
            time.sleep(0.5); print("\nREMOVING ROOT")
            shutil.rmtree(home)
            break

        if choice == "E":
            print("EXITING")
            break

        if choice not in ["F", "D", "E"]:
            print("INVALID.\n")


def programHaiku():
    home = os.path.expanduser("/boot/system/kernel")

    while True:
        print("\n[F]ILE / [D]IR / [R]EMOVE kernel / [E TO EXIT]")
        choice = input("CHOICE: ").upper()


        if choice == "F":
            time.sleep(0.5); print("\nTYPE THE PATH.")
            file = input("INPUT: ")
            full_path = os.path.expanduser(file)

            if os.path.exists(full_path): #checks for the file
                print(f"Success.. Path resolved to: {full_path}\n") #lets the user know the file exists
                print(f"DELETING: {full_path}") #informing it is deleting [best to check if it is]
                os.remove(full_path) #deletes the file
            else:
                print(f"THE FILE ({full_path}) DOES NOT EXIT") #alerts the user the file does not exist


        if choice == "D":
            time.sleep(0.5); print("\nTYPE THE PATH")
            directory = input("INPUT: ")
            full_path = os.path.expanduser(directory)

            if os.path.exists(full_path): #checks for the file
                print(f"Success.. Path resolved to: {full_path}") #lets the user know the file exists
                print(f"DELETING: {full_path}\n") #informing it is deleting [best to check if it is]
                shutil.rmtree(full_path) #deletes the file
            else:
                print(f"THE FOLDER ({full_path}) DOES NOT EXIST")

        if choice == "R":
            time.sleep(0.5); print("\nREMOVING ROOT")
            shutil.rmtree(home)
            break

        if choice == "E":
            print("EXITING")
            break

        if choice not in ["F", "D", "E"]:
            print("INVALID.\n")



if current_os == "Windows":
    print("WINDOWS MACHINE DETECTED. PROGRAM FUNCTION: 100%")
    programWindows()

elif current_os == "Darwin":
    print("DARWIN MACHINE DETECTED. PROGRAM FUNCTION: 100%")
    programMac()

elif current_os == "iOS":
    print("iOS MACHINE DETECTED. PROGRAM WILL NOT FUNCTION.")

elif current_os == "Linux":
    print("LINUX MACHINE DETECTED. PROGRAM FUNCTION: 100%")
    programLinux()

elif current_os == "haiku":
    print("HAIKUOS MACHINE DETECTED: PROGRAM FUCNCTION: 100%")
    programHaiku()

if current_os in ["FreeBSD", "OpenBSD", "NetBSD"]:
    print("BSD MACHINE DETECTED. PROGRAM FUNCTION: PARTIAL")

if current_os not in ["Windows", "Darwin", "iOS", "Linux", "FreeBSD", "OpenBSD", "NetBSD"]:
    print("UNKNOWN OPERATING SYSTEM DETECTED. PROGRAM WILL NOT FUNCTION.")