#move log; determine which moves are valid; engine
class gameState():
    def __init__(self):
        
        #initialize playing board, 8X8 array
        #w = white, b = black, r= rock, n = knight, b = bishop, q= queen, k = king, p= pawn, --= empty field
        self.board = [["br","bn","bb","bq","bk","bb","bn","br"],
                ["bp","bp","bp","bp","bp","bp","bp","bp"],
                ["--","--","--","--","--","--","--","--"],
                ["--","--","--","--","--","--","--","--"],
                ["--","--","--","--","--","--","--","--"],
                ["--","--","--","--","--","--","--","--"],
                ["wp","wp","wp","wp","wp","wp","wp","wp"],
                ["wr","wn","wb","wq","wk","wb","wn","wr"]
                ]
        self.whiteToMove = True
        

print (board[1][1])
