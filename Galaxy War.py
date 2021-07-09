#Name: Akarsh
#Program Name: #GalaxyWar.py
#What it does: a space game
#Submission Date: 1/17/2019

#Credits of my game
print ("==========CREDITS==========")
print ("  Main programmer: Akarsh")
print ("  Images: Google Images")
print ("  Sound: Audio Library Youtube")
print ("  Website for initiating the ship to shoot/more: Kids Can Code")

#imported all the modules needed
import pygame
import sys
import time
import random

#to start pygame
pygame.init()

#the display height and width set 
iDisplay_width = 800
iDisplay_height = 600

#this is the clock speed the game will be running on
iFPS = 30
iFPS2 = 30
iFPS3 = 30

#set the display size into one variable
screen = pygame.display.set_mode((800, 600)) #sets screen to 800 x 600

#all the colors needed in the game have been called
black = (0,0,0)
white = (255,255,255)
red = (125,0,0)
green = (0,125,0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#assignment statements we will need for keeping track of the points in the game
iNumber = 1
iTotal = 0
iPoints = 0 #for setting points to zero when game begins

#users or players characters width and height
iShip_width = 50
iShip_height = 85

#all the sound variables
pygame.mixer.init()# to turn on pygame
soundExplode = pygame.mixer.Sound("explode.wav") #used when bullet hits alien
soundGun = pygame.mixer.Sound("gunshot.wav") #used when user fires
soundWin = pygame.mixer.Sound("win.wav") #not used
soundDefeat = pygame.mixer.Sound("defeat.wav") #used when user crashes
pygame.mixer.music.load("background.wav") #used throughout game as background music

#assigning the display to another variable
gameDisplay = pygame.display.set_mode((iDisplay_width, iDisplay_height))

#caption to be displayed on top of window
pygame.display.set_caption('Galaxy War')

#creates an object to help keep time
clock = pygame.time.Clock()

#all the images needed for the game have been loaded into the game
crashImg = pygame.image.load("crash.png").convert_alpha()#used alpha to display png format images
backImg = pygame.image.load("space.jpg").convert() #convert used to create a copy that will draw more quickly on the screen
backImg_rect = backImg.get_rect() #background
playerImg = pygame.image.load("ship.png").convert()#convert used to create a copy that will draw more quickly on the screen
alienImg = pygame.image.load("alien.png").convert()#convert used to create a copy that will draw more quickly on the screen
bulletImg = pygame.image.load("bullet.png").convert()#convert used to create a copy that will draw more quickly on the screen
storyImg = pygame.image.load("story.png").convert_alpha()#used alpha to display png format images
startgp = False #checks if user has selected which mode
startgp2 = False #checks if user has selected which mode
intro = True

class MV():

    def __init__(self):
        self.startgp = False
        self.startgp2 = False
        self.startgp3 = False
        
#easier way to call the funtion MV()
Start = MV()

#text displayed on screen font and text can be called using this
def text_objects(text, font):
    textSurface = font.render(text, True, white) #sets color of font to white
    return textSurface, textSurface.get_rect()

#the text wanted to display on the screen can be written by calling this definiton
def message_display(text): # this definition statement for how the text will look like on the screen
    largeText = pygame.font.Font('font_one.ttf', 100) #the font and size
    TextSurf, textRect = text_objects(text, largeText) #sets to display large font
    textRect.center = ((iDisplay_width/2),(iDisplay_height/2))
    gameDisplay.blit(TextSurf, textRect) #called for displaying text

    pygame.display.update() #updates the screen

    time.sleep(2)#waits for two seconds

    game_loop() #starts game loop

#this funtion can be called to set the exact way wanted to display the text
def draw_text(surf, text, size, x, y):# this definition statement for how the text will look like on the screen
    font = pygame.font.Font('font_one.ttf', 70)#the font and size
    text_surface = font.render(text, True, white) #sets font to be white when displayed
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y) #sets the text to be displayed on midtop
    surf.blit(text_surface, text_rect)#called to display text
    
