import pygame
import time
import random
from os import path


bg=path.join(path.dirname(__file__),'sound')
pygame.init()
pygame.mixer.init()
background = (255,213,213)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
yellow = (255,255,0)
golden = (255,215,0)
brown = (165,42,42)
display_width = 800
display_height =600
gameDisplay = pygame.display.set_mode((display_width,display_height))

out=pygame.mixer.Sound("dead2.wav")
gain=pygame.mixer.Sound("point.wav")

pygame.display.set_caption('SNAKE_GAME')
clock = pygame.time.Clock()
block_size = 20
FPS = 15
cp1=cp2=cp3=[0,0]
pp1=pp2=pp3=[0,0]

smallfont = pygame.font.SysFont(None,25)
medfont = pygame.font.SysFont(None,50)
largefont = pygame.font.SysFont(None,75)
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Paused",
                           black,
                           -100,
                            size=2
                          )
        message_to_screen("Press c to continue and q to quit.",
                            blue,
                           25,
                           size=1
                          )
        pygame.display.update()
        clock.tick(15)
        

def text_objects(text,color,size):
    if size==0:
        textSurface=smallfont.render(text,True,color)
    elif size==1:
        textSurface=medfont.render(text,True,color)
    elif size==2:
        textSurface=largefont.render(text,True,color)
        
    return textSurface,textSurface.get_rect()


def message_to_screen(msg,color, y_displace=0,size=0):
    textSurf,textRect =text_objects(msg,color,size)
    textRect.center=(display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)
    
def go_screen():
    intro =True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type ==pygame.KEYDOWN:
                if event.key== pygame.K_c:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(background)
        message_to_screen("SNAKE_GAME",red,-100,size=2)
        message_to_screen("Eat before it Disappears",black,20,size=1)
        message_to_screen("Press C to play or Q to quit and p to pause ",black,60,size=0)
        pygame.display.update()
        clock.tick(15)

def score (score):
    text=medfont.render("score: "+str(score),True, background)
    gameDisplay.blit(text,[0,0])



pygame.mixer.music.load(path.join(bg,'background.wav'))
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(loops=-1)




def gameloop():
    img = pygame.image.load("frame1.jpg").convert_alpha()
    gameExit = False
    gameOver = False
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change = 0
    lead_y_change = 0
    
    randredX = round(random.randrange(0,display_width-block_size)/20.0)*20.0
    randredY = round(random.randrange(0,display_height-block_size)/20.0)*20.0
    randgreenX = round(random.randrange(0,display_width-block_size)/20.0)*20.0
    randgreenY = round(random.randrange(0,display_height-block_size)/20.0)*20.0
    randblueX = round(random.randrange(0,display_width-block_size)/20.0)*20.0
    randblueY = round(random.randrange(0,display_height-block_size)/20.0)*20.0


    ct=0
    scr=0
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(background)
            
            message_to_screen("GAME OVER",red,-50,size=2)
            #message_to_screen("Your Score: ",blue,-30,size=1)
            message_to_screen("Press C to play again or Q to quit ",black,50,size=1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameloop()
                    if event.key == pygame.K_p:
                        pause()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                if event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                if event.key == pygame.K_p:
                    pause()
        if lead_x >=display_width or lead_x <=0:
            pygame.mixer.Sound.play(out)
            gameOver = True
        if lead_y >=display_height or lead_y <=0:
            pygame.mixer.Sound.play(out)
            gameOver = True
        

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(background)
        gameDisplay.blit(img,(0,0))
        if(ct%20==0):
            randredX = round(random.randrange(0,display_width-2*block_size)/20.0)*20.0
            randredY = round(random.randrange(0,display_height-2*block_size)/20.0)*20.0
        pygame.draw.rect(gameDisplay,red,[randredX,randredY,block_size,block_size])
        if(ct%40==0):
            randgreenX = round(random.randrange(0,display_width-2*block_size)/20.0)*20.0
            randgreenY = round(random.randrange(0,display_height-2*block_size)/20.0)*20.0
        pygame.draw.rect(gameDisplay,green,[randgreenX,randgreenY,block_size,block_size])
        if(ct%60==0):
            randblueX = round(random.randrange(0,display_width-2*block_size)/20.0)*20.0
            randblueY = round(random.randrange(0,display_height-2*block_size)/20.0)*20.0
        pygame.draw.rect(gameDisplay,blue,[randblueX,randblueY,block_size,block_size])
        
        pygame.draw.rect(gameDisplay,brown,[100,500,200,20])
        pygame.draw.rect(gameDisplay,brown,[300,200,200,20])
        pygame.draw.rect(gameDisplay,golden,[lead_x,lead_y,block_size,block_size])
        if lead_x >=100 and lead_x + block_size <=300 and lead_y>=500 and lead_y +block_size <=520:
            pygame.mixer.Sound.play(out)
            gameOver = True
        if lead_x >=300 and lead_x + block_size <=500 and lead_y>=200 and lead_y +block_size <=220:
            pygame.mixer.Sound.play(out)
            gameOver = True
        


        score(scr)
        
        pygame.display.update()
        if lead_x == randredX and lead_y == randredY:
             randredX = round(random.randrange(0,display_width-block_size)/20.0)*20.0
             randredY = round(random.randrange(0,display_height-block_size)/20.0)*20.0
             pygame.mixer.Sound.play(gain)
             scr=scr+15
        if lead_x == randgreenX and lead_y == randgreenY:
             randgreenX = round(random.randrange(0,display_width-block_size)/20.0)*20.0
             randgreenY = round(random.randrange(0,display_height-block_size)/20.0)*20.0
             pygame.mixer.Sound.play(gain)
             scr=scr+10
        if lead_x == randblueX and lead_y == randblueY:      
             randblueX = round(random.randrange(0,display_width-block_size)/20.0)*20.0
             randblueY = round(random.randrange(0,display_height-block_size)/20.0)*20.0
             pygame.mixer.Sound.play(gain)
             scr=scr+5
        
            
            
        ct=ct+1
        clock.tick(FPS)
    pygame.quit()
    quit()
go_screen()
gameloop()
