#Password manager

"""
Objective: write a password managing application. The user will have a file with 
all his passwords. The user inputs name of the website, login and password and the
program stores this data in an encrypted file. The user can also remove an item, 
update a password, view all names of the websites and seach login and password by name.

Concepts used in project:
-file I/O
-encryption/decryption using fernet


Modules used in the project:
Fernet

"""

from cryptography.fernet import Fernet
import time

info = {}
def to_dict():
    file = open("data.txt", "r")
    text = file.readlines()
    file.close()
    for item in text:
        website, login, password = item.split(':')
        info[website] = [login, password]

def actions():
    print("1) Add a password and login to the file")
    print("2) Show all websites with passwords and logins stored")
    print("3) Retrieve a login and password for a website")
    print("4) Update a password/login")
    print("5) Delete an item")
    print("6) Exit Password Manager")
def choice(user_input):
    if user_input == 1:
        add()
    if user_input == 2:
        show()
    if user_input == 3:
        retrieve()
    if user_input == 4:
        update()
    if user_input == 5:
        delete()
    if user_input == 6:
        return False
    return True

def add():
    website = input("Enter the name of the website: ")
    login = input("Enter login: ")
    password = input("Enter password: ")
    info[website] = [login, password]
    file = open("data.txt", "a")
    file.write(website + ":" + login + ":" + password + "\n")
    file.close()

    time.sleep(1)

    print("Your password and login are successfully stored.")
    print()

    time.sleep(1)

def show():
    websites = list(info.keys())
    websites.sort()
    time.sleep(1)
    print(*websites)
    print()
    time.sleep(1)

def retrieve():
    print("Enter the name of website for which you want to retrieve login and password: ", end = ' ')
    website = input()
    login, password = info[website]

    time.sleep(1)
    print(f'Login: {login}, password: {password}')
    print()
    time.sleep(1)

def update():
    time.sleep(1)
    website = input("Enter the website name: ")
    n_login = input("Enter new login: ")
    n_password = input("Enter new password: ")
    info[website] = [n_login, n_password]

    #overwriting login and password in the file
    time.sleep(1)
    file = open("data.txt", "w")
    for key in info.keys():
        login, password = info[key]
        file.write(key + ":" + login + ":" + password)
    file.close()
    print("Login and password are successufully updated! ")
    time.sleep(1)

def delete():
    time.sleep(1)
    print("Enter the name of the website you want to delete: ", end = ' ')
    website = input()
    info.pop(website)
    file = open("data.txt", "w")
    for key in info.keys():
        login, password = info[key]
        file.write(key + ":" + login + ":" + password)
    file.close()
    
    time.sleep(1)
    print("The item successfully deleted.")
    print()
    time.sleep(1)

#main loop
if __name__ == '__main__':
    run = True
    print("Welcome to password manager! ")
    to_dict()
    while run:
        actions()
        user_input = input("Your choice: ")
        run = choice(int(user_input))