def button (msg, x,y,w,h,ic,ac,action = None ):# this funtion is called when creating a button and changing the way it displays
    dp = MV()
    mouse = pygame.mouse.get_pos() #gets the position of the mouse
    click = pygame.mouse.get_pressed() #assigns what click does
    if x+ w > mouse[0] >x and y + h > mouse[1] > y: # if left click, it is true, if right click, nothing happens 
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))#used for drawing the button on the screen
        if click[0] == 1 and action != None :#checks for the button player selects the option with
            #these are used when the player clicks a certain button, these will get activated
            if action == "Play": #for playing easy mode
                Start.startgp = True #starts this function
            elif action == "Play2": #for playing med mode
                Start.startgp2 = True #starts this function
            elif action == "Play3": #for playing hard mode
                Start.startgp3 = True #starts this function
            elif action == "Again":
                pygame.mixer.Sound.stop(soundDefeat)
                game_loop() # for going back to menu
            elif action == "Random":
                Start.startgp2 = True #starts this function
            elif action == "Story": #for looking at story
                story() #starts this function
            elif action == "Quit": # for quiting game
                pygame.quit()
                quit()
                
    else :
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.Font('font_one.ttf', 20)
    TextSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x +(w/2),(y +(h/2))))
    gameDisplay.blit(TextSurf, textRect)

# the crash funtion is called when the player loses
def crash():
    while True: #checks if it is true
        for event in pygame.event.get(): #if user quits, this is called
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        screen.blit(crashImg, [0, 0])#fills the game screen with black

        pygame.mixer.music.stop() #stops background music
        pygame.mixer.Sound.play(soundDefeat) #plays the losing music

        draw_text(screen, "You Died", 50, 400, 150)#message displayed for user to feel nice when they lose
        draw_text(screen, "Good Try Pilot!", 50, 400, 250)
        
        #the button displayed when player loses
        button ("Play Again",125,415,150,50,green,white,"Again")#used if player wants to play again
        button ("Quit",525,415,150,50,red,white,"Quit")# used if player would like to quit

        pygame.display.update()#updates
        clock.tick(15) 

# this makes the main menu of the game 
def game_intro():
    while intro: #while loop will be used while user is in game intro
        for event in pygame.event.get(): #this is called if user quits
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(backImg, [0, 0])#displays the background image onto screen
        pygame.image.load('space.jpg')# loads the background
        largeText = pygame.font.Font('font_one.ttf', 65)#font the background will be displayed in
        TextSurf, textRect = text_objects("Galaxy War", largeText)#this is what the title will say
        textRect.center = ((iDisplay_width/2),(iDisplay_height/2))
        gameDisplay.blit(TextSurf, textRect) #displays the text
        if Start.startgp == True or Start.startgp2 == True or Start.startgp3 == True: #checks wether the player has chosen easy, medium, or hard mode
            break
        
        
        # def button (msg, x,y,w,h,ic,ac):
        #buttons or options shown at menu
        startgp = button ("Easy",150,350,105,50,green,white,"Play") #button for playing easy mode
        button ("Exit",550,425,105,50,red,white,"Quit") #button for quitting the game mode
        button ("Medium",350,350,105,50,green,white,"Play2") #button for playing medium mode
        button ("Hard",550,350,105,50,green,white,"Play3") #button for playing hard mode
        button ("Random",150,425,105,50,blue,white,"Random") #button for randomly selecting mode
        button ("Story",350,425,105,50,blue,white,"Story") #button for looking at the story
        pygame.display.update() #updates screen
        clock.tick(15)

#the story funtion called to display context of game
def story():
    pygame.image.load('story.png')  #loads story image 
    screen.blit(storyImg, [150, 50]) #displays story image

#this is the character the user will be playing as
class user(pygame.sprite.Sprite): #using a sprite character
    def __init__(self):
        #this funtion defines how the user will appear onto the screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(playerImg, (iShip_width, iShip_height)) #the size of the player is set
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = iDisplay_width / 2
        self.rect.bottom = iDisplay_height - 10
        self.speedx = 0 #the speed is set to zero

    #these will set the keys the user needs to move
    def update(self):
        self.speedx = 0#the speed is set to zero
        self.speedy = 0#the speed is set to zero
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]: #if a is pressed the player will move left
            self.speedx = -8 #the players speed
        if keystate[pygame.K_d]: #if d is pressed the player will move right
            self.speedx = 8 #the players speed
        self.rect.x += self.speedx
        if keystate[pygame.K_w]: #if w is pressed the player will move up
            self.speedy = -8 #the players speed
        if keystate[pygame.K_s]: #if s is pressed the player will move down
            self.speedy = 8 #the players speed
        if keystate[pygame.K_p]: #key user will press to pause
            pause() #pause function is called
        self.rect.x += self.speedx #changes the speed
        self.rect.y += self.speedy #changes the speed
        if self.rect.right > iDisplay_width:
            self.rect.right = iDisplay_width
        if self.rect.left < 0:
            self.rect.left = 0

    #funtion for the user to shoot
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Crypter(pygame.sprite.Sprite): #these will set the easy enemies
    def __init__(self): #this funtion defines how the enemy will be displayed
        pygame.sprite.Sprite.__init__(self)
        self.image = alienImg #the image used for enemy
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(iDisplay_width - self.rect.width) #for where the aliens appear
        self.rect.y = random.randrange(-100, -40)
        #the speed of the enemy
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):#updates how the enemy will react and look like on screen
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > iDisplay_height + 10 or self.rect.left < -25 or self.rect.right > iDisplay_width + 20:
            self.rect.x = random.randrange(iDisplay_width - self.rect.width) #for where the aliens appear
            self.rect.y = random.randrange(-100, -40)
            #the speed of the enemy
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)

