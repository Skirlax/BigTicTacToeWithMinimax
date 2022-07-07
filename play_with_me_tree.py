import copy

import calculations
import container

calc = calculations.CalculateEv()


class MiniMaxAi(container.PropContainer):
    def __init__(self):
        super().__init__()

    def get_possible_moves(self, board):
        # opp_player = 's'
        # possible_moves = []
        # temp_board = copy.deepcopy(board)
        # if move is not None and temp_board[move] == 'x':
        #     temp_board[move] = player
        return [index for index, x in enumerate(board) if x == 'x']
        # if pos is not None:
        #     board[pos] = opp_player
        # for index, x in enumerate(temp_board):
        #     if temp_board[index] == 'x':
        #         possible_moves.append(index)

        # possible_moves_temp = possible_moves[move - (self.rects_in_row * 2) - 1:move + (self.rects_in_row * 2) + 1]
        # do_continue = False
        # last_rel_index = 0
        # stops = [x for x in range(4,4 +(5 * 18) + 1, 18)]
        # possible_moves_temp_temp = copy.deepcopy(possible_moves_temp)
        # for index,pos_move in enumerate(possible_moves_temp_temp):
        #     if (last_rel_index + self.rects_in_row) - 4 == index:
        #         do_continue = False
        #     if do_continue:
        #         possible_moves_temp.remove(pos_move)
        #         continue
        #
        #     if index in stops:
        #         do_continue = True
        #         last_rel_index = index

        # return possible_moves

    def calculate_score(self, current_board):
        score = 0
        opponent_score = 0

        # score_circle = 0
        # score_cross = 0
        #
        # if calc.find_if_winning(False, 5, current_board):
        #     return -800
        # if calc.find_if_winning(True, 5, current_board):
        #     return 800
        # if calc.find_if_winning(False, 4, current_board):
        #     score_cross -= 400
        #
        # if calc.find_if_winning(False, 3, current_board):
        #     score_cross -= 200
        #
        # if calc.find_if_winning(True, 4, current_board):
        #     score_circle += 300
        # if calc.find_if_winning(True, 3, current_board):
        #     score_circle += 100
        #
        # return score_circle - score_cross
        for y in range(2, 6):
            if calc.find_if_winning(True, y, current_board):
                score += y
            if calc.find_if_winning(False, y, current_board):
                opponent_score += y

        # if calc.has_blocked(has_blocked_board, player):
        #     score += 10

        return score - opponent_score

    def find_best_move(self):
        bestScore = -1000
        bestMove = None
        copy_board = copy.deepcopy(self.str_map)

        for move in self.get_possible_moves(self.str_map):
            copy_board[move] = "ci"
            score = self.minimax(False, 4, copy_board)
            copy_board[move] = "x"
            if score > bestScore:
                bestScore = score
                bestMove = move

        return bestMove

    def minimax(self, is_max, depth, board, alpha=-1000, beta=1000):
        if calc.find_if_winning(False, self.rect_limit, board):
            return -20

        if calc.find_if_winning(True, self.rect_limit, board):
            return 20

        if len(self.get_possible_moves(board)) == 0 or depth == 0:
            return 0

        scores = []
        for move in self.get_possible_moves(board):
            board[move] = "ci" if is_max else "cr"
            scores.append(self.minimax(not is_max, depth - 1, board, alpha, beta))
            board[move] = "x"

            if is_max:
                if scores[-1] >= beta:
                    return max(scores)

                alpha = max(alpha, scores[-1])

            else:
                if scores[-1] <= alpha:
                    return min(scores)

                beta = min(beta, scores[-1])

        return max(scores) if is_max else min(scores)


