import pygame

pygame.init() #initializes pygame and its modules

display_width = 800
display_height = 600

black = (0,0,0) #define colors via (R,G,B) levels
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width, display_height)) #sets display & obj
pygame.display.set_caption("Insert Caption Here")
clock = pygame.time.Clock() #clock object for game

spriteImg = pygame.image.load(r"C:\Users\jdcas\eclipse\workspace\game1\sprites\basic_sprite.png")

def sprite(x,y):
    gameDisplay.blit(spriteImg,(x,y))

x_position = 300
y_position = 250

x_change = 0


#-------------------------------------GAME LOOP---------------------------------------------
crashed = False

while not crashed:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            crashed = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                x_change = 0
    
    x_position += x_change
    
    gameDisplay.fill(white)
    sprite(x_position, y_position)
    
    pygame.display.update()
    clock.tick(60)
#-------------------------------------------------------------------------------------------  
pygame.quit()
quit()