class Crypter2(pygame.sprite.Sprite):#these will set the medium enemies
    def __init__(self):#this funtion defines how the enemy will be displayed
        pygame.sprite.Sprite.__init__(self)
        self.image = alienImg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(iDisplay_width - self.rect.width)#for where the aliens appear
        self.rect.y = random.randrange(-100, -40)
        #the speed of the enemy
        self.speedy = random.randrange(15, 20)
        self.speedx = random.randrange(-10, 30)

    def update(self):#updates how the enemy will react and look like on screen
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > iDisplay_height + 10 or self.rect.left < -25 or self.rect.right > iDisplay_width + 20:
            self.rect.x = random.randrange(iDisplay_width - self.rect.width) #for where the aliens appear
            self.rect.y = random.randrange(-100, -40)
            #the speed of the enemy
            self.speedy = random.randrange(15, 20)
            self.speedx = random.randrange(-10, 30)
            
class Crypter3(pygame.sprite.Sprite):#these will set the hard enemies
    def __init__(self):#this funtion defines how the enemy will be displayed
        pygame.sprite.Sprite.__init__(self)
        self.image = alienImg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(iDisplay_width - self.rect.width) #for where the aliens appear
        self.rect.y = random.randrange(-100, -40)
        #the speed of the enemy
        self.speedy = random.randrange(25, 35)
        self.speedx = random.randrange(-20, 35)

    def update(self):#updates how the enemy will react and look like on screen
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > iDisplay_height + 10 or self.rect.left < -25 or self.rect.right > iDisplay_width + 20:
            self.rect.x = random.randrange(iDisplay_width - self.rect.width) #for where the aliens appear
            self.rect.y = random.randrange(-100, -40)
            #the speed of the enemy
            self.speedy = random.randrange(25, 35)
            self.speedx = random.randrange(-20, 35)            

class Bullet(pygame.sprite.Sprite):# this sets the bullets used for the user when he/she shoots
    #how the bullet will look like
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletImg #the bullets image is called
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10 #the speed of the bullets

    # updates the bullet on screen
    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

#the pause funtion is called using 'p'
def pause():
    paused = True #checks if pause is true
    #options that appear when on pause
    draw_text(screen, "Paused", 50, 400, 150) #displays what to press to continue, quit
    draw_text(screen, "R - Resume", 50, 400, 250)
    draw_text(screen, "Q - Quit", 50, 400, 350)
    pygame.display.update() #updates 
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: #use 'r' to resume
                    paused = False
                elif event.key == pygame.K_q: #use 'q' to quit game
                    pygame.quit()
                    quit()
        clock.tick(5)


all_sprites = pygame.sprite.Group() #assigns the characters to a variable
cryps = pygame.sprite.Group()#assigns the aliens to a variable
bullets = pygame.sprite.Group()#assigns the bullets to a variable
user = user() #user can be called instead of user()
all_sprites.add(user)

for i in range(8):
    m = Crypter()
    all_sprites.add(m)
    cryps.add(m)
    
def game_loop(): #the easy game loop funtion
    pygame.mixer.music.play(-1) #starts background music
    running = True
    iPoints = 0 # sets the score to zero
    while running:
        clock.tick(iFPS) #the FPS game will run on
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user quit, this will be called
                running = False #game closes 
            elif event.type == pygame.KEYDOWN:
                # the key used for user to deploy shots
                if event.key == pygame.K_SPACE: #use space to deploy shots
                    user.shoot()
                    pygame.mixer.music.stop() #stops background music
                    pygame.mixer.Sound.play(soundGun)#starts the gun sound effect
                    pygame.mixer.music.play(-1) #starts background music again

        all_sprites.update() #updates everything
        #detects when alien and bullet collide
        hits = pygame.sprite.groupcollide(cryps, bullets, True, True)
        for hit in hits:
            pygame.mixer.music.stop()# stops background music
            pygame.mixer.Sound.play(soundExplode) #plays soundeffect
            pygame.mixer.music.play(-1)#plays background music again
            iPoints = iPoints + 2 #adds on to points by 2
            m = Crypter()
            all_sprites.add(m)
            cryps.add(m)

        # detects when the user and alien collide
        hits = pygame.sprite.spritecollide(user, cryps, False, pygame.sprite.collide_circle_ratio(0.85))
        if hits:
            pygame.mixer.Sound.play(soundExplode) #plays explosion effect when player crashes and loses
            crash() #opens crashs funtion 
            running = False #stops the game

        screen.fill(black)
        screen.blit(backImg, backImg_rect) #displays background image
        all_sprites.draw(screen) #displays all characters
        draw_text(screen, str(iPoints), 18, 75, 0) #displays the points on upper left 
        pygame.display.flip() #flips everything
        

