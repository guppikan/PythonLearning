
''' This program will generate random password of lenght 6'''
# importing random module
import random
# String initiation
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()?"
# Declaring password length
password_length = 6
# generating random password
random_password = "".join(random.sample(string, password_length))
# Printing random password
print("The generated random password is : " + random_password)
# Second way of printing using format string
print(f"The generated random password is : {random_password}")
