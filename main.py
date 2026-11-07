import pygame
import random

pygame.init()
clock= pygame.time.Clock()
screen = pygame.display.set_mode((400,600))

base= (0,460,400,300)
text=""

score=0

time=0

hp=100

color=(255,255,255)

font = pygame.font.Font(None,32)

bulletposition=(1000,1000)

bulletx=1000
a=50

x=1

explosionx=1000
explosiony=1000

shot=False
shot1=False
shot2=False
shot3=False

wordy=50
wordy1,wordy2=50,50

second_word=False
third_word=False
game_over=False

bullety=4000

shotsound= pygame.mixer.Sound("sounds/shot.ogg")
shotsound.set_volume(0.5)

with open('words_alpha.txt') as f:
    words= [w for w in (line.strip() for line in f) if 3<= len(w) <= 10 ]

bullet = pygame.image.load("images/06.png").convert_alpha()
bullet = pygame.transform.scale(bullet,(30,30))

explosion = pygame.image.load("images/explosion.png").convert_alpha()
explosion = pygame.transform.scale(explosion,(20,60))

ship = pygame.image.load("images/ship.png").convert_alpha()
ship = pygame.transform.scale(ship,(150,400))
ship = pygame.transform.rotate(ship,90)

etimer=0

fps=30
flash=int(fps/4)
timer=10*fps
z=random.choice(words)
z1=random.choice(words)
z2=random.choice(words)


player = pygame.Rect(180,500,50,50)
hpbar = pygame.Rect(0,0,20,hp*2)

hpcolor=(0, 128, 0)

running= True

while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

        if game_over and event.type==pygame.KEYDOWN and event.key==pygame.K_r:
            hp=100
            z=random.choice(words)
            z1=random.choice(words)
            z2=random.choice(words)
            bulletposition=(1000,1000)

            bulletx=1000
            a=50

            shot=False
            shot1=False
            shot2=False
            shot3=False

            wordy=50
            wordy1,wordy2=50,50

            second_word=False
            third_word=False
            game_over=False

            bullety=4000

            score=0

            time=0
            text=""
            hpcolor=(0, 128, 0)          
            game_over=False

    if not game_over:
        timer+=1
        

        if (text.lower()==z):
            bullety=400
            bulletx=200
            text=""
            a=1
            score+=1
            shotsound.play()
            shot=True
            
        if (text.lower()==z1):
            bullety=400
            bulletx=50
            score+=1
            text=""
            shotsound.play()
            a=2
            shot=True

        if (text.lower()==z2):
            bullety=400
            bulletx=350
            score+=1
            text=""
            shotsound.play()
            a=3
            shot=True


        bulletposition = (bulletx,bullety)

        wordy+=2

        if wordy>400:
            hp-=len(z)
            z=random.choice(words)
            wordy=50
            text=""
            flash=int(fps/4)
            color=(255,0,0)
            
        if color==(255,0,0) and flash<0:
            color=(255,255,255)

        flash-=1

        if wordy1>400:
            hp-=len(z1)
            z1=random.choice(words)
            wordy1=50
            text=""
            color=(255,0,0)
            flash=int(fps/4)


        if wordy2>400:
            hp-=len(z2)
            z2=random.choice(words)
            wordy2=50
            text=""
            color=(255,0,0)
            flash=int(fps/4)



        if score>=5:
            wordy1+=2
            second_word=True
        if score>=15:
            wordy2+=2
            third_word=True

        if hp<=90:
            text=""
            time=(timer/fps-10)
            game_over=True

        if hp<=70 and hp>30:
            hpcolor=(255,165,0)

        if hp<=30:
            hpcolor=(255,0,0)

        if shot:
            bullety-=20
            if a==1:
                wordy-=2
            elif a==2:
                wordy1-=2
            elif a==3:
                wordy2-=2


        if bullety<=wordy1 or bullety<=wordy2 or bullety<=wordy:
            explosionx=bulletx
            explosiony=bullety
            etimer=5
            bullety=1000
            bulletposition= (1000,bullety)
            shot=False
            if a==1:
                shot1=True
            if a==2:
                shot2=True
            if a==3:
                shot3=True

        if shot1:
            z=random.choice(words)
            wordy=50
            shot1=False
        if shot2:            
            z1=random.choice(words)
            wordy1=50
            shot2=False
        if shot3:
            wordy2=50
            z2=random.choice(words)
            shot3=False


    screen.fill((20,20,20))
    scoret = font.render("Score: " + str(score),True,(255,255,255))
    screen.blit(scoret,(150,30))
    if not game_over:
        hpt= font.render(str(hp),True,(255,255,255))
        screen.blit(hpt,(2*hp+20,0))
        hpbar = pygame.Rect(0,0,hp*2,20)   
        screen.blit(ship,(0,460))
        pygame.draw.rect(screen,hpcolor,hpbar)
        playertext = font.render(text,True,(255,255,255))
        wordshow = font.render(z.capitalize(),True,(255,255,255))
        if second_word:
            wordshow1 = font.render(z1.capitalize(),True,(255,255,255))
            screen.blit(wordshow1,(20,wordy1))

        if third_word:    
            wordshow2 = font.render(z2.capitalize(),True,(255,255,255))
            screen.blit(wordshow2,(280,wordy2))

        if etimer>0:
            x+=0.1
            etimer-=1
            explosion = pygame.transform.scale(explosion,(60*x,20))
            screen.blit(explosion,(explosionx,explosiony))
        if etimer==0:
            x=1
        screen.blit(wordshow,(165,wordy))
        
    bulletposition = list(bulletposition)
    if game_over:
        wpm = font.render("Your word per minute",True,(255,255,255))
        wpm2= font.render("  was: " + str(score/time*60)[0:5],True,(255,255,255))
        pressc=font.render("PRESS R TO PLAY AGAIN",True,(255,255,255))

        screen.blit(wpm, (80,250))
        screen.blit(pressc, (80,350))
        screen.blit(wpm2, (130,300))
    screen.blit(bullet,bulletposition)
    screen.blit(bullet,[bulletposition[0]+30,bulletposition[1]])
    screen.blit(bullet,[bulletposition[0]-30,bulletposition[1]])

    screen.blit(playertext,(160,550))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
