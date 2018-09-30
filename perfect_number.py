#A number $n$ is called perfect if the sum of its proper divisors equals $n$.
def sum_of_proper_divs(n):#function
    y = 0#variable for storing the addition value
    d = 0#variable for storing the addition value
    for v in range(1,n):#repetition of the additon
        if n%v==0:#if v is a multiple of n:
            d=v#variable stores value of v
            y = y+d#Adds previous value and new value - stores to same variable
    return y#returns the sum of the mulitples

for i in range(100,999):#Computes the sums of all triple digit numbers
    sum_of_proper_divs(i)#computes each number from 100-999
    if i==sum_of_proper_divs(i):#If the number inputted equals to the number returned...
        print(sum_of_proper_divs(i))#print the number
