from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]
NUM_OF_ENEMIES = 6
BOTTOM_EDGE_SCREEN = -315

class Enemy(Turtle) :

    def __init__(self):
        super().__init__()
        self.enemies = []
        self.hideturtle()
        self.enemies = self.create_enemy()  # list of turtle objects

    def create_enemy(self) :
        # create a list of turtles that have random positions above the screen
        turtles = []
        for i in range(NUM_OF_ENEMIES) :
            color = random.choice(COLORS)
            x_pos = random.randint(-270, 270)
            y_pos = random.randint(340, 540)  # set its initial y pos to be somewhere off the top of screen
            enemy_turtle = Turtle("turtle")
            enemy_turtle.color(color)
            enemy_turtle.setheading(270)
            enemy_turtle.penup()
            enemy_turtle.goto(x=x_pos, y=y_pos)
            turtles.append(enemy_turtle)
        return turtles
            
    def drop_enemies(self) :
        # have the enemies y position decrease by 5 in each iteration of the main game loop
        # simulate dropping of enemies
        for turtle in self.enemies :
            turtle.goto(x=turtle.xcor(), y=turtle.ycor() - 3)

    def next_wave(self) :
        # clear the current contents of the list of enemies
        # create new enemies with new positions 
        self.enemies.clear()
        self.enemies = self.create_enemy()

    def off_screen(self) :
        # returns True if all enemies have gone past the bottom edge of screen, returns False otherwise
        for turtle in self.enemies :
            if turtle.ycor() > BOTTOM_EDGE_SCREEN :
                return False
        return True