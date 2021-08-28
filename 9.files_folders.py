"""os and shutil modules required"""
import os
import shutil
import sys


def create():

    user_input = input("Choose d-Folder,f-File: ")
    if user_input == 'd':
        directory_name = input("Enter Directory Name: ")
        os.mkdir(f"D:/{directory_name}")
        print("Folder Created Successfully @ D:")
    elif user_input =='f':
        print("Sorry,File creation under Developing....")
        pass


def rename():

    user_input = input("Choose d-Folder,f-File: ")
    if user_input == 'd':
        old_directory_name = input("Enter Old Directory Name: ")
        new_directory_name = input("Enter Old Directory Name: ")
        os.rename(f"D:/{old_directory_name}",f"D:/{new_directory_name}")
        print("Folder Renamed Successfully @ D:")
    elif user_input == 'f':
        print("Sorry,File Rename under Developing....")
        pass


def move():
    user_input = input("Choose d-Folder,f-File: ")
    if user_input == 'd':
        file_name = input("Enter file Name: ")
        shutil.move(f"D:/prasad/{file_name}",f"D:\prasad2")
        print("File Moved Successfully @ D:")
    elif user_input == 'f':
        print("Sorry,File creation under Developing....")
        pass




while True:
    user_input = input("Enter C-Create, M-Move, R-Rename, U-Update: ").upper()
    if user_input == 'C':
        create()
    elif user_input == 'R':
        rename()
    elif user_input == 'M':
        move()
    elif user_input =='U':
        print("Sorry, Update under devolopment...")
    else:
        sys.exit()


