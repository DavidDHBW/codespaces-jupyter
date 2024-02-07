#move log; determine which moves are valid; engine


class gameState():
        def __init__(self):
        
                #initialize playing board, 8X8 array
                #w = white, b = black, R= rock, N = knight, B = bishop, Q= queen, K = king, p= pawn, --= empty field
                self.board = [["bR","bN","bB","bQ","bK","bB","bN","bR"],
                        ["bp","bp","bp","bp","bp","bp","bp","bp"],
                        ["--","--","--","--","--","--","--","--"],
                        ["--","--","--","--","--","--","--","--"],
                        ["--","--","--","--","--","--","--","--"],
                        ["--","--","--","--","--","--","--","--"],
                        ["wp","wp","wp","wp","wp","wp","wp","wp"],
                        ["wR","wN","wB","wQ","wK","wB","wN","wR"]
                        ]
                self.movelog =[]
                self.whiteToMove = True
        def makeMove(self, move):
                self.board[move.startRow][move.startCol] = "--"
                self.board[move.endRow][move.endCol] = move.pieceMoved
                self.movelog.append(move.getChessNotation())
                self.whiteToMove = not self.whiteToMove



class Move():
        # for correct chess notation
        ranksToRows = {"1":7,"2":6, "3":5, "4":4,"5": 3, "6":2, "7": 1,"8":0}
        rowsToRanks = {v: k for k, v in ranksToRows.items()} # flip the dict
        filesToCols ={"a":0, "b":1, "c": 2, "d": 3,"e": 4, "f": 5, "g": 6, "h": 7}
        colsToFiles = {v:k for k, v in filesToCols.items()}


        def __init__(self, startSq, endSq, board):
                self.startRow = int(startSq[0])
                self.startCol = int(startSq[1])
                self.endRow = int(endSq[0])
                self.endCol = int(endSq[1])
                self.pieceMoved = board[self.startRow][self.startCol]
                self.piceCaptured = board[self.endRow][self.endCol]

        def getChessNotation(self):
                #this isnt the real chess notation things like caption a piece or castling are missing
                return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

        def getRankFile(self, r , c):
                return self.colsToFiles[c] + self.rowsToRanks[r]