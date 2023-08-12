from turtle import Turtle

TOP_SCREEN = 270
NUM_OF_LIVES = 3
ALIGNNMENT = "center"
FONT_SCORE_LIVES = ("Arial", 14, "normal")
FONT_GAME_OVER = ("Arial", 20, "normal")

class Scoreboard(Turtle) :

    def __init__(self) :
        super().__init__()
        self.score_counter = 0
        self.num_of_lives = NUM_OF_LIVES
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=TOP_SCREEN)
        self.write(f"Score : {self.score_counter}     No. of lives : {self.num_of_lives}", align=ALIGNNMENT, font=FONT_SCORE_LIVES)

    def game_over(self) :
        self.goto(x = 0, y = 0)
        self.write("Game Over!", align=ALIGNNMENT, font=FONT_GAME_OVER)

    def increment_score(self) :
        self.score_counter += 1
        self.clear()
        self.write(f"Score : {self.score_counter}     No. of lives : {self.num_of_lives}", align=ALIGNNMENT, font=FONT_SCORE_LIVES)

    def decrement_life(self) :
        self.num_of_lives -= 1
        self.clear()
        self.write(f"Score : {self.score_counter}     No. of lives : {self.num_of_lives}", align=ALIGNNMENT, font=FONT_SCORE_LIVES)

    def out_of_lives(self) :
        return self.num_of_lives == 0