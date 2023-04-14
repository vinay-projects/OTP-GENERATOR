import random
import time

a = input("Enter Your Mobile Number:")
if len(a) == 10:
    print("Number Valid")
    print("Your OTP is Generating:")
    time.sleep(2)
    for i in range(6):
        b = random.randrange(10)
        print(b, end=" ")
else:
    print("Number Invalid, must be integar and 10 digits :")