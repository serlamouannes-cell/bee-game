import pgzrun
import random

WIDTH = 400
HEIGHT = 400
TITLE = "Bee Game"

score = 0
game_over = False

bee=Actor("bee")
bee.pos=100,100

flower=Actor("flower")
flower.pos=200,200

def draw():
    screen.blit("bg",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+str(score), color="black",topleft=(10,10))
    if game_over:
        screen.fill("pink")
        screen.draw.text("Time's Up! Your final Score :" +str(score), color="black",midtop=(200,10))

def move_flower():
    flower.x=random.randint (50,350)
    flower.y=random.randint (50,350)

def update():
    global score
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2

    if bee.colliderect(flower):
        move_flower()
        score = score + 10

def timer():
    global game_over 
    game_over=True
clock.schedule(timer,60.0)








pgzrun.go()