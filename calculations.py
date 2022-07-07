import contextlib

import numpy as np

import container


class CalculateEv(container.Container):
    def __init__(self):
        super().__init__()

    def create_map(self, grid_rects, return_map=False):
        for rect in grid_rects:
            self.str_map.append('x')

    def replace_in_map(self, index, char):
        self.str_map[index] = char

    def check_if_circle_winning(self):
        diag_score = 0
        row_score = 0
        col_score = 0
        idx_bac = None
        for idx, x in enumerate(self.str_map):
            if x == 'ci':
                if row_score == 1 and idx_bac is None:
                    if self.str_map[idx - 1] == 'ci':
                        idx_bac = idx - 1
                if row_score == 4 and idx - 4 == idx_bac:
                    return True
                row_score += 1
                if self.str_map[idx + self.rects_in_row + 1] == 'ci' or self.str_map[idx + \
                                                                                     self.rects_in_row - 1] == 'ci':
                    diag_score += 1
                if self.str_map[idx + self.rects_in_row] == 'ci':
                    col_score += 1
            if diag_score == 4 or diag_score == 4 or col_score == 4:
                return True
        else:
            return False

    def check_if_crooss_winning(self):
        diag_score = 0
        row_score = 0
        col_score = 0
        idx_bac = None
        for idx, x in enumerate(self.str_map):
            if x == 'cr':
                idx_bac = idx if idx_bac is None else idx_bac
                if row_score == 4 and idx - 4 == idx_bac:
                    return True
                row_score += 1
                if self.str_map[idx + self.rects_in_row + 1] == 'cr' or self.str_map[idx + \
                                                                                     self.rects_in_row - 1] == 'ci':
                    diag_score += 1
                if self.str_map[idx + self.rects_in_row] == 'cr':
                    col_score += 1
            if diag_score == 4 or diag_score == 4 or col_score == 4:
                return True

        else:
            return False

    def find_if_winning(self, circle_or_cross, limit_minus_one, *args, return_indexes=False):

        char = 'ci' if circle_or_cross else 'cr'
        found_str = []
        str_map_2 = ''
        try:
            str_map_2 = args[0]
        except IndexError:
            str_map_2 = self.str_map

        indexes = list(map(lambda x: x[0], enumerate(str_map_2)))
        player_indexes = [x for x in indexes if str_map_2[x] == char]
        indexes_matrix = np.array(indexes)
        indexes_matrix = indexes_matrix.reshape(self.rects_in_column, self.rects_in_row)
        winning_poses = []
        if not player_indexes:
            return False

        # save all diagonals to variable diagonals and use k=1 and k=2 len of row
        diagonals = []
        for k in range(0, self.rects_in_row):
            if len(np.diag(indexes_matrix, k)) > limit_minus_one - 1 or len(
                    np.diag(np.fliplr(indexes_matrix), k)) > limit_minus_one - 1:
                diagonals.append(np.diag(indexes_matrix, k))
                diagonals.append(np.diag(np.fliplr(indexes_matrix), k))

        columns = indexes_matrix.T

        for element in [indexes_matrix, columns, diagonals]:
            for y in element:
                if sum(str_map_2[x] == char for x in y) > limit_minus_one - 1:
                    if return_indexes:
                        return y
                    return True


    def collect_info(self, circles, crosses):
        self.circles_on_the_screen = len(circles)
        self.crosses_on_the_screen = len(crosses)

    def has_blocked(self, board, circle_or_cross):
        if not self.find_if_winning(circle_or_cross, 2, board):
            return False
        char = 'ci' if circle_or_cross else 'cr'
        enemy_char = "cr" if char == "ci" else "ci"

        matrix = np.array(board)
        matrix = matrix.reshape(self.rects_in_column, self.rects_in_row)
        enemy_indexes = np.where(matrix == enemy_char)
        # x_es = [x[0] for x in enemy_indexes]
        # y_es = [x[1] for x in enemy_indexes]
        enemy_indexes = [[x, y] for x, y in zip(enemy_indexes[0], enemy_indexes[1])]
        # my_indexes = np.where(matrix == char)
        for enemy_idx in enemy_indexes:
            # print(enemy_idx[0])
            try:
                if matrix[enemy_idx[0]][enemy_idx[1] + 1] == char:
                    return True
            except IndexError:
                pass
            if matrix[enemy_idx[0]][enemy_idx[1] - 1] == char:
                return True
            try:
                if matrix[enemy_idx[0] + 1][enemy_idx[1]] == char:
                    return True
            except IndexError:
                pass

            if matrix[enemy_idx[0] - 1][enemy_idx[1]] == char:
                return True
        return False

        # Check if one player is blocking another
