import pygame as pg

pg.init()


class PropContainer:
    scr_width = 1800
    rect_size = 100
    scr_height = 900
    screen = pg.display.set_mode([scr_width, scr_height])
    color_white = (255, 255, 255)
    color_red = (255, 0, 0)
    color_blue = (0, 0, 255)
    color_yellow = (255,255,0)
    color_green = (0, 255, 0)
    clock = pg.time.Clock()
    FPS = 60
    str_map = []
    circles_on_the_screen = 0
    crosses_on_the_screen = 0
    end_count = 5
    rects_in_row = scr_width // rect_size
    rects_in_column = scr_height // rect_size
    grid_rects_count = rects_in_column * rects_in_row
    ai_control_list = list(range(grid_rects_count + 1))
    game_won_by_circles = False
    circles_won_the_game_times = 0
    game_won_by_crosses = False
    crosses_won_the_game_times = 0
    active_rect_cross = pg.Rect(0,0,100,100)
    active_rect_circle = pg.Rect(0,0,100,100)

