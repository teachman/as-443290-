from tippy_state import TippyState
from tippy_move import TippyMove


class TicState(TippyState):
    """
    blablalballasldasdlasldflfgafelrsifndclxkjn   
    """

    def __init__(self, p, interactive=False,
                 board=[[' ', ' ', ' '], [' ', ' ', ' '], \
                        [' ', ' ', ' ']]):
        """
        We felt like making Tic Tac Toe as well!
        """
        TippyState.__init__(self, p, False, board)
        self.instructions = (
            'The classic game of Tic-Tac-Toe.\nTo win, you must get a '
            'vertical, '
            'horiztonal, or diagonal line.')


    def winner(self, player):
        """
        aasdasd
        """
        return is_line(self.board) and self.opponent() == player


    def possible_next_moves(self):
        """
        need to add checking for tippys
        """

        moves = []
        if is_line(self.board):
            return moves
        else:
            for x in range(len(self.board[0])):
                for y in range(len(self.board)):
                    if self.board[x][y] not in ('X', 'O'):
                        moves.append(
                            TippyMove((x + 1, y + 1), self.next_player))

        return moves


def is_line(board):
    """
    returns true if there is a line
    called is_tippy for the sake of simplicity (otherwise we would have to
    re-write
    many imported methods!)
    else returns false
    """

    symbol = ''
    for x in (0, 1, 2):
        if board[x][0] != ' ' and board[x][0] == board[x][1] == board[x][2]:
            return True

    for y in (0, 1, 2):
        if board[0][y] != ' ' and board[0][y] == board[1][y] == board[2][y]:
            return True

    return (board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]) \
           or (board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0])








