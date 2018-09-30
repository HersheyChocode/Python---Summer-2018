import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
snail = turtle.Turtle()    # Create a turtle, assign to alex

clockLength = 75 #This is the radius of the circle - used to create the stamps

snail.penup()
snail.left(120)
snail.forward(clockLength)
snail.stamp() #These lines were used to create the initial stamp
for x in range(11): #Makes the stamps for the rest of the clock
    snail.backward(clockLength)
    snail.left(30)
    snail.forward(clockLength)
    snail.stamp()

snail.back(clockLength)   #Returns to original position 

hour = int(input("Chose an hour you want your clock to be at")) #Inputted hour
minute = int(input("Chose the minute you want your clock to be at")) #Inputted minute

hour = (30*hour) + (minute/2) #This is the hour hand angle (more detailed explanation above)
minute = (6*minute) - hour #This is the minute hand angle - subtracts hour hand so it is back at its original position

snail.pendown() # Begins to draw

snail.right(hour) #Turns the hour degree
snail.forward(25) #Makes short line

snail.stamp() #Makes stamp for hour indicator

snail.penup() #Pauses to draw
snail.back(25) #Backs to original position

snail.pendown() #Resumes to draw

snail.right(minute) #Turns the minute angle
snail.forward(50) #Makes long line

snail.stamp() #Makes stamp for minute indicator
    

wn.mainloop()
#
