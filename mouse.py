import pygame as pg
import container

pg.init()


class HandleMouse(container.PropContainer):
    def __init__(self):
        super().__init__()

    def check_mouse_pos(self, given_rect):
        if given_rect.collidepoint(pg.mouse.get_pos()):
            return True
        else:
            return False

    def check_button_clicked(self, button_index):
        button = pg.mouse.get_pressed()
        if button[button_index] and pg.MOUSEBUTTONDOWN:
            return True
        else:
            return False
