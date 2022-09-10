Input = int(input("Enter a number"))
count = 0
while(Input!=0):
    count += Input%10
    Input = int(Input/10)
print("Count is: ",count) 