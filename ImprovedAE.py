from medipipe_had_sign import hand_identifier

import pygame
import random
import math
from pygame import mixer
import threading
from medipipe_had_sign import hand_identifier

#Available ships are ship1, ship2, ship3, ship4


while True:
    player_ship = input("Choose a Cruiser!:")
    Player = set(player_ship.lower().split())

    available_cruiers = {'ship1', 'ship2', 'ship3', 'ship4'}
    if available_cruiers & Player:
        print("Okay!")
        break

    else:
        print('Invalid Cruiser: ship1, ship2, ship3, ship4')
        continue



# ... (your other code)

# Create a variable to indicate whether hand tracking is running
hand_tracking_running = False

# Define a function to start hand tracking
def start_hand_tracking():
    global hand_tracking_running
    hand_tracking_running = True
    while hand_tracking_running:
        hand_result = hand_identifier()
        pygame.time.delay(100)

# Start the hand tracking thread
hand_thread = threading.Thread(target=start_hand_tracking)
hand_thread.start()



# This will initialize the pygame
pygame.init()
# This will give you the display screen with the use of width and height and creates the screen
screen = pygame.display.set_mode((1200, 1000))

# This is the background, add the BG to the while loop for it to work
background = pygame.image.load("SpaceBG6.png")



restart_button = pygame.image.load("retry_button.png")
restart_button_rect = restart_button.get_rect()
restart_button_rect.center = (600, 600)


# This part of the code will change the dsiplay icon
pygame.display.set_caption("SHOOT THE ARMY OF GERLAD!!!")
icon = pygame.image.load("potato.png")  # This line code mentions the icon, the icon has to be in a 32 Pixel
pygame.display.set_icon(icon)  # Displays the icon on the window



mixer.music.load("Relaxing Music Lofi Waterfall Background.mp3 ")
mixer.music.play(-1)

player1 = pygame.image.load(f"ships\{player_ship}.png")
playerx = 550
playery = 800
playerx_change = 0

# Adding more enemy
enemy1 = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []


enemy2 = pygame.image.load("enemy1.png")
enemy2x = []
enemy2y = []
enemy2x_change = []
enemy2y_change = []



num_of_enemies = 7

# Where going to use append code instead of equal so that the enemies can be copied
for i in range(num_of_enemies):
    # Adiing the enemy image
    enemy1.append(pygame.image.load("robot2.png"))
    # This codes is the x and y axis on where you want the enemy to be placed
    enemyx.append(random.randint(0, 800))  # This allows the enemy to appear from left to right randomly
    enemyy.append(random.randint(60, 250))  # This allows the enemy to appear up and down but with a limit of 150
    enemyx_change.append(0.5)  # This will make the enemy move sideways
    enemyy_change.append(120)  # This will make the enemy move downward


for i in range(num_of_enemies):
    enemy2x.append(random.randint(0, 800))
    enemy2y.append(random.randint(60, 250))
    enemy2x_change.append(0.5)
    enemy2y_change.append(120)


# Adiing the bullet image
bullet1 = pygame.image.load("cheese-burger.png")
# This codes is the x and y axis on where you want the enemy to be placed
bulletx = 0
bullety = 800  # The size of the player ship
bulletx_change = 0  # X axis will not be use because the bullet will be moving upward
bullety_change = 3.5 #faster shooting of burger
bullet_state = "ready"
# The ready state means that, you can't see the bullet on the screen
# Fire will be the buller moving



title = pygame.font.Font("HaveFun.ttf", 100)
Textx = 300
Texty = 0


def Title(Textx, Texty):
    score = pygame.image.load("title.jpg")
    screen.blit(score, (Textx, Texty))


# This will be the scoring
score_value = 0

# Thid code is built in the pygame and this is displaying the type of font and the size of it
font = pygame.font.Font("HaveFun.ttf", 30)
# This is the x and y coordinates of the game
textx = 30
texty = 950

# Gamve over Text
Over_font = pygame.font.Font("HaveFun.ttf", 100)


