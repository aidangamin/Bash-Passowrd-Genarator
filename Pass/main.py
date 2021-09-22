"""
Bash Password Genarator
Written In Python (Isn't it so obvious?)

Created By Aidan
"""


import random
import pyperclip
import sys
import base64
import tkinter
from modules.cipher import PasswordEncoder

def create_pass(length:int, num:bool, low:bool, up:bool, sym:bool):
    a = ""
    e = ""
    if num:
        a += "1234567890"
    if low:
        a += "qwertyuiopasdfghjklzxcvbnm"
    if up:
        a += "QWERTYUIOPASDFGHJKLZXCVBNM"
    if sym:
        a += "!@#$%^&*"
    
    
    
    for i in range(length):
        e += random.choice(a)
    return e

def main():
    while True:
        command = input(">>> ")
        tokens = command.split()
        if command.startswith("help"):
            print("  genarate length:[int] num:[bool] low:[bool] up:[bool] sym:[bool]\n  save:[directory]\n  open:[directory]")
        elif command.startswith("genarate"):
            try:
                a = create_pass(length=int(tokens[1]), num=bool(int(tokens[2])), low=bool(int(tokens[3])), up=bool(int(tokens[4])), sym=bool(int(tokens[5])))
                print(f"{a}\nPassword Has Been Copied To Clipboard")
                pyperclip.copy(a)
            except Exception as error:
                print(error)
        elif command.startswith("save"):
            with open(command[5:]+"\passwords.txt", "a") as f:
                f.write(PasswordEncoder.pass_encrypt(a))
                print(f"Saved Password As " + command[5:] + "passwords.txt")

        elif command.startswith("open"):
            with open(command[5:]+"\passwords.txt", "r") as f:
                print(PasswordEncoder.pass_decrypt(f.read()))
        
        else:
            print("Unknown Command.")

print("=-------------------------------=\n| Welcome to Password Genarator |\n=-------------------------------=\nBy Aidan..\nType help for help.")


try:
    main()
except KeyboardInterrupt:
    confirm = input("Press Enter To Exit.")
