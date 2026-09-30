#=======================================
#get current time
#=======================================

from datetime import datetime


def get_current_time():
    now = datetime.now()
    print(now)
    # current_time = now.strftime("%H:%M:%S")
    current_time = now.strftime("%d-%m-%Y %I:%M:%S %p")
    return current_time


# print(get_current_time())

#=======================================
#roll a dice
#=======================================

import random

def roll_dice():
    return random.randint(1, 6)


#=======================================
#generate a secure password
#=======================================

import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += secrets.choice(characters)
    return password