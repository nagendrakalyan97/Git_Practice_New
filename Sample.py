import random
def SumOfNumbers(Input):
    count = 0
    while(Input>0):
        count += Input%10
        Input = int(Input/10)
    return count

Input = int(random.randint(9,999999999))
print("Given input number is: ", Input)
result = SumOfNumbers(Input)
while(result > 9):
    result = SumOfNumbers(result)
else:
    print("Count of numbers is", result)