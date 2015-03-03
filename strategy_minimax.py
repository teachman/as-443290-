import copy

from strategy import Strategy


class StrategyMinimax(Strategy):
    """
    lbaldlasd
    """

    def __init__(self, interactive=False):
        Strategy.__init__(self, interactive)
        self.player = None
        self.opponent = None

    def suggest_move(self, state):
        self.player = state.next_player
        self.opponent = state.opponent()
        return self.minimax(state, 1)[0]

    def minimax(self, state, depth):
        best_score, best_move = None, None

        for move in state.possible_next_moves():
            new_state = copy.deepcopy(state).apply_move(move)

            if new_state.possible_next_moves():
                score = self.minimax(new_state, depth + 1)[1]

            else:
                score = 1 if new_state.winner(self.player) else -1 if \
                    new_state.winner(self.opponent) else 0

            if depth == 1 and score == 1:
                print("W: {}".format(move))
            if depth == 1 and score == 0:
                print("T: {}".format(move))
            if depth == 1 and score == -1:
                print("L: {}".format(move))

            if best_score is None or (state.next_player != self.player and
                                              score < best_score) or (
                            state.next_player == self.player and score >
                        best_score):
                best_score, best_move = score, move

        return best_move, best_score

    

            
