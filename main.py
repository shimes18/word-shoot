import pygame
import random

pygame.init()
clock= pygame.time.Clock()
screen = pygame.display.set_mode((400,600))

base= (0,460,400,300)
text=""

score=0

hp=100

color=(255,255,255)

font = pygame.font.Font(None,32)

bulletposition=(1000,1000)

wordy=0
wordy1,wordy2=0,0

second_word=False
third_word=False
game_over=False

bullety=400
bullety1=500

with open('words_alpha.txt') as f:
    words= [w for w in (line.strip() for line in f) if 3<= len(w) <= 10 ]

bullet = pygame.image.load("images/06.png").convert_alpha()
bullet = pygame.transform.scale(bullet,(15,15))

fps=30
flash=int(fps/4)
timer=10*fps
z=random.choice(words)
z1=random.choice(words)
z2=random.choice(words)


player = pygame.Rect(180,500,40,40)
running= True

while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                text = text[:-1]
                print(text)
            else:
                text += event.unicode
                print(text)

    if not game_over:
        timer+=1
        

        if (text.lower()==z):
            bullety=400
            z=random.choice(words)
            text=""
            score+=1
            shot=True
            
        if (text.lower()==z1):
            bullety1=500
            z1=random.choice(words)
            score+=1
            text=""
            shot=True

        if (text.lower()==z2):
            bullety=500
            z2=random.choice(words)
            score+=1
            text=""
            shot=True


        bullety-=30
        bulletposition = (300,bullety)

        wordy+=2

        if wordy>400:
            hp-=len(z)
            z=random.choice(words)
            wordy=0
            text=""
            print(hp)
            flash=int(fps/4)
            color=(255,0,0)
            
        if color==(255,0,0) and flash<0:
            color=(255,255,255)

        flash-=1

        if wordy1>500:
            hp-=len(z1)
            z1=random.choice(words)
            wordy1=0
            text=""
            color=(255,0,0)
            flash=int(fps/4)

            print(hp)

        if wordy2>500:
            hp-=len(z2)
            z2=random.choice(words)
            wordy2=0
            text=""
            color=(255,0,0)
            flash=int(fps/4)
            print(hp)


        if score>=5:
            wordy1+=2
            second_word=True
        if score>=15:
            wordy2+=2
            third_word=True

        if hp<=0:
            game_over=True


        if shot:
            wordy-=2
            wordy1-=2
            wordy2-=2


        
    screen.fill((20,20,20))
    pygame.draw.rect(screen,color,player)
    pygame.draw.arc(screen,(255,255,255),base,0,3.14159,5)
    playertext = font.render(text,True,(255,255,255))
    wordshow = font.render(z.capitalize(),True,(255,255,255))
    if second_word:
        wordshow1 = font.render(z1.capitalize(),True,(255,255,255))
        screen.blit(wordshow1,(20,wordy1))

    if third_word:    
        wordshow2 = font.render(z2.capitalize(),True,(255,255,255))
        screen.blit(wordshow2,(300,wordy2))

    screen.blit(wordshow,(165,wordy))
    screen.blit(bullet,bulletposition)

    screen.blit(playertext,(160,550))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()