
from turtle import clear


print("Welcome to my worlde")
print("Pleas tell your name and dittails")
print(" ")
cho1 = input("Name : ")
print("   ")
cho2 = float(input("Mobail Nomber : "))
print("   ")
cho3 = input("create your user id : ")
print("   ")
cho4 = input("Create your password : ")
print("   ")
cho5 = input("conform your password : ")
print("   ")
if cho4 == cho5:
    print("Password is saved")
print("   ")
if cho4 != cho5:
    print("Ther was a problem")
    clear
print("Halo %s is your number(%d) was corect" %(cho1 , cho2))
print("  ")
print(">>>if all okay then type yes")
print("   ")
print(">>>if ther was a mistake then type clear")
print("   ")
cho6 = input()
if cho6 == ("clear"):
    clear
print("   ")
if cho6 == ("yes"):
    f = open("save.py", "w")
    f.write("Name = " + "\"" + str(cho1) + "\"" + "\n")
    f.write("Number = " + "\"" + str(cho2) + "\"" + "\n")
    f.write("Id = " + "\"" + str(cho3) + "\"" + "\n")
    f.write("Password = " + "\"" + str(cho4) + "\"" + "\n")
    f.close()
if cho6 == ("yes"):
    print("All okay now log in")
    print("  ")
    import First
        

           
    

