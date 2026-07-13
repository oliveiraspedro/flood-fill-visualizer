
import pygame

class Button:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def was_clicked(self, x, y):
        if self.rect.collidepoint(x, y):
            print(f"Color {self.color}")
            return True
    