def game_loop2(): #the medium game loop funtion
    pygame.mixer.music.play(-1) #starts background music
    running = True
    iPoints = 0 # sets the score to zero
    while running:
        clock.tick(iFPS2) #the FPS game will run on
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#if user quit, this will be called
                running = False #game closes
            elif event.type == pygame.KEYDOWN:
                # the key used for user to deploy shots
                if event.key == pygame.K_SPACE: #use space to deploy shots
                    user.shoot()
                    pygame.mixer.music.stop() #stops background music
                    pygame.mixer.Sound.play(soundGun)#starts the gun sound effect
                    pygame.mixer.music.play(-1) #starts background music again

        all_sprites.update() #updates everything
        #detects when alien and bullet collide
        hits = pygame.sprite.groupcollide(cryps, bullets, True, True)
        for hit in hits:
            pygame.mixer.music.stop()# stops background music
            pygame.mixer.Sound.play(soundExplode) #plays soundeffect
            pygame.mixer.music.play(-1)#plays background music again
            iPoints = iPoints + 2 #adds on to points by 2
            m = Crypter2()
            all_sprites.add(m)
            cryps.add(m)

        # detects when the user and alien collide
        hits = pygame.sprite.spritecollide(user, cryps, False, pygame.sprite.collide_circle_ratio(0.85))
        if hits:
            pygame.mixer.Sound.play(soundExplode) #plays explosion effect when player crashes and loses
            crash() #opens crashs funtion 
            running = False #stops the game

        screen.fill(black)
        screen.blit(backImg, backImg_rect) #displays background image
        all_sprites.draw(screen) #displays all characters
        draw_text(screen, str(iPoints), 18, 75, 0) #displays the points on upper left 
        pygame.display.flip() #flips everything

def game_loop3(): #the hard game loop funtion
    pygame.mixer.music.play(-1) #starts background music
    running = True
    iPoints = 0# sets the score to zero
    while running:
        clock.tick(iFPS3) #the FPS game will run on
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#if user quit, this will be called
                running = False #game closes
            elif event.type == pygame.KEYDOWN:
                # the key used for user to deploy shots
                if event.key == pygame.K_SPACE: #use space to deploy shots
                    user.shoot()
                    pygame.mixer.music.stop() #stops background music
                    pygame.mixer.Sound.play(soundGun)#starts the gun sound effect
                    pygame.mixer.music.play(-1) #starts background music again

        all_sprites.update() #updates everything
        #detects when alien and bullet collide
        hits = pygame.sprite.groupcollide(cryps, bullets, True, True)
        for hit in hits:
            pygame.mixer.music.stop()# stops background music
            pygame.mixer.Sound.play(soundExplode) #plays soundeffect
            pygame.mixer.music.play(-1)#plays background music again
            iPoints = iPoints + 2 #adds on to points by 2
            m = Crypter3()
            all_sprites.add(m)
            cryps.add(m)

        # detects when the user and alien collide
        hits = pygame.sprite.spritecollide(user, cryps, False, pygame.sprite.collide_circle_ratio(0.85))
        if hits:
            pygame.mixer.Sound.play(soundExplode) #plays explosion effect when player crashes and loses
            crash() #opens crashs funtion 
            running = False #stops the game

        screen.fill(black)
        screen.blit(backImg, backImg_rect) #displays background image
        all_sprites.draw(screen) #displays all characters
        draw_text(screen, str(iPoints), 18, 75, 0) #displays the points on upper left 
        pygame.display.flip() #flips everything

#starts the game intro
game_intro()

#starts the game loops according to what is selected by user
if Start.startgp:
    game_loop()
if Start.startgp2:
    game_loop2()
if Start.startgp3:
    game_loop3()

#quit funtion
pygame.quit()
quit()
