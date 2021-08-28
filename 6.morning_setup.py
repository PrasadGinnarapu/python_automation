"""importing webbrowswer module"""
import sys
import webbrowser


def opensetup():
    """function for open user specified website"""

    var = input("Enter g-google, 'd'-darwin, o-office: ").strip()
    if var == 'g':
        webbrowser.open("www.google.com")
    elif var == 'd':
        webbrowser.open("https://ojasit.darwinbox.com/user/login")
    elif var == 'o':
        webbrowser.open("https://www.office.com/?auth=2")


while True:
    yesno = input("Do you want to play(Y/N): ").upper()
    if yesno == 'Y':
        opensetup()
    else:
        sys.exit()
