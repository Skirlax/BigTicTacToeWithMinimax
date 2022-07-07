import pygame as pg
import container

pg.init()


class HandleMouse(container.Container):
    def __init__(self):
        super().__init__()

    def check_mouse_pos(self, given_rect):
        return bool(given_rect.collidepoint(pg.mouse.get_pos()))

    def check_button_clicked(self, button_index):
        button = pg.mouse.get_pressed()
        return bool(button[button_index] and pg.MOUSEBUTTONDOWN)
