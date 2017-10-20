import turtle
import random
import math

#creating border
def border_screen():
        border = turtle.Turtle()
        border.penup()
        border.setposition(-250,-250)
        border.pendown()
        border.pensize(3)
        for _ in range(4):
                border.forward(500)
                border.left(90)
        border.hideturtle()


#keyboard bindings
def keyboard_binding(Alex,key):
	if key =='a':
		Alex.left(45)
	elif key =='d':
		Alex.right(45)
	elif key =='w':
		Alex.forward(30)
	elif key =='s':
		Alex.backward(30)
	else:
		return -1
		
		
#distance between Alex and Alice	
def distance(Alex,Alice):
	d = math.sqrt((Alex.xcor()-Alice.xcor())**2+(Alex.ycor()-Alice.ycor())**2)
	return d


#game statistics	
def statistics(Alex, Alice,step,pen):
	
	
	
	pen.undo()
	pen.penup()
	pen.hideturtle()
	pen.setposition(-240,270)
	
	pen_string ="step#" ,step ," Distance between Alex & Alice ",distance(Alex,Alice)
	pen.write(pen_string, False, align = "left",font=["Arial",14,"normal"])
def check_boundary(object, halfWindowWidth, halfWindowHeight):

	if object.xcor() > halfWindowWidth or object.xcor() < -halfWindowWidth or \
	 object.ycor() > halfWindowHeight or object.ycor() < -halfWindowHeight:
		object.setposition(random.randint(-halfWindowHeight, halfWindowWidth), \
			random.randint(-halfWindowWidth, halfWindowHeight))
		
		
def main():
	window = turtle.Screen()
	windowHeight, windowWidth = 500, 500
	window.screensize(canvwidth=windowWidth, canvheight=windowHeight)
	border_screen()
	Alex = turtle.Turtle()
	Alex.color("blue")
	Alex.shape("turtle")
	Alex.speed(0)
	Alex.setposition(0,0)
	Alex.penup()
	#boundary  checking for Alex

		
	Alice =turtle.Turtle()
	Alice.color("red")
	Alice.shape("turtle")
	Alice.speed(0)
	Alice.penup()
	Alice.setposition(random.randint(-windowWidth/2, windowHeight/2),random.randint(-windowWidth/2, windowHeight/2))
	Alice.pendown()
	Alex.pendown()
	step =0

	pen = turtle.Turtle() # writing steps information on top of screen
	while True: 
		step +=1
		move = random.randint(1,3)
		
		if move < 3:
		    Alice.forward(20)
		else :
			direction = random.randint(1,2)
			if direction ==1:
				Alice.left(90)
			else:
				Alice.right(90)
		
		while True:
			key = input("Move Alex: ")
			if keyboard_binding(Alex,key) ==-1:
				print('my string is not recognized as a movement. Retype \n')
			else:
				break

		check_boundary(Alex,windowWidth/2, windowHeight/2)
		check_boundary(Alice,windowWidth/2, windowHeight/2)
		
		
		statistics(Alex, Alice,step,pen)
		if distance(Alex,Alice)<=30:
			break
	window.exitonclick()  #exit on click

if __name__=='__main__':
	main()
