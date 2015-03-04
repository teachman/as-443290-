from move import Move


class TippyMove(Move):
    ''' A move in the game of Subtract Square.

    amount: int -- amount to subtract from current value.
    '''

    def __init__(self, location, p):
        """
        
        beepboopbeepboop
        """
        self.symbol = 'X' if p == 'p1' else 'O'
        self.x = location[0]
        self.y = location[1]

    def __repr__(self):
        ''' 
        blal
        '''
        return 'TippyMove({},{}, {})'.format(repr(self.x, self.y), repr(self.symbol))

    def __str__(self):
        """p
        bll
        """
        return "{} at ({},{})".format(self.symbol, self.x, self.y)


    def __eq__(self, other):
        '''
        blala
        '''
        return isinstance(other,
                          TippyMove) and self.symbol == other.symbol and (
                                                                             self.x,
                                                                             self.y) == (
                                                                             other.x,
                                                                             other.y)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

