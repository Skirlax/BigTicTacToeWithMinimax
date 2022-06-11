import copy
import time

import draw
from sys import exit
import pygame as pg
import container
import handle_input
from stopwatch import Stopwatch
import calculations
import play_with_me_tree
from time import sleep

import test

pg.init()

dr = draw.DrawOnTheScreen()
calc = calculations.CalculateEv()
hi = handle_input.InputHandler()
timer = Stopwatch().reset()


class MainRun(container.PropContainer):
    def __init__(self):
        super().__init__()

    def run_it_all(self):
        self.screen.fill((0,0,0))

        # pg.display.update()
        # sleep(3)
        # play_with_ai = hi.get_input()
        circles_not_temp = []
        crosses_not_temp = []
        grid_rects = dr.draw_the_grid()
        calc.create_map(grid_rects)
        run_ai = True


        while True:
            self.check_for_exit()
            self.clock.tick(self.FPS)
            timer.start()
            # circles = dr.draw_circles(grid_rects, False, None)
            # circles_not_temp.append(circles[0]) if circles else circles_not_temp
            crosses = dr.draw_crosses(grid_rects, False, None)
            crosses_not_temp.append(crosses[0]) if crosses else crosses_not_temp
            crosses_not_temp = list(set(crosses_not_temp))
            # winner_circle = calc.check_if_circle_winning()
            # winner_cross = calc.check_if_crooss_winning()
            circles_winner = calc.find_if_winning(True, 5)
            crosses_winner = calc.find_if_winning(False, 5)
            dr.draw_the_winning_five(crosses_winner, circles_winner, circles_not_temp, crosses_not_temp, grid_rects)
            calc.collect_info(circles_not_temp, crosses_not_temp)
            if len(crosses_not_temp) > len(circles_not_temp):
                # print(crosses_not_temp[0])
                # if circles_not_temp:
                #     first_circle = circles_not_temp[-1]
                # else:
                #     first_circle = None
                # print(first_circle)
                score,move = play_with_me_tree.MiniMaxAi().minimax(copy.deepcopy(self.str_map), "ci",True, 2, -1000, 1000)
                print(score)
                play_with_me_tree.MiniMaxAi().set_score(score)

                # print(move)
                circles = dr.draw_circles(grid_rects, True, move)
                circles_not_temp.append(circles[0]) if circles else circles_not_temp

            pg.display.update()

    def check_for_exit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(0)

        

mr = MainRun()
mr.run_it_all()
