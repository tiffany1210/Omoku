from boardstate import *

# Gomoku has the matrix board representing black or white.
# Gomoku decides who wins.
# Gomoky has the current position and the state for that position.
class Gomoku(object):
    def __init__(self, hparams):
        #Gomoky instance variable probably
        self.hparams = hparams
        #chessMap is the board, 2 by 2 matrix of black or white.
        self.__chessMap = [
            [BoardState.EMPTY for j in range(self.hparams['board_size'])]
            for i in range(self.hparams['board_size'])
            ]
        self.__currentI = -1
        self.__currentJ = -1
        self.__currentState = BoardState.EMPTY

    def get_chessMap(self):
        return self.__chessMap

    def get_chessboard_state(self, i, j):
        return self.__chessMap[i][j]

    def set_chessboard_state(self, i, j, state):
        self.__chessMap[i][j] = state
        self.__currentI = i
        self.__currentJ = j
        self.__currentState = state
    #return winner's current state
    def get_chess_result(self):
        if self.connected_five(self.__currentI, self.__currentJ, self.__currentState):
            return self.__currentState
        else:
            return BoardState.EMPTY
    #player is currentState
    def direction_count(self, i, j, xdirection, ydirection, player):
        count = 0
        for step in range(1, 5):  # 1,2,3,4 look four more steps on a certain direction, 5 NOT INCLUDED
            if xdirection != 0 and (j + xdirection * step < 0 or j + xdirection * step >= self.hparams['board_size']):
                break
            if ydirection != 0 and (i + ydirection * step < 0 or i + ydirection * step >= self.hparams['board_size']):
                break
            if self.__chessMap[i + ydirection * step][j + xdirection * step] == player:
                count += 1
            else:
                break
        return count

    def connected_five(self, i, j, player):
        # there are 4 possible axis and 8 directions in omok
        possibleAxis = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 1), (1, -1)],
                        [(-1, -1), (1, 1)]]  # can we take this out as a global variable? idk
        for axis in possibleAxis:
            connected_count = 1
            for (xdirection, ydirection) in axis: # two directions (-1,0), (1,0) for axis [(-1, 0), (1, 0)]
                connected_count += self.direction_count(i, j, xdirection, ydirection, player)
                if connected_count >= 5:
                    return True
        return False
