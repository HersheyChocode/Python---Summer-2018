# print the first n Fibonacci numbers
n = int(input("Enter a positive integer n: "))
firstNumber = 1
secondNumber = 1
print('1 1',end=' ')
for i in range(3,n+1):
    currentNumber = firstNumber + secondNumber # computes the newest Fibonacci number
    print(str(currentNumber),end=' ')
    # move the two numbers one down the list
    firstNumber = secondNumber  
    secondNumber = currentNumber
