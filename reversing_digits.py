num = int(input("Type in a 4-digit number please: "))

#I took the first digit by cancelling the remainders when dividing by 1000
a = num//1000

#This is the thousands place
firstPlacement = a*1000
#I cancelled out the remainder when dividing by 100 to get second digit - also subtracted first placement
b = (num - (firstPlacement))//100

#This is the hundreds place
secondPlacement = 100*b 
# I cancelled out the remainder when dividing by 10 to get third digit - also subtracted first and second placement
c = (num - (firstPlacement+secondPlacement))//10

#This is the tens place 
thirdPlacement = 10*c 
#Final digit
d = num - (firstPlacement+secondPlacement+thirdPlacement) 

#prints backwards with place values
print (1000*d + 100*c + 10*b + a)
