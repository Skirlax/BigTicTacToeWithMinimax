import calculations
import copy

calc = calculations.CalculateEv()

def minimax( board, depth, player, alpha, beta):
    if depth == 0:
        # Return to the get_best_move method
        return calculate_score(board, player)
    if player == 'c':
        best_score = -1000
        for move in get_all_possible_moves(board):
            board_copy = copy.deepcopy(board)
            board_copy[move] = 'c'
            score = minimax(board_copy, depth - 1, 's', alpha, beta)
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = 1000
        for move in get_all_possible_moves(board):
            board_copy = copy.deepcopy(board)
            board_copy[move] = 's'
            score = minimax(board_copy, depth - 1, 'c', alpha, beta)
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


def get_all_possible_moves( board):
    possible_moves = []
    for index, x in enumerate(board):
        if x == 'x':
            possible_moves.append(index)
    return possible_moves


def calculate_score( board, player):
    score = 0
    for index, x in enumerate(board):
        if x == player:
            for y in range(4):
                if calc.find_if_winning(player, y, board):
                    score += y
    return score * 10


def get_best_move( board, depth, player):
    best_score = -1000
    best_move = -1
    for move in get_all_possible_moves(board):
        board_copy = copy.deepcopy(board)
        board_copy[move] = player
        score = minimax(board_copy, depth - 1, 's' if player == 'c' else 'c', -1000, 1000)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move