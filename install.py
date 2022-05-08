import time
import os
os.system("clear")
import sys
os.system("clear")
print("Ghost Installer - By: Giuseppe\n\nGhost made by : EntySec (https://github.com/EntySec/Ghost)")
print("")
yes_or_no = input("Are you sure want to install?\n\nY/n: ")
os.system("clear")
if yes_or_no == "Y" or "y":
    kali_or_termux = input("Are you using [KALI]/[TERMUX]: ")
    os.system("clear")
    if kali_or_termux == "" or "UBUNTU":
        os.system("clear")
        print("Please choose between KALI/TERMUX next time :)\n\nPress CTRL + C to exit")
    if kali_or_termux == "KALI" or "[KALI]" in kali_or_termux:
        print("Starting download on KALI ...")
        time.sleep(1)
        os.system("clear")
    if kali_or_termux == "TERMUX" or "[TERMUX]":
        print("Starting download on TERMUX ...")
        time.sleep(1)
if yes_or_no == "N" or "n":
    os.system("clear")
    print("Goodbye :)")
    sys.exit()
while yes_or_no == "":
    os.system("clear")
    print("Sorry, i didn't get that")
    sys.exit()
    
