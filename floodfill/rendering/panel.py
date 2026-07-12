
import pygame
from floodfill.rendering.components.button import Button

class Panel:
    def __init__(self, surface):
        self.surface = surface

    def draw(self):
        color_selector_button = Button(640, 360, 100, 100)
        Button.draw(color_selector_button, self.surface)

    def get_selected_color(self):
        pass

    def handle_color_selection(self):
        pass

    def handle_slider(self, x, y):
        pass

    def get_speed(self):
        pass