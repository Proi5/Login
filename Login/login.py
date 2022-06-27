from turtle import clear
from save import *

print("Welcom to login page")

Idn = input("User name : ")

print("  ")

Pass = input("Password : ")

if Idn == Id:
    print("Id is correcte")
if Pass == Password:
    print("Password is correct")
if Idn != Id:
    print("user name not available")
    exit()
if Pass != Password:
    print("wrong password")
    exit()
print("  ")
print("Welcome to your account")
print("   ")
print("To see your account details press 1")
print("")
drt = input("choose")
if drt == ("1"):
    print("Name = " + Name)
    print("Mobail Number = " + Number)
    print("User Id = " + Id)
    print("Password = *********")
    clear


