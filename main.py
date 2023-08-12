from turtle import Turtle, Screen
from spaceship import Spaceship
from enemy import Enemy
from bullet import Bullet
from scoreboard import Scoreboard
import time

# constants
BULLET_ENEMY_COLLISION_DISTANCE = 30
TIME_BETWEEN_UPDATES = 0.1
BOTTOM_EDGE_SCREEN = -300

# configure screen setup
screen = Screen()
screen.setup(600, 600)
screen.title("Play a game of Space Invaders!")
screen.tracer(n=0)

# render spaceship
spaceship = Spaceship()

# spaceship movements
screen.listen()
screen.onkey(fun=spaceship.move_right, key="Right")
screen.onkey(fun=spaceship.move_left, key="Left")

# render enemy turtles
enemy = Enemy()

# render bullet and bullet movement
bullet = Bullet(screen)
screen.onkey(lambda : bullet.fire_bullet(spaceship.xcor()), key="Up")

# render scoreboard
scoreboard = Scoreboard()

# main game loop
game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(TIME_BETWEEN_UPDATES)    

    # enemy movement
    enemy.drop_enemies()  # have the enemies keep dropping down until they go off screen
    if enemy.off_screen() :
        # once all enemies have gone past screen, send in next wave
        enemy.next_wave()
    
    # detect spaceship and enemy collision, bullet and enemy collision
    for enemy_turtle in enemy.enemies :  # checking through individual enemies in enemies list
        # check for every enemy turtle's position, if the spaceship is within it
        if enemy_turtle.xcor() - 12 <= spaceship.xcor() <= enemy_turtle.xcor() + 12 and spaceship.ycor() >= enemy_turtle.ycor() - 15:
            scoreboard.game_over()  # render game over text
            game_is_on = False  # stop game loop

        # check for collisions with any bullet
        for curr_bullet in bullet.active_bullets :  # checking through individual bullets in bullets list
            if enemy_turtle.distance(curr_bullet) <=  BULLET_ENEMY_COLLISION_DISTANCE :
                # check shortest distance between the current bullet and the enemy 
                scoreboard.increment_score()  # increment score on scoreboard
                enemy_turtle.hideturtle()  # hide the enemy being shot at first 
                enemy.enemies.remove(enemy_turtle)  # remove the enemy being shot at from the enemies list

        # check how many enemies successfully went off screen
        if enemy_turtle.ycor() <= BOTTOM_EDGE_SCREEN :
            enemy.enemies.remove(enemy_turtle)
            scoreboard.decrement_life()
    
    # check if out of lives
    if scoreboard.out_of_lives() :
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()