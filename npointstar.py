import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex

point = int(input("How many points do you want your star to have? Enter an odd positive integer: ")) # This is taking the input of the user and making it an integer

inAngle = 180/point #Calculates the inside angle to turn
outAngle = 180 - inAngle #Calculates outside angle

alex.penup() #Makes sure that there it doesn't draw
alex.back(40) #Just moves it back to go in center
alex.pendown()#Goes back to drawing

alex.left(inAngle)#Makes original angle
alex.forward(70)#Goes forward
for i in range(point-1): #Repeats
        alex.right(outAngle)#Second angle and so on
        alex.forward(70)
