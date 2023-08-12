from turtle import Turtle

SCREEN_BOTTOM_EDGE_Y = -280
SCREEN_RIGHT_EDGE_X = 280
SCREEN_LEFT_EDGE_X = -285

class Spaceship(Turtle) :

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.setheading(90)
        self.penup()
        self.goto(x=0, y=SCREEN_BOTTOM_EDGE_Y)  # set its initial position to be center bottom of screen

    def move_right(self) :
        # controls movement to right
        curr_x_pos = self.xcor()
        new_x_pos = curr_x_pos + 15  # moves 15 pixels each time right key is press
        if new_x_pos >= SCREEN_RIGHT_EDGE_X :
            new_x_pos = SCREEN_RIGHT_EDGE_X
        self.goto(x=new_x_pos, y=self.ycor()) 

    def move_left(self) :
        # controls movement to left
        curr_x_pos = self.xcor()  # moves 15 pixels each time left key is press
        new_x_pos = curr_x_pos - 15
        if new_x_pos <= SCREEN_LEFT_EDGE_X :
            new_x_pos = SCREEN_LEFT_EDGE_X
        self.goto(x=new_x_pos, y=self.ycor())
