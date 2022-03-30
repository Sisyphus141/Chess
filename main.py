import pygame

FEN_GAME_START = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

PAWN   = 0
KNIGHT = 1
BISH   = 2
ROOK   = 3
KING   = 4
QUEEN  = 5

pygame.init()

res = (400, 400)

screen = pygame.display.set_mode(res)
pygame.display.set_caption("Chess")
square = pygame.image.load("./assets/square.png")

boardcolor = (255, 255, 255)

SPRITES = {
    "black" : [
        pygame.image.load("./assets/black/bp.png"),
        pygame.image.load("./assets/black/bk.png"),
        pygame.image.load("./assets/black/bb.png"),
        pygame.image.load("./assets/black/br.png"), 
        pygame.image.load("./assets/black/bq.png"),
        pygame.image.load("./assets/black/bk.png")
    ],
    "white" : [
        pygame.image.load("./assets/white/wp.png"),
        pygame.image.load("./assets/white/wk.png"),
        pygame.image.load("./assets/white/wb.png"),
        pygame.image.load("./assets/white/wr.png"), 
        pygame.image.load("./assets/white/wq.png"),
        pygame.image.load("./assets/white/wk.png")
    ]
}

#all classes

class piece():
    def __init__(self, color, name, x, y, locked, *, troop_type=PAWN):
        ## dynamics of the piece
        self.troop_type = troop_type
        self.color = color 
        self.name = name
        self.x = x
        self.y = y
        
        ## for sanity check later - may
        self.oldx = self.x
        self.oldy = self.y
        
        ## class properties
        self.firstMove = True
        self.locked = True

    def lockPos(self) -> None:
        # TODO: check if move is legal if not be 
        if not self.isLegalMove(): return
        self.locked = True
        difx = (self.x - 25) % 50
        dify = (self.y - 25) % 50

        self.x -= difx - 25
        self.y -= dify - 25

    def isLegalMove(self):
        """ Generic legality check """
        return True

    def move(self):
        """ Generic move """
        pos = pygame.mouse.get_pos()
        self.oldx, self.oldy = self.x, self.y
        self.x, self.y = pos
        self.x -= 25
        self.y -= 25
            
    def drawPiece(self) -> None:
        ## draw the piece
        screen.blit(SPRITES[self.color][self.troop_type], (self.x, self.y))

class pawn(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked, troop_type=PAWN)
        self.firstMove = True
        self.color = color 
        
        self.x = x
        self.y = y 
        
    def isLegalMove(self):
        allowedInc = 25 if not self.firstMove else 50
        allowedInc *= 1 if self.color == "black" else -1
        if self.firstMove: self.firstMove = False
        
        return True
    
class knight(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked, troop_type=KNIGHT)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 
        
class bishop(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked, troop_type=BISH)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 

class rook(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked, troop_type=ROOK)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 
class queen(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked, troop_type=QUEEN)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 
class king(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked, troop_type=KING)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 

#makes the board, dont ask questions idk what i did lol
y = 0
def window():
    screen.fill(boardcolor)
    board = [
        [1, 3, 5, 7],
        [0, 2, 4, 6],
        [1, 3, 5, 7],
        [0, 2, 4, 6],
        [1, 3, 5, 7],
        [0, 2, 4, 6],
        [1, 3, 5, 7],
        [0, 2, 4, 6]
    ]

    y = 0
    for row in board:
        for i in row:
            screen.blit(square, (i*50, y*50))
        y += 1

window()

loop = True
currentPlayer = 'w'

#creates all instances of all classes for pieces 
pieces:list[piece] = []

FEN_TYPES = {
    'p': pawn,
    'r': rook,
    'n': knight,
    'b': bishop,
    'q': queen,
    'k': king
}

#it works... but please make a function to make this cleaner PLEASE
def renderFEN(fenStr:str) -> list[piece]:
    board = []
    location = [0, 0]
    fenPieces = fenStr.split(" ")[0]
    for char in fenPieces:
        if char.isnumeric():
            location[0] += int(char) * 50
        
        elif char == '/':
            location = [0, location[1] + 50]
        else:
            color = "white" if char.isupper() else "black"
            troop_type = FEN_TYPES[char.lower()]
            board.append(troop_type(color, f"{color}{char}{location[0]}{location[1]}", location[0], location[1], False))
            location[0] += 50
    return board

pieces = renderFEN(FEN_GAME_START)

#list of all the pieces to draw

holding = False

while loop:
    events = pygame.event.get()
    pygame.display.update()

    mousePos = pygame.mouse.get_pos()

    for event in events:
        if event.type == pygame.QUIT:
            loop = False

        #check for click here
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mx, my = pos 
            for p in pieces:
                if mx in range(p.x, p.x+50) and my in range(p.y, p.y+50):
                    if p.locked == False:
                        n = p.name
                        mx = (mx//50) * 50
                        my = (my//50) * 50
                        occupied = False
                        for i in pieces:
                            if (locOccupied := (i.x == mx and i.y == my)):
                                occupied = True
                            ## i.color != p.color (prevents mutiny)
                            if (locOccupied) and (i.name != n) and (i.color != p.color):
                                pieces.remove(i)
                                p.lockPos()
                                holding = False
                                break
                            
                        if not occupied:
                            ## lock the piece (empty space)
                            p.lockPos()
                            holding = False
                    else:
                        p.locked = False if not holding else True
                        holding = True
 

    window()


#draws the pieces 
    for i in range(len(pieces)):
        p:piece = pieces[i]
        p.drawPiece()
        if not p.locked:
            p.move()


    pygame.time.wait(0)
    pygame.display.update()

