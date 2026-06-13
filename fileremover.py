import shutil
import sys
import os
import time
import time

while True:
    print("[F]ILE OR [D]IR [E TO EXIT]")
    choice = input("CHOICE: ")


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

    if choice == "E":
        print("EXITING")
        break

    if choice not in ["F", "D", "E"]:
        print("INVALID.\n")