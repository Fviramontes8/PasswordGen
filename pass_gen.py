# -*- coding: utf-8 -*-
"""
Author: Ya boi Franku

Description: Takes an input from the input line and writes 100 lines to a
     text file called password.txt. There is a random chance that the password
     will be added to the file, SO MAKE SURE TO RUN THIS MULTIPLE TIMES
     
             kplsthx
"""

import string
import random
import hashlib

def random_gen(size=6, chars=string.ascii_lowercase + string.digits):
    #Returns 6 random lowercase letters or digits
    return ''.join(random.choice(chars) for _ in range(size))

def grab_input():
    #Grabs input from input line
    device = raw_input("Enter device for password:\n")
    
    '''
    If the input is longer than 9 characters, we call the function recursively
     until the user provides an input less than 9 characters.
    '''
    if len(device) > 9:
        print("Device's name is too long!")
        return grab_input()
    else:
        return device
    
device_name = grab_input()

#Opens/creates password.txt and appends to the file
password_txt = open("password.txt", "a")

#digest of the SHA256 of a string
device_password = hashlib.sha256(device_name).hexdigest()

#Writes either a random string of 6 characters or the password of the device
for i in range(98):
    if random.uniform(0, 1) > 0.98:
        #print(len(obj_pass))
        #print("\tHenlo")
        password_txt.write(device_password[4:10]+"\n")
        print("Password has been written to file.\n")
    else:
        password_txt.write(random_gen()+"\n")

#Closes text file
password_txt.close()