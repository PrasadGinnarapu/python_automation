"""importing required module i.e requests"""
import requests


def wheatherrep():
    """Function for """

    city = input("Enter Your City :")
    result = requests.get(f'https://wttr.in/{city}')  #{sys.argv[1].replace(" ", "+")}'
    print(result.text)


wheatherrep()
