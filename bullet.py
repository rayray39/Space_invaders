from turtle import Turtle

BOTTOM_EDGE_SCREEN = -310
TOP_EDGE_OF_SCREEN = 315
BULLET_COLOR = "cyan"

class Bullet(Turtle) :

    active_bullets = []

    def __init__(self, screen) :
        # instance of self acts like the master bullet that controls the firing of subsequent initialised bullets
        super().__init__()
        self.screen = screen
        self.shape("circle")
        self.setheading(90)
        self.penup()
        self.goto(x=0, y=BOTTOM_EDGE_SCREEN)

    def fire_bullet(self, spaceship_x) :
        # create a new Turtle instance (a new bullet) that the master bullet will be firing off
        bullet = Turtle("circle")
        bullet.color(BULLET_COLOR)
        bullet.penup()
        bullet.setheading(90)
        bullet.goto(x=spaceship_x, y=self.ycor())  # newly created bullet goes to spaceship_xcor, where Up was pressed, and the master bullet's ycor
        self.active_bullets.append(bullet)  # add it to the list of bullets going to be fired
        self.move_bullet(bullet)  # master bullet calls the move bullet method on this newly created bullet

    def move_bullet(self, bullet) :
        bullet.forward(15)  # have this bullet move forward
        if bullet.ycor() >= TOP_EDGE_OF_SCREEN :
            # check if it has gone off screen
            self.active_bullets.remove(bullet)  # once an active bullet has gone past the screen, remove it from the list
        else :
            # if it has yet to go off screen, call this move_bullet function on the same bullet again afte 100ms 
            # to make to seem like the bullet is moving continuously
            self.screen.ontimer(lambda : self.move_bullet(bullet), 100)