from turtle import clear
Nots =()
from savenot import *
print()
print("Options")
print()
print("1.Right your nots and save (one time use only)")
print()
print("2.If you what to see the save data")
print()
Cho = input("Option : ")
if Cho == ("1"):
    Cho1 = input("Right you whant : ")
    cho2 = input("Did you want to save y/n : ")
    if cho2 == ("y"):
        h = open("savenot.py", "w")
        h.write("Nots = "+ "\"" + str(Cho1) + "\"")
        clear
    if cho2 == ("n"):
        clear
if Cho == ("2"):
    print(Nots)
    clear