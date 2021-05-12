import os 
import sys 
import time 

class Token:
    def __init__(self):
        entryuser = input("Enter Your Username: ")
        with open("documents/userdoc.txt" ,'r') as userfile :
            for entryuser in userfile:
                print("User Found!")
                entrypass = input("Enter Your Password: ")
                with open("documents/passdoc.txt",'r') as passfile :
                    for entrypass in passfile:
                        print("Pass Found!")
                    else:
                        print("Pass Not Found!")
                        time.sleep(5)
                        sys.exit() 
            else:
                print("User Not Found!")
                time.sleep(5)
                sys.exit() 
Token()