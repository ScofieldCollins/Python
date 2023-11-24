def collatz(number):
    if(number % 2 == 0):
        print(number//2)
        return number//2
    else:
        print(3*number + 1)
        return 3*number + 1
     
print("please input a int number :")
try:
    num = int(input())
    while num != 1:
        num = collatz(num)
except ValueError:
    print("please input a int number,it is not number")

    