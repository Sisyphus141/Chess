from tkinter import messagebox
from uuid import uuid4
import pygame

FEN_GAME_START = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"

PAWN   = 0
KNIGHT = 1
BISH   = 2
ROOK   = 3
QUEEN  = 4
KING   = 5

debug = False



pygame.init()

res = (400, 400)

screen = pygame.display.set_mode(res)
pygame.display.set_caption("Chess")
square = pygame.image.load("./assets/square.png")

boardcolor = (255, 255, 255)

SPRITES = {
    "black" : [
        pygame.image.load("./assets/black/bp.png"),
        pygame.image.load("./assets/black/bn.png"),
        pygame.image.load("./assets/black/bb.png"),
        pygame.image.load("./assets/black/br.png"), 
        pygame.image.load("./assets/black/bq.png"),
        pygame.image.load("./assets/black/bk.png")
    ],
    "white" : [
        pygame.image.load("./assets/white/wp.png"),
        pygame.image.load("./assets/white/wn.png"),
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
        self.locked = True
        difx = (self.x - 25) % 50
        dify = (self.y - 25) % 50

        self.x -= difx - 25
        self.y -= dify - 25

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
        
    def isLegalMove(self, **kwargs) -> bool:
        xAllowed = 1 if kwargs["attack"] else 0

        if self.color == "white":
            if self.firstMove == True:
                yAllowed = 2
            elif self.firstMove == False:
                yAllowed = 1

        if self.color == "black":
            if self.firstMove == True:
                yAllowed = -2
            elif self.firstMove == False:
                yAllowed = -1

        startPos:tuple[int] = kwargs['start']
        endPos:tuple[int]   = kwargs['end']
        
        ## check if the move is legal
        ## check if the x is allowed
        if abs(endPos[0] - startPos[0]) != xAllowed:
            return False
        ## check if the y is allowed
        if self.color == "black":
            if endPos[1] - startPos[1] > yAllowed * -1:
                return False
        elif self.color == "white":
            if startPos[1] - endPos[1] > yAllowed:
                return False
        
        ##check if its going backwards
        if self.color == "white":
            if endPos[1] > startPos[1]:
                return False

        if self.color == "black":
            if endPos[1] < startPos[1]:
                return False

        ## if we are attacking a piece we have to be moving diagonally
        if kwargs["attack"]:
            if abs(endPos[0] - startPos[0]) != abs(endPos[1] - startPos[1]):
                return False

        if self.firstMove: self.firstMove = False


        return True



class knight(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked, troop_type=KNIGHT)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 
        
    def isLegalMove(self, **kwargs) -> bool:
        startPos:tuple[int] = kwargs['start']
        endPos:tuple[int]   = kwargs['end']
        return True


class bishop(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked, troop_type=BISH)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 

    def isLegalMove(self, **kwargs) -> bool:
        return True
'''
        startPos:tuple[int] = kwargs['start']
        endPos:tuple[int]   = kwargs['end']
        board = kwargs['board']
        ## check if the move is legal
        ## check if the x is allowed
        if abs(endPos[0] - startPos[0]) != abs(endPos[1] - startPos[1]):
            return False
        
        ## check if there is a piece in the way
        for i in range(1, abs(endPos[0] - startPos[0])):
            y = startPos[1] + i * (endPos[1] - startPos[1]) // abs(endPos[1] - startPos[1])
            x = startPos[0] + i * (endPos[0] - startPos[0]) // abs(endPos[0] - startPos[0])
            if board[y][x] != None:
                return False
        return True
'''
class rook(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked, troop_type=ROOK)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 
        
    def isLegalMove(self, **kwargs) -> bool:
        return True
'''
        startPos:tuple[int] = kwargs['start']
        endPos:tuple[int]   = kwargs['end']
        board = kwargs['board']
        if abs(endPos[0] - startPos[0]) == abs(endPos[1] - startPos[1]):
            return False
        
        if endPos[0] - startPos[0] == 0:
            for i in range(1, abs(endPos[1] - startPos[1])):
                y = startPos[1] + i * (endPos[1] - startPos[1]) // abs(endPos[1] - startPos[1])
                if board[y][startPos[0]] != None:
                    return False
        ## check if there is a piece in the way
        for i in range(1, abs(endPos[0] - startPos[0])):
            x = startPos[0] + i * (endPos[0] - startPos[0]) // abs(endPos[0] - startPos[0])
            if board[startPos[1]][x] != None:
                return False
        return True
'''

class queen(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked, troop_type=QUEEN)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 
        
    def isRookLegal(self, **kwargs) -> bool:
        return True
        '''
        startPos:tuple[int] = kwargs['start']
        endPos:tuple[int]   = kwargs['end']
        board = kwargs['board']
        if abs(endPos[0] - startPos[0]) == abs(endPos[1] - startPos[1]):
            return False
        
        if endPos[0] - startPos[0] == 0:
            for i in range(1, abs(endPos[1] - startPos[1])):
                y = startPos[1] + i * (endPos[1] - startPos[1]) // abs(endPos[1] - startPos[1])
                if board[y][startPos[0]] != None:
                    return False
        ## check if there is a piece in the way
        for i in range(1, abs(endPos[0] - startPos[0])):
            x = startPos[0] + i * (endPos[0] - startPos[0]) // abs(endPos[0] - startPos[0])
            if board[startPos[1]][x] != None:
                return False
        return True
        '''

    def isBishupLegal(self, **kwargs) -> bool:
        return True
        '''
        startPos:tuple[int] = kwargs['start']
        endPos:tuple[int]   = kwargs['end']
        board = kwargs['board']
        ## check if the move is legal
        ## check if the x is allowed
        if abs(endPos[0] - startPos[0]) != abs(endPos[1] - startPos[1]):
            return False
        
        ## check if there is a piece in the way
        for i in range(1, abs(endPos[0] - startPos[0])):
            y = startPos[1] + i * (endPos[1] - startPos[1]) // abs(endPos[1] - startPos[1])
            x = startPos[0] + i * (endPos[0] - startPos[0]) // abs(endPos[0] - startPos[0])
            if board[y][x] != None:
                return False
        return True
        '''


    def isLegalMove(self, **kwargs) -> bool:
        ## TODO: fix this plz lol
        return True

        ## check if the move is legal
        #print(self.isRookLegal(**kwargs))
        #print(self.isBishupLegal(**kwargs))
        #if self.isRookLegal(**kwargs) or self.isBishupLegal(**kwargs):
        #    return True
        #return False
        
class king(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked, troop_type=KING)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 
    
    def isLegalMove(self, **kwargs) -> bool:
        
        '''
        startPos:tuple[int] = kwargs['start']
        endPos:tuple[int]   = kwargs['end']
        
        if abs(endPos[0] - startPos[0]) > 1 or abs(endPos[1] - startPos[1]) > 1:
            return False
        '''
        return True

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


def debugMode():
    printBoardASCII(board)
    for row in board:
        for p in row:
            if p is None:
                print("{0:5}".format("None"), end="")
                continue
            print("({0}, {1}){2:5}".format(p.x, p.y, ''), end="")
    


        

loop = True
currentPlayer = 'white'

#creates all instances of all classes for pieces 
FEN_TYPES = {
    'p': pawn,
    'r': rook,
    'n': knight,
    'b': bishop,
    'q': queen,
    'k': king
}

#it works... but please make a function to make this cleaner PLEASE

def printBoardASCII(board:list[list[piece]]) -> None:
    for row in board:
        for piece in row:
            print ("{0:15}".format(piece.name if piece != None else "None"), end="")
        print()

def formFEN(board:list[list[piece|None]]) -> str:
    FEN = ""
    space = 0
    for row in board:
        for p in row:
            if p is None:
                space += 1
            else:
                if space != 0:
                    FEN += str(space)
                    FEN += p.name[0].upper() if p.color == "white" else p.name[0]
                    space = 0
                else:
                    FEN += p.name[0].upper() if p.color == "white" else p.name[0]
        if space != 0:
            FEN += str(space)
        FEN += "/"
        space = 0
    FEN = FEN[:-1]
    FEN += " " + currentPlayer[0]
    return FEN

def renderFEN2D(fenStr:str) -> tuple[list[list[piece]], str]:
    board = []
    file  = []
    location = [0, 0]
    UID = 0
    fenSplit = fenStr.split(" ")
    currentPlayer = 'white' if fenSplit[1] == 'w' else 'black'
    
    fenPieces = fenSplit[0]
    for char in fenPieces:
        if char.isnumeric():
            location[0] += int(char) * 50
            ## fill the row with None to n - 1
            for i in range(int(char)):
                file.append(None)
        elif char == '/':
            location = [0, location[1] + 50]
            board.append(file)
            file = []
        else:
            color = "white" if char.isupper() else "black"
            troop_type = FEN_TYPES[char.lower()]
            file.append(troop_type(color, f"{char}{UID * 100 if color == 'black' else 200}", location[0], location[1], False))
            UID += 1
            location[0] += 50
    board.append(file)
    return (board, currentPlayer)

captured:dict[str, list[piece]] = {
    "white": [],
    "black": []
}

#pieces = renderFEN(FEN_GAME_START)
#pieces = renderFEN('8/2kp1b2/4B1q1/1P1P2R1/3R1NP1/8/3K4/4n2q w - - 0 1')

board, currentPlayer  = renderFEN2D('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')

print(currentPlayer)
#list of all the pieces to draw

previous_fens:list[str] = [formFEN(board)]
held_startPos = (0, 0)
holding = False
selected = None
"""
def kwargsFunny(*args, **kwargs):
    print(args)
    print(kwargs)

kwargsFunny("hello", "world", a=10, hello="hello world!")

loop = False
"""


while loop:
    events = pygame.event.get()
    pygame.display.update()

    mousePos = pygame.mouse.get_pos()

    for event in events:
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print(formFEN(board))
            if event.key == pygame.K_r:
                board, currentPlayer = renderFEN2D(previous_fens[-1])
                previous_fens.insert(0, previous_fens.pop())
                
            if event.key == pygame.K_u:
                board, currentPlayer = renderFEN2D(previous_fens[0])
                previous_fens.append(previous_fens.pop(0))
                
            if event.key == pygame.K_SPACE:
                ## reset the board
                board, currentPlayer = renderFEN2D(FEN_GAME_START)
                
            if event.key == pygame.K_ESCAPE:
                loop = not messagebox.askyesno("Quit", "Are you sure you want to quit?")
                
        #check for click here
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mx, my = pos 
            mx = mx // 50
            my = my // 50
            ## check if the player is holding a piece
            if not holding:
                if board[my][mx] != None and board[my][mx].color == currentPlayer and board[my][mx].locked:
                    holding = True
                    selected = board[my][mx]
                    selected.locked = False
                    held_startPos = (mx, my)
            elif holding:
                if board[my][mx] == selected:
                    holding = False
                    selected.lockPos()
                    selected = None
                    
                if board[my][mx] != None and board[my][mx].color == currentPlayer:
                    continue
                
                if not selected.isLegalMove(attack=True if board[my][mx] is not None else False, start=held_startPos, end=(mx, my), board=board):
                    messagebox.showerror("Error", "Illegal move")
                    break
                
                ## check if space is empty
                if board[my][mx] == None:
                    holding = False
                    selected.lockPos()
                    board[my][mx] = selected
                    selected = None
                
                elif board[my][mx].color != currentPlayer:
                    holding = False
                    selected.lockPos()
                    captured[currentPlayer].append(board[my][mx])
                    if board[my][mx].troop_type == KING:
                        loop = False
                        messagebox.showinfo("Game Over", "king has been captured!\n" + currentPlayer + " wins!")
                    board[my][mx] = selected
                    selected = None

                board[held_startPos[1]][held_startPos[0]] = None
                currentPlayer = "white" if currentPlayer == "black" else "black"
                previous_fens.append(formFEN(board))
                    
            
            if debug == True: debugMode()
            
    window()

    for row in board:
        for p in row:
            if p is not None:
                p.drawPiece()
                if not p.locked:
                    p.move()


    pygame.time.wait(0)
    pygame.display.update()
uuid = uuid4().hex
pygame.image.save(screen, f"{uuid}.png")

with open(uuid + ".fens", 'w+') as f:
    f.write('\n'.join(previous_fens))

