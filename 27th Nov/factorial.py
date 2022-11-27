num = int(input("Enter your number : "))
fact = 1
if num < 0:
    print("The factorial for {} doesn't exist".format(num))
elif num == 0:
    print("The factorial of {} is 1")
else:
    for i in (1,num+1) :
        fact = fact * i
    print("Factorial of {} is {}".format(num,fact))