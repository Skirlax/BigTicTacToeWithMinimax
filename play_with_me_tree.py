import copy

import calculations
import container

# 1. Get all possible moves
# 2. Get all possible moves for each move to the depth of 4 or 3
# 2. Calculate the score for each move
# 3. Choose the move with the highest score
# 4. Implement alpha beta pruning

# We are going to calculate the score based on how far away our next move is from the previous move.

# Methods:
# Copy of the map board (deep copy)
# Calculate the score for each move
# Communicate with our game
# Alpha beta pruning

calc = calculations.CalculateEv()


class MiniMaxAi(container.PropContainer):
    def __init__(self):
        super().__init__()
        self.highest_score = -1000
        self.lowest_score = 1000
        self.best_move = -1
        self.enemy_worst_move = -1
        self.score_cross = 0
        self.score_circle = 0

    def get_possible_moves(self, board, move, player):
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

    def calculate_score(self, current_board, player, position):
        score_circle = 0
        score_cross = 0
        for y in range(1, 6):
            if calc.find_if_winning(player, y, current_board):
                score_circle += y * 10

            if calc.find_if_winning("cr", y, current_board):
                score_cross += y * 20
        # if calc.find_if_winning(player, 4, current_board):
        #     score_circle += 1000
        # if calc.find_if_winning("cr", 3, current_board):
        #     score_cross += 300

        if player == "cr":
            print(f"{score_circle - score_cross} yes")
            return score_circle - score_cross
        else:
            print(f"{score_cross - score_circle} hi")
            return score_cross - score_circle

    def minimax(self, board, player, is_max, depth, alpha, beta, position=None):

        if depth == 0 or calc.find_if_winning(player, 5, board):
            if not is_max:
                score = self.calculate_score("cr", board, position)
                return score,position
            score = self.calculate_score(board, player, position)

            # score2 = self.calculate_score(board, player, position)
            # score = score - score2
            # print(score)
            return score, position

        if is_max:
            max_pos_score = -1000
            best_move = None
            # moves = self.get_possible_moves(board, position, player)
            for move in self.get_possible_moves(board, position, player):
                board_copy = copy.deepcopy(board)
                board_copy[move] = player
                # if move > 63 and move < 68:
                #     print(move)
                current_node_eval = self.minimax(board_copy, player, False, depth - 1, alpha, beta, position=move)[0]
                max_pos_score = max(max_pos_score, current_node_eval)
                if max_pos_score == current_node_eval:
                    best_move = move

                if max_pos_score >= beta:
                    score = self.calculate_score(board_copy, player, position)
                    # print("man"+ str(score))
                    return score, position

                alpha = max(alpha, max_pos_score)

            return max_pos_score, best_move
        else:
            min_pos_score = 1000
            best_move = None
            for move in self.get_possible_moves(board, position, "cr"):
                board_copy = copy.deepcopy(board)
                board_copy[move] = "cr"
                if move == 64:
                    print(move)
                current_node_eval = self.minimax(board, player, True, depth - 1, alpha, beta, position=move)[0]
                min_pos_score = min(current_node_eval, min_pos_score)
                if min_pos_score == current_node_eval:
                    best_move = move

                if min_pos_score <= alpha:
                    score = self.calculate_score(board, "cr", position)
                    # print(str(score) + "min")
                    return score, position

                beta = min(beta, min_pos_score)

            return min_pos_score, best_move

    def set_score(self, value):
        self.score_circle = value