import copy

import calculations
import container

calc = calculations.CalculateEv()


class MiniMaxAi(container.Container):
    def __init__(self):
        super().__init__()

    def get_possible_moves(self, board):
        return [index for index, x in enumerate(board) if x == 'x']

    def calculate_score(self, current_board):
        score = 0
        opponent_score = 0

        for y in range(2, 6):
            if calc.find_if_winning(True, y, current_board):
                score += y
            if calc.find_if_winning(False, y, current_board):
                opponent_score += y

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


