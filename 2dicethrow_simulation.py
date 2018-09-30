import random #Imports the random function

differentRolls = [] #Makes an empty list

for i in range(1,1001): #Loop for 1000 times
    dice1 = random.randrange(1,7) #Computes a random number for the first dice
    dice2 = random.randrange(1,7) #Computes a random number for the second dice
    sumOfRolls = dice1+dice2 #Computes the sum of each roll
    differentRolls.append(sumOfRolls) #Adds the sum to the empty list

print("Roll\tNumber") #Makes a row for rolls and the times it occured
print("----\t---------") #Seperator

for rollNumber in range(2,13): #Repeats from 2 to 12
    amountOfRolls = differentRolls.count(rollNumber) #stores how many times the roll occured
    print(rollNumber, "\t", amountOfRolls) #Prints the roll and how many times it occured
