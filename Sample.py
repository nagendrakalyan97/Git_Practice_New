import random

Input = int(random.randint(999,99999))
count = 0
while(Input!=0):
    count += Input%10
    Input = int(Input/10)
print("Count is: ",count) 