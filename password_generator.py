import string
import random

def randompassword(x):
    max_len = x
    chars = string.ascii_letters + string.digits
    size = 0
    return ''.join(random.choice(chars) for x in range(size,max_len))

print(" Your password should contain length minimum -> 3 ")
m = 0
n = int(input('How many passwords do you want to generate?'))
while m < n:
    x = int(input('What length of password do you want?'))
    if x<3:
        print("Sorry, choose length above 3 !!")
        break
    elif x>2 and x<6:
        print(randompassword(x))
        print("Alert !! You have a weak password !!")
    elif x>5 and x<12:
        print(randompassword(x))
        print("Strong password !!")
    else:
        print(randompassword(x))
        print("Very Strong password !!!")
    m = m + 1