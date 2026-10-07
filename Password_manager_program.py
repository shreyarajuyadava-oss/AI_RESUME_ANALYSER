'''uses:
dictionary,loops,conditionals,modules,file handling
website: password
random module
file read/write
real world application

'''

import random
import string

passwords ={}

#load existing files
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, password = line.strip().split(":")
            passwords[website] = password

except:
    pass

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(8))
    return password

while True:
    print( "\n -------PASSWORD MANAGER APP-------")
    print("1. save Password")
    print("2. View Passwords")
    print("3. generate Password")
    print("4. Exit")

    choice = input("Enter your choice : ")

    #save password
    if choice == '1':
        website = input("Enter Website Name : ")
        password = input("Enter Password : ")
        passwords[website] = password
        with open("passwords.txt", "a") as file:
            file.write(f"{website}:{password}\n")
        print(f"Password for {website} saved successfully!")

    #view passwords
    elif choice == '2':
        if not passwords:
            print("No passwords found.")
        else:
            print("\nSaved Passwords:")
            for website, password in passwords.items():
                print(f"Website: {website}, Password: {password}")

    #generate password
    elif choice == '3':
        print("generated password",generate_password(8))

    #exit
    elif choice == '4':
        print("Exiting the Password Manager App. Goodbye!")
        break

    else:   
        print("Invalid choice. Please try again.")
        