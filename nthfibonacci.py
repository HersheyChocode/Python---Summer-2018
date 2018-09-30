n = int(input("Enter a positive integer n: "))
firstNumber = 1
secondNumber = 1
for i in range(3,n+1):
    currentNumber = firstNumber + secondNumber # computes the newest Fibonacci number
    # move the two numbers one down the list
    firstNumber = secondNumber  
    secondNumber = currentNumber
print("The nth Fibonacci number is: "+str(currentNumber))
