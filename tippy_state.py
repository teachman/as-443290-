from game_state import GameState
from tippy_move import TippyMove
import copy


class TippyState(GameState):
    """
    The state of a subtract square game. 
    
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
        """(TippyState, int, bool, list) -> NoneType

        Initialize Tippy State self with board of n x n dimensions based on 
        user input. 

        Assume: p in {'p1', 'p2'}
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
        """(TippyState) -> str

        Return a string representation of TippyState self
        that evaluates to an equivalent TippyState

        >>> t = TippyState('p1', False, 3)
        >>> t
        TippyState('p1', 3)
        """

        return "TippyState({},{})".format(repr(self.next_player),
                                          repr(self.board))


    def __str__(self):
        """(TippyState) -> str

        Return a convenient string representation of TippyState self.

        >>> t = TippyState('p1', False, 3) 
        >>> print(t)
        Player p1
          | | 
        -------
          | | 
        -------
          | | 
        """

        returnstatement = "Player {0}\n ".format(self.next_player)

        for x in range(len(self.board[0])):
            returnstatement += '\n' + '-' * (2 * len(self.board[0]) + 1) + \
                '\n ' if x != 0 else ''
            for y in range(len(self.board[x])):
                returnstatement += "{}|".format(self.board[x][y]) if y != \
                    len(self.board[x]) - 1 else "{}".format(self.board[x][y])

        return returnstatement

    def __eq__(self, other):
        """ (TippyState, TippyState) -> bool

        Return True iff this TippyState is the equivalent to other.

        >>> t1 = TippyState('p1', False, 3)
        >>> t2 = TippyState('p1', False, 3)
        >>> t1 == t2
        True
        """
        return (isinstance(other, TippyState) and self.board == other.board
                and self.next_player == other.next_player)


    def apply_move(self, move):
        """ (TippyState, TippyMove) -> TippyState
                
        Return new TippyState iff TippyMove is legal. 
        >>> t = TippyState('p1', False, 3)
        >>> m = TippyMove(1,1, 'O')
        t.apply_move(m) 
        ???
        """        
        if move in self.possible_next_moves():
            self.board[move.x - 1][move.y - 1] = move.symbol
            return self.__class__(self.opponent(), False, self.board)
        else:
            return None

    def rough_outcome(self):
        """(TippyState) -> Float  
        
        Provide a rough estimate of the chances of winning with current
        gamestate, b, based on the existence of an "L" shaped on the board.        
        """

        for move in self.possible_next_moves():
            # maintain a copy
            new_self = copy.deepcopy(self).apply_move(move)
            print(new_self)
            if new_self.winner(self.next_player):
                return 1
            else:
                for move in new_self.possible_next_moves():
                    print(copy.deepcopy(new_self).apply_move(move), '\n') 
                    if copy.deepcopy(new_self).apply_move(move).winner(self.opponent()):
                        return -1            
        return 0
             
                                          

    def get_move(self):
        """ (TippyState) -> TippyState
        
        Prompt player for their move and return TippyMove. 
        
        >>> t = TippyState('p1', False, 3)
        >>>t.get_move()
        Which row? 
        1
        Which Column? 
        1
        TippyMove(1,1, 'X')
        """        
        x, y = int(input("Which row? \n")), int(input("Which Column? \n"))
        return TippyMove((x, y), self.next_player)

    def winner(self, player):
        """(TippyState, str) -> bool
        
        Return True if the player has won the game. 
        
        >>> t = (TippyState('p1', False, [[' ', 'X', 'X'], ['X', 'X', ' '],
        [' ', ' ', ' ']])) 
        >>> t.winner('p1')
        True
        """

        return is_tippy(self.board) and self.opponent() == player

    def possible_next_moves(self):
        """(TippyState) -> list of TippyMove
        
        Return a list of legal moves for a given instance of the game. 
        
        >>> t = TippyState('p1', True)
        How big should the board be? 
        3
        >>> t.possible_next_moves()
        [TippyMove(1,1, 'X'), TippyMove(1,2, 'X'), TippyMove(1,3, 'X'), \
        TippyMove(2,1, 'X'), TippyMove(2,2, 'X'), TippyMove(2,3, 'X'), \
        TippyMove(3,1, 'X'), TippyMove(3,2, 'X'), TippyMove(3,3, 'X')]
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
    """(TippyState) -> bool 
    
    Return True if the board b contains a Tippy. 
    
    >>>tips = []
    >>>tips.append(TippyState('p1', False, [[' ', ' ', 'X'], [' ', 'X', 'X'],
    [' ', 'X', ' ']]))
    >>>tips.append(TippyState('p1', False, [['X', ' ', ' '], ['X', 'X', ' '],
    [' ', 'X', ' ']]))
    >>>tips.append(TippyState('p1', False, [[' ', 'X', ' '], ['X', 'X', ' '],
    ['X', ' ', ' ']]))
    >>>tips.append(TippyState('p1', False, [[' ', 'X', ' '], [' ', 'X', 'X'],
    [' ', ' ', 'X']]))
    >>>tips.append(TippyState('p1', False, [[' ', '', ' '], ['X', 'X', ' '],
    [' ', 'X', 'X']]))
    >>>tips.append(TippyState('p1', False, [[' ', '', ' '], [' ', 'X', 'X'],
    ['X', 'X', ' ']]))
    >>>tips.append(TippyState('p1', False, [['X', 'X', ' '], [' ', 'X', 'X'],
    [' ', ' ', ' ']]))
    >>>tips.append(TippyState('p1', False, [[' ', 'X', 'X'], ['X', 'X', ' '],
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
