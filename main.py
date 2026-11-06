import pygame

pygame.init()
clock= pygame.time.Clock()
screen = pygame.display.set_mode((400,600))

base= (0,460,400,300)
text=""

font = pygame.font.Font(None,32)

words=["hello","apple","onomotopiea","return","sleep"]

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



    screen.fill((20,20,20))
    pygame.draw.rect(screen,(255,255,255),player)
    pygame.draw.arc(screen,(255,255,255),base,0,3.14159,5)
    pygame.display.flip()
    
pygame.quit()