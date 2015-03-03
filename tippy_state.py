import copy

from game_state import GameState
from tippy_move import TippyMove


class TippyState(GameState):
    """
    blablalballasldasdlasldflfgafelrsifndclxkjn
    
    for debug:
    inherits:
    opponent # Return the opponent of the next player, either 'p1' or 'p2'.
    get_move # not implemented /  Prompt user and return a move.
    apply_move # not implemeted / retursnnew game state, or none
    winner #  not implemented / return whether player has won
    possible_next_moves # not implemented / return a (possibly empty) list of 
    moves that are legal from
    outcome
    rough_outcome
    """

    def __init__(self, p, interactive=False, board=[]):
        """
        blalbladasld
        """

        self.board = board

        if interactive:

            n = input("How big should the board be? \n")
            while not n.isnumeric() or int(n) < 3:
                n = input("How big should the board be? \n")

            for x in range(int(n)):
                self.board.append([])
                for y in range(int(n)):
                    self.board[x].append(' ')

        GameState.__init__(self, p)
        self.instructions = ('gotta make dem instructions')

    def __repr__(self):
        """
        blelelalsaldsaldaldeScwecdsczx
        """

        return "TippyState({},{})".format(repr(self.next_player),
                                          repr(self.board))


    def __str__(self):
        """
        blabla
        """

        returnstatement = "Player {0}\n ".format(self.next_player)

        for x in range(len(self.board[0])):
            returnstatement += '\n' + '-' * (2 * len(self.board[0]) + 1) + \
                               '\n ' if x != 0 else ''
            for y in range(len(self.board[x])):
                returnstatement += "{}|".format(self.board[x][y]) if y != \
                                                                     len(
                                                                         self.board[
                                                                             x]) - 1 else "{}".format(
                    self.board[x][y])

        return returnstatement

    def __eq__(self, other):
        """
        aasdsdjfnjsdfn
        """
        return (isinstance(other, TippyState) and self.board == other.board
                and self.next_player == other.next_player)


    def apply_move(self, move):

        if move in self.possible_next_moves():
            self.board[move.x - 1][move.y - 1] = move.symbol
            return self.__class__(self.opponent(), False, self.board)
        else:
            return None

    def rough_outcome(self):
        """
        
        """
        opponent_tie = False
        for move in self.possible_next_moves():
            # maintain a copy
            new_self = copy.deepcopy(self).apply_move(move)
            if new_self.winner(self.next_player):
                return 1
            elif not opponent_tie:
                opponent_win = False
                for m in new_self.possible_next_moves():
                    if copy.deepcopy(new_self).apply_move(m).winner(
                            self.opponent()):
                        opponent_win = True
                if not opponent_win:
                    opponent_tie = True

        return -1 if not opponent_tie else 0


    def get_move(self):

        x, y = int(input("Which row? \n")), int(input("Which Column? \n"))
        return TippyMove((x, y), self.next_player)

    def winner(self, player):
        """
        gotta do this still
        """

        return is_tippy(self.board) and self.opponent() == player

    def possible_next_moves(self):
        """
        need to add checking for tippys
        """

        moves = []
        if is_tippy(self.board):
            return moves
        else:
            for x in range(len(self.board[0])):
                for y in range(len(self.board)):
                    if self.board[x][y] not in ('X', 'O'):
                        moves.append(
                            TippyMove((x + 1, y + 1), self.next_player))

        return moves


def is_tippy(b):
    """
    >>>tips = []
    >>>tips.append(TippyState(1, False, [[' ', ' ', 'X'], [' ', 'X', 'X'],
    [' ', 'X', ' ']]))
    >>>tips.append(TippyState(1, False, [['X', ' ', ' '], ['X', 'X', ' '],
    [' ', 'X', ' ']]))
    >>>tips.append(TippyState(1, False, [[' ', 'X', ' '], ['X', 'X', ' '],
    ['X', ' ', ' ']]))
    >>>tips.append(TippyState(1, False, [[' ', 'X', ' '], [' ', 'X', 'X'],
    [' ', ' ', 'X']]))
    >>>tips.append(TippyState(1, False, [[' ', '', ' '], ['X', 'X', ' '],
    [' ', 'X', 'X']]))
    >>>tips.append(TippyState(1, False, [[' ', '', ' '], [' ', 'X', 'X'],
    ['X', 'X', ' ']]))
    >>>tips.append(TippyState(1, False, [['X', 'X', ' '], [' ', 'X', 'X'],
    [' ', ' ', ' ']]))
    >>>tips.append(TippyState(1, False, [[' ', 'X', 'X'], ['X', 'X', ' '],
    [' ', ' ', ' ']]))
    >>>for state in tips:
    >>>    print(is_tippy(state.board))
    True
    True
    True
    True
    True
    True
    True
    True
    """

    for x in range(1, len(b[0]) - 1):
        for y in range(1, len(b) - 1):
            if b[x][y] != ' ':
                s = (b[x][y], b[x][y])
                if b[x + 1][y] is s[0]:
                    return (b[x + 1][y - 1], b[x][y + 1]) == s or \
                           (b[x + 1][y + 1], b[x][y - 1]) == s or \
                           (b[x][y - 1], b[x - 1][y - 1]) == s or \
                           (b[x][y + 1], b[x - 1][y + 1]) == s
                elif b[x - 1][y] is s[0]:
                    return (b[x - 1][y - 1], b[x][y + 1]) == s or \
                           (b[x - 1][y + 1], b[x][y - 1]) == s or \
                           (b[x][y - 1], b[x + 1][y - 1]) == s or \
                           (b[x][y + 1], b[x + 1][y + 1]) == s

    return False








