import turtle
import random

#######################################           Global Variables ###############################################################
#distinct_colors
colors  = ["red","green","blue","orange","purple","pink","yellow","dark green","dark red","lime","dark blue","medium violet red",
           "cyan","saddle brown","dark gray","dark orange","medium purple","magenta"]
#dark_colors
dark_colors = ["white","red","green","blue","orange","purple","pink","yellow","black"]

#tilt_angle
tilt_angle = 45
#line_width
line_width_max = 2.7
line_width_mid = 2
line_width_min = 1
common_bg_color = 'black'
#line_length
length = 5

#######################################           Global Variables ###############################################################

def remote_concentric_circles(circle_turtle,dis_range,radius):
    """ Function to draw Concentric Circles
    Parameters:
    arg1 (turtle class): Turtle Class Refernce
    arg2 (int)         : Distance Range
    arg3 (int)         : Circle Radius 
    Returns:
    None:Returning None

    """
    for i in range(dis_range):
        color = random.choice(dark_colors)
        circle_turtle.color(color)
        circle_turtle.circle(radius*i)
        circle_turtle.up()
        circle_turtle.sety((radius*i)*(-1))
        circle_turtle.down()

    circle_turtle.up()
    circle_turtle.goto(0,0)
    circle_turtle.down()


##################################################################################################################################

if __name__ == "__main__":

        remote_turtle = turtle.Turtle()
        remote_turtle_screen = turtle.Screen()
        remote_turtle_screen.bgcolor(dark_colors[7])
        remote_turtle.speed(0)

        remote_turtle.color(dark_colors[8])
        remote_turtle.width(line_width_max)

        for i in range(0,8):
                remote_turtle.forward(216)
                remote_turtle.penup()
                remote_turtle.backward(216)
                remote_turtle.pendown()
                remote_turtle.left(tilt_angle)

        remote_turtle.width(line_width_min + 0.6)
        
        for i in range(0,8):
                remote_turtle.forward(90)
                remote_turtle.right(68)
                remote_turtle.forward(166)
                remote_turtle.penup()
                remote_turtle.backward(166)
                remote_turtle.left(68)
                remote_turtle.backward(90)
                remote_turtle.pendown()
                remote_turtle.left(tilt_angle)

        remote_turtle.width(line_width_min + 0.3)
        
        for i in range(0,8):
                remote_turtle.forward(90)
                remote_turtle.right(68)
                remote_turtle.forward(54)
                remote_turtle.left(94)
                remote_turtle.forward(116)
                remote_turtle.backward(116)
                remote_turtle.right(94)
                remote_turtle.backward(54)
                remote_turtle.left(68)
                remote_turtle.backward(90)
                remote_turtle.left(tilt_angle)
        
        remote_turtle.width(3)
        remote_concentric_circles(remote_turtle,15,3)
        
        remote_turtle.width(2)
        #start drawing the lines
        for count in range(15):
          remote_turtle.forward(length)
          remote_turtle.right(135)
          remote_turtle.color('black')    #change the color 
          length = length + 5
        
        #Reset the Original Position
        remote_turtle.penup()
        remote_turtle.home()
        remote_turtle.pendown()
        
        #exit the turtle class on click()
        turtle.Screen().exitonclick()
