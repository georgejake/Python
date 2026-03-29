import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,1000))            
        self.surface.fill((157, 186, 102))
    def run(self):
        snake = Snake(self.surface)        
        snake.draw_block()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                       running = False
                       break
                    if event.key == K_UP:
                       snake.move_up()                       
                    if event.key == K_DOWN:                       
                       snake.move_down()
                    if event.key == K_RIGHT:
                       snake.move_right()
                    if event.key == K_LEFT:
                       snake.move_left()                    
                        
                elif event.type == QUIT:
                    running = False

    

    

class Snake:
    def __init__(self,surface):        
        self.path = r"C:\George\Technical\Python\poetry_codes\snake_game\src\snake_game\resources\block.jpg"    
        self.block = pygame.image.load(self.path).convert()
        self.x = 0
        self.y = 0
        self.parent_surface = surface
    def move_left(self):
        self.x -= 10
        self.draw_block()
    def move_right(self):
        self.x += 10
        self.draw_block()
    def move_up(self):
        self.y -= 10
        self.draw_block()
    def move_down(self):
        self.y += 10
        self.draw_block()
    def draw_block(self):
        self.parent_surface.fill((157, 186, 102))        
        self.parent_surface.blit(self.block,(self.x,self.y))
        pygame.display.flip()
    




if __name__=="__main__":

    game = Game()
    game.run()

       
    
    

    
    
    
                

    


