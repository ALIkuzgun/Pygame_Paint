import pygame

class Cell:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rect = pygame.Rect(self.x * self.size, self.y * self.size, self.size, self.size)

    def draw(self):
        pygame.draw.rect(ekran, self.color, self.rect)
        pygame.draw.rect(ekran, (100, 100, 100), self.rect, 1)

pygame.init()

width, height = 700, 480
ekran = pygame.display.set_mode((width, height))
pygame.display.set_caption('Paint App')

cell_size = 24
cells = [Cell(x, y, cell_size, (255, 255, 255)) for y in range(20) for x in range(20)]

red_rect = pygame.Rect(550,70,24,24)
green_rect = pygame.Rect(550,110,24,24)
darkblue_rect = pygame.Rect(550,150,24,24)
yellow_rect = pygame.Rect(550,190,24,24)
pink_rect = pygame.Rect(590,70,24,24)
blue_rect = pygame.Rect(590,110,24,24)
black_rect = pygame.Rect(590,150,24,24)
brown_rect = pygame.Rect(590,190,24,24)
red,green,darkblue,yellow,pink,blue,black,brown = 0,0,0,0,0,0,0,0

def colors():
    font = pygame.font.Font('Jersey10-Regular.ttf',50)
    text = font.render('Colors',True,(0,0,0))
    ekran.blit(text,(530,15))
    pygame.draw.rect(ekran, (255,0,0), (550,70,24,24))
    pygame.draw.rect(ekran, (0,255,0), (550,110,24,24))
    pygame.draw.rect(ekran, (0,0,255), (550,150,24,24))
    pygame.draw.rect(ekran, (255,255,0), (550,190,24,24))
    pygame.draw.rect(ekran, (255,0,255), (590,70,24,24))
    pygame.draw.rect(ekran, (0,255,255), (590,110,24,24))
    pygame.draw.rect(ekran, (0,0,0), (590,150,24,24))
    pygame.draw.rect(ekran, (150,75,0), (590,190,24,24))

clear_rect = pygame.Rect(536,320,102,40)
def clear():
    font = pygame.font.Font('Jersey10-Regular.ttf',54)
    text = font.render('Clear',True,(0,0,0))
    pygame.draw.rect(ekran, (100,100,100), (536,320,102,40))
    ekran.blit(text,(540,310))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for cell in cells:
                if event.button == 1:
                    if cell.rect.collidepoint(mouse_pos):   
                        if red == 1:
                          cell.color = (255,0,0)
                        if green == 1:
                          cell.color = (0,255,0)   
                        if darkblue == 1:
                          cell.color = (0,0,255)
                        if yellow == 1:
                          cell.color = (255,255,0)
                        if pink == 1:
                          cell.color = (255,0,255)
                        if blue == 1:
                          cell.color = (0,255,255)
                        if black == 1:
                          cell.color = (0,0,0)
                        if brown == 1:
                          cell.color = (150,75,0)

                    if clear_rect.collidepoint(mouse_pos):   
                       cell.color = (255,255,255)

                if event.button == 3:
                    if cell.rect.collidepoint(mouse_pos):   
                        cell.color = (255,255,255)

                if red_rect.collidepoint(mouse_pos):   
                    red,green,darkblue,yellow,pink,blue,black,brown = 1,0,0,0,0,0,0,0
                if green_rect.collidepoint(mouse_pos):   
                    red,green,darkblue,yellow,pink,blue,black,brown = 0,1,0,0,0,0,0,0
                if darkblue_rect.collidepoint(mouse_pos): 
                    red,green,darkblue,yellow,pink,blue,black,brown = 0,0,1,0,0,0,0,0
                if yellow_rect.collidepoint(mouse_pos): 
                    red,green,darkblue,yellow,pink,blue,black,brown = 0,0,0,1,0,0,0,0
                if pink_rect.collidepoint(mouse_pos): 
                    red,green,darkblue,yellow,pink,blue,black,brown = 0,0,0,0,1,0,0,0
                if blue_rect.collidepoint(mouse_pos): 
                    red,green,darkblue,yellow,pink,blue,black,brown = 0,0,0,0,0,1,0,0
                if black_rect.collidepoint(mouse_pos): 
                    red,green,darkblue,yellow,pink,blue,black,brown = 0,0,0,0,0,0,1,0
                if brown_rect.collidepoint(mouse_pos): 
                    red,green,darkblue,yellow,pink,blue,black,brown = 0,0,0,0,0,0,0,1

    ekran.fill((255, 255, 255))
    colors()
    clear()
    for cell in cells:
        cell.draw()
    pygame.display.flip()

pygame.quit()