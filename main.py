import time
from sys import exit

import pygame as pg
from stopwatch import Stopwatch

import calculations
import container
import draw
import minimax

pg.init()

dr = draw.DrawOnTheScreen()
calc = calculations.CalculateEv()
timer = Stopwatch().reset()


class Main(container.Container):
    def __init__(self):
        super().__init__()
        self._main()

    def _main(self):
        self.screen.fill((0, 0, 0))
        circles_not_temp = []
        crosses_not_temp = []
        grid_rects = dr.draw_the_grid()
        calc.create_map(grid_rects)
        while True:
            self._check_for_exit()
            self.clock.tick(self.FPS)
            timer.start()
            crosses = dr.draw_crosses(grid_rects, False, None)
            crosses_not_temp.append(crosses[0]) if crosses else crosses_not_temp
            crosses_not_temp = list(set(crosses_not_temp))
            circles_winner = calc.find_if_winning(True, self.rect_limit)
            crosses_winner = calc.find_if_winning(False, self.rect_limit)

            dr.draw_the_winning_five(crosses_winner, circles_winner, circles_not_temp, crosses_not_temp, grid_rects)
            calc.collect_info(circles_not_temp, crosses_not_temp)
            pg.display.update()
            if len(crosses_not_temp) == len(circles_not_temp):
                move = minimax.MiniMaxAi().find_best_move()
                if move is None:
                    print("No moves left")
                    time.sleep(3)
                    exit(0)
                circles_not_temp.append(move)
                dr.draw_circles(grid_rects, True, move)
                calc.has_blocked(self.str_map, False)

            pg.display.update()

    def _check_for_exit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(0)


if __name__ == "__main__":
    Main()
