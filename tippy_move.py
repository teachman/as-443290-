from move import Move


class TippyMove(Move):
    ''' A move in the game of Subtract Square.

    amount: int -- amount to subtract from current value.
    '''

    def __init__(self, location, p):
        """(TippyMove, tup, str) -> NoneType

        Initialize a new TippyMove for placing a symbol on the board.
        
        Assume: p in {'p1', 'p2'}
        """
        self.symbol = 'X' if p == 'p1' else 'O'
        self.x = location[0]
        self.y = location[1]

    def __repr__(self):
        ''' (TippyMove) -> str
        
        Return a string representation of this TippyMove. 
        
        >>> m = TippyMove((1,1), 'p1')
        >>> m
        TippyMove(1,1, 'X')
        '''
        return 'TippyMove({},{}, {})'.format(self.x, self.y, repr(self.symbol))

    def __str__(self):
        """ (TippyMove) -> str
        
        Return a string representation of this TippyMove that is suitable 
        for users to read. 
        
        >>> m = TippyMove((1,1), 'p1')
        >>> print(m)
        to place an X at (1,1)
        """
        return "to place an {} at ({},{})".format(self.symbol, self.x, self.y)


    def __eq__(self, other):
        """(TippyMove, TippyMove) -> bool
        Return True iff this TippyMove is the same as other.

        >>> m1 = TippyMove((1,1), 'p1')
        >>> m2 = TippyMove((1,1), 'p2')
        >>> print(m1 == m2)
        False
        """
        return isinstance(other,
                          TippyMove) and self.symbol == other.symbol and (
                                                                         self.x,
                                                                         self.y) == (
                                                                         other.x,
                                                                         other.y)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

