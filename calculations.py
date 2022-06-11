import container
import re


class CalculateEv(container.PropContainer):
    def __init__(self):
        super().__init__()

    def create_map(self, grid_rects):
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

    def find_if_winning(self, circle_or_cross, limit_minus_one, *args):



        if circle_or_cross:
            char = 'ci'
        else:
            char = 'cr'
        found_str = []
        str_map_2 = ''
        try:
            str_map_2 = args[0]
        except IndexError:
            str_map_2 = self.str_map

        indexes = list(map(lambda x: x[0],enumerate(str_map_2)))
        player_indexes = [x for x in indexes if str_map_2[x] == char]
        winning_poses = []
        for x in indexes:
            try:
                winning_poses.extend([list(range(x, x + ((5) * (self.rects_in_row + 1)), self.rects_in_row + 1))])
                winning_poses.extend([list(range(x, x + ((5) * (self.rects_in_row - 1)), self.rects_in_row - 1))])
                winning_poses.extend([list(range(x, x + ((5) * self.rects_in_row), self.rects_in_row))])
                winning_poses.extend([list(range(x, x + 5))])
            except IndexError:
                pass

        # index = 0
        # player_indexes_sliced = []
        # while index + 4 < len(player_indexes):
        #     player_indexes_sliced.extend([player_indexes[index:index + 5]])
        #     index += 5
        # if len(player_indexes) > 5:
        #     player_indexes = player_indexes_sliced

        for x in winning_poses:
            counter = 0
            for y in x:
                if y in sorted(player_indexes):
                    counter += 1
            if counter == limit_minus_one:
                return True








        # pattern_one = char * (limit_minus_one + 1)
        # found_str.append(re.search(pattern_one, str_map_2))
        # count_of_diags_plus = 0
        # count_of_cols = 0
        # count_of_diags_minus = 0
        # different_chars = 0
        # for idx, x in enumerate(str_map_2):
        #     if x == char and found_str[0] is None:
        #         different_chars += 1
        #         if different_chars == 1:
        #             continue
        #         if str_map_2[idx - (self.rects_in_row + 1)] == char:
        #             count_of_diags_plus += 1
        #         if str_map_2[idx - (self.rects_in_row - 1)] == char:
        #             count_of_diags_minus += 1
        #         if str_map_2[idx - self.rects_in_row] == char:
        #             count_of_cols += 1
        #     if count_of_diags_plus == limit_minus_one or count_of_diags_minus == limit_minus_one or count_of_cols == limit_minus_one:
        #         return True
        #
        # if found_str[0] is not None:
        #     return True
        # else:
        #     return False

    def collect_info(self, circles, crosses):
        self.circles_on_the_screen = len(circles)
        self.crosses_on_the_screen = len(crosses)
