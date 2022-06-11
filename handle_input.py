import container


class InputHandler:

    def get_input(self):
        play_with_ai = input("Do you wish to play against AI? (y/n): ")
        if play_with_ai == 'y' or play_with_ai == 0:
            return True
        else: return False

       