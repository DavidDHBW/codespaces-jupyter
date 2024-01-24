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
        self.whiteToMove = True
        

print (board[1][1])
