#!/usr/bin/env python3
from cryptography.fernet import Fernet
import os

def f_finder(CWD):
    for file in os.listdir(CWD):
        if file == "secure.py" or file == "key.txt":
            continue
        cwd=os.path.join(CWD,file)
        if os.path.isfile(cwd):
            files.append(cwd)
        elif os.path.isdir(cwd):
            dirs.append(cwd)

files=[]
dirs=[]
dirs.append(os.getcwd())
for dir in dirs:
    f_finder(dir)
pin=input("ENTER your key\n==> ")
if pin=="225390":
    choise=input("WHat Do YoU WAnt To dO?\npress [1] for SECURE \npress [2] for UNLOCK\n==> ")
    if choise =='1':

        key=Fernet.generate_key()
        with open("key.txt","wb") as KEY:
            KEY.write(key)
        for file in files:
            with open(file, "rb") as CON:
                context=CON.read()
            context=Fernet(key).encrypt(context)
            with open(file,"wb") as file:
                file.write(context)
        print("\n------------------------------------\n")
        print("\n---YOur FIls ArE LOCKED & SEcurED---\n")
        print("\n------------------------------------\n")
    elif choise=='2':
        with open("key.txt","rb") as KEY:
            key=KEY.read()
        for file in files:
            with open(file, "rb") as CON:
                context=CON.read()
            context=Fernet(key).decrypt(context)
            with open(file,"wb") as file:
                file.write(context)
        print("\n------------------------------------\n")
        print("\n-------YOur FIls ArE UNLOCKED-------\n")
        print("\n------------------------------------\n")