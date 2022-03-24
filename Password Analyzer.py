from os import system

def clear_screen():
    system("cls")

name = input("\nEnter your name : ")

clear_screen()

print("-----------------  PASSWORD ANALYzER  ------------------")

print(f"Hi {name}. We'll be helping you out to set a strong password for your accounts.")

print("Lets begin !!\n\nRULES TO BE FOLLOWED\n\nRULE 1: The Password must contain atleast one uppercase letter.\nRULE 2: The Password must contain special characters like @,#,$,%,^,&,*,!.\nRULE 3: The Password must contain a minimum of 6 characters.\n\n")

password = input("Enter the password : ")
length = len(password)
passer = list(password.upper())

if length>=6:
    print(f"\nSize of password - PERFECT")
    if '@' or '#' or '$' or '%' or '^' or '&' or '*' or '!' or "_" or '-' in password:
        print("Special characters - INCLUDED")
    else:
        print("Special characters not included.\nTry again :(")
    
    for x in passer:
        if x in password:
            print("Uppercase character - INCLUDED\n")
            print("YOUR PASSWORD HAS PASSED ALL THE TESTS AND ITS SECURITY LEVEL IS HIGH.\n")
            break
    else:
        print("Uppercase not included.\nTry again :(")

else:
    print("No.of characters in the password is less than 5.\nTry again :(")