# The code below is rendering the text that will show on the screen
def Score(x, y):
    score = font.render("ALIENS ELIMINATED!!!: " + str(score_value), True, (0, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = Over_font.render("GAME OVER!!", True, (255, 0, 0))
    screen.blit(over_text, (350, 350))


def player(x, y):
    screen.blit(player1, (x, y))
    # The code "blit" meand to draw, the code is drawing an image in the screen
    # In this it is saying that the player image should appear in these coordinates


def enemy(x, y, i):
    screen.blit(enemy1[i], (x, y))
    # This will draw in the enemy


def fire_bullet(x, y):
    global bullet_state  # The code "global" is a function use so that the def command can use the bullet
    bullet_state = "fire"
    screen.blit(bullet1, (x + 16, y + 10))  # This command will make the image appear in that specific coordinates
    # The reason why we put "x +16, y + 10" to make sure that the bullet will appear in the spaceship and to give it a bit more of an illusion


# This will make the bullet colide with the enemy
def collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
    # This is the equation for collision "Distance between two points and the midpoint
    if distance < 30:  # This is the distance for the enemy and bullet collision
        return True
    else:  # This code is saying if this distance is less than 27 pixels then reurn the value of True else return value of False
        return False


def reset_game():
    global playerx, playery, playerx_change, score_value

    # Reset player position and state
    playerx = 550
    playery = 800
    playerx_change = 0

    # Reset score
    score_value = 0

    # Reset enemy positions
    for i in range(num_of_enemies):
        enemyx[i] = random.randint(0, 800)
        enemyy[i] = random.randint(60, 100)
    for i in range(num_of_enemies):
        enemy2x[i] = random.randint(0, 800)
        enemy2y[i] = random.randint(60, 100)




running = True
while running:
    #screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))


    # Anything happening in the game is in this code below


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -2.3
            if event.key == pygame.K_RIGHT:
                playerx_change = 2.3
            
            if event.key == pygame.K_q:
                break

            if event.key == pygame.K_UP:
                if bullet_state == "ready":
            
            

                    # This code below give the bullet sound
                    Bullet_Sound = mixer.Sound("BulletZound.wav")
                    Bullet_Sound.play()

                    bulletx = playerx
                    fire_bullet(playerx, bullety)

            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0





        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if restart_button_rect.collidepoint(event.pos):
                reset_game()
    # Check if both hands are detected


        # This value zero prevents it from moving if the keys aren't being pressed


    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 1138:
        playerx = 1138

    for i in range(num_of_enemies):
        # This will give the enemy movement

        # Gameover
        if enemyy[i] > 750 or enemy2y[i] > 750:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
                enemy2y[j] = 2000  # Set the y-coordinate of the special enemy to a high value
            hand_tracking_running = False
            screen.blit(restart_button, restart_button_rect)
            game_over_text()
            break


        enemy2x[i] += enemy2x_change[i]
        if enemy2x[i] <= 0:
            enemy2x_change[i] = 0.6
            enemy2y[i] += enemy2y_change[i]
        elif enemy2x[i] >= 1140:
            enemy2x_change[i] = -0.6
            enemy2y[i] += enemy2y_change[i]

        collide2 = collision(enemy2x[i], enemy2y[i], bulletx, bullety)
        if collide2:
            # Handle collision with the new enemy
            eliminated_Sound = mixer.Sound("robot_destroyed2.mp3")
            eliminated_Sound.play()
            bullety = 800
            bullet_state = "ready"
            score_value += 1
            enemy2x[i] = random.randint(0, 1000)
            enemy2y[i] = random.randint(30, 100)

        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.8
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 1140:
            enemyx_change[i] = -0.8
            enemyy[i] += enemyy_change[i]



        collide = collision(enemyx[i], enemyy[i], bulletx, bullety)
        if collide:  # This is asking what do you what to happend after a collision?

            # This is when the alien is eliminated it will make a sound
            eliminated_Sound = mixer.Sound("robot_destroyed.mp3")
            eliminated_Sound.play()

            bullety = 800
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0, 1000)
            enemyy[i] = random.randint(30, 100)



        screen.blit(enemy2, (enemy2x[i], enemy2y[i]))
        enemy(enemyx[i], enemyy[i], i)

    # This will be the bullet movement
    if bullety <= 0:
        bullety = 800
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)  # In this line of code it is saying that as the action of firing a bullet appears it will then move a Y axis movement by fram
        bullety -= bullety_change

    player(playerx, playery)

    Score(textx, texty)

    Title(Textx, Texty)

    pygame.display.update()