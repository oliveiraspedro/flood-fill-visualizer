
import pygame
from floodfill.rendering.components.button import Button

COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)

class Panel:
    """
    Classe responsável por gerenciar os componentes do painel lateral.

    Contém os seletores de cores e o slider para controlar a velocidade.

    """ 
    def __init__(self, surface, window_width, window_height):
        self.surface = surface
        self.window_width = window_width
        self.window_height = window_height
        colored_button_size = 30
        colored_button_x = int((self.window_width * 2 / 3) + ((self.window_width / 3) / 2))
        colored_button_y = int((self.window_height / 2) - 30)
        self.red_button = Button(colored_button_x, colored_button_y, colored_button_size, colored_button_size, COLOR_RED)
        self.yellow_button = Button(colored_button_x + colored_button_size, colored_button_y, colored_button_size, colored_button_size, COLOR_YELLOW)
        self.blue_button = Button(colored_button_x + 2*colored_button_size, colored_button_y, colored_button_size, colored_button_size, COLOR_BLUE)
        self.selected_color = COLOR_RED

    def draw(self):
        self.red_button.draw(self.surface)
        self.yellow_button.draw(self.surface)
        self.blue_button.draw(self.surface)

    def get_selected_color(self):
        return self.selected_color 

    def handle_color_selection(self, x, y):
        if self.red_button.was_clicked(x, y):
            self.selected_color = COLOR_RED
        elif self.yellow_button.was_clicked(x, y):
            self.selected_color = COLOR_YELLOW
        elif self.blue_button.was_clicked(x, y):
            self.selected_color = COLOR_BLUE

    def handle_slider(self, x, y):
        pass

    def get_speed(self):
        pass