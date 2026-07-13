
import pygame

class Slider:
    def __init__(self, x: int, y: int, width: int, height: int, initial_val: float, min: int, max: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.slider_left_pos = self.x - (self.width//2)
        self.slider_right_pos = self.x + (self.width//2)
        self.slider_top_pos = self.y - (self.height//2)

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos-self.slider_left_pos)*initial_val # <- Porcentagem

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.width, self.height)
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, "darkgray", self.container_rect)
        pygame.draw.rect(surface, "blue", self.button_rect) 

    def move_slider(self, x, y):
        self.button_rect.centerx = x

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return (button_val/val_range)*(self.max-self.min)+self.min
