import pygame

#js checking git push pull commit code stuffs
pygame.init()

res = (400, 400)

screen = pygame.display.set_mode(res)
pygame.display.set_caption("Chess")
square = pygame.image.load("./assets/square.png")
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Chess")
square = pygame.image.load("./assets/square.png")
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Chess")
square = pygame.image.load("./assets/square.png")

boardcolor = (255, 255, 255)


#assigns all images to a sprite to be called later
blackPawnSprite = pygame.image.load("./assets/black/bp.png")
blackKnightSprite = pygame.image.load("./assets/black/bk.png")
blackBishopSprite = pygame.image.load("./assets/black/bb.png")
blackRookSprite = pygame.image.load("./assets/black/br.png") 
blackQueenSprite = pygame.image.load("./assets/black/bq.png")
blackKingSprite = pygame.image.load("./assets/black/bk.png")

whitePawnSprite = pygame.image.load("./assets/white/wp.png")
whiteKnightSprite = pygame.image.load("./assets/white/wk.png")
whiteBishopSprite = pygame.image.load("./assets/white/wb.png")
whiteRookSprite = pygame.image.load("./assets/white/wr.png") 
whiteQueenSprite = pygame.image.load("./assets/white/wq.png")
whiteKingSprite = pygame.image.load("./assets/white/wk.png")


#all classes

class piece():
    def __init__(self, color, name, x, y, locked):
        self.color = color 
        self.name = name
        self.x = x
        self.y = y
        self.locked = True

    def lockPos(self):
        # TODO: check if move is legal if not be angry
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
        self.x, self.y = pos
        self.x -= 25
        self.y -= 25

class pawn(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 

    def drawPiece(self):

        if self.color == ("black"):
            screen.blit(blackPawnSprite, (self.x, self.y))

        if self.color == ("white"):
            screen.blit(whitePawnSprite, (self.x, self.y))

class knight(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 

    def drawPiece(self):

        if self.color == ("black"):
            screen.blit(blackKnightSprite, (self.x, self.y))

        if self.color == ("white"):
            screen.blit(whiteKnightSprite, (self.x, self.y))

class bishop(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 

    def drawPiece(self):

        if self.color == ("black"):
            screen.blit(blackBishopSprite, (self.x, self.y))

        if self.color == ("white"):
            screen.blit(whiteBishopSprite, (self.x, self.y))

class rook(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 

    def drawPiece(self):

        if self.color == ("black"):
            screen.blit(blackRookSprite, (self.x, self.y))

        if self.color == ("white"):
            screen.blit(whiteRookSprite, (self.x, self.y))

class queen(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 

    def drawPiece(self):

        if self.color == ("black"):
            screen.blit(blackQueenSprite, (self.x, self.y))

        if self.color == ("white"):
            screen.blit(whiteQueenSprite, (self.x, self.y))

class king(piece):
    def __init__(self, color, name, x, y, locked):
        super().__init__(color, name, x, y, locked)
        self.firstMove = True
        self.color = color 
        self.x = x
        self.y = y 

    def drawPiece(self):

        if self.color == ("black"):
            screen.blit(blackKingSprite, (self.x, self.y))

        if self.color == ("white"):
            screen.blit(whiteKingSprite, (self.x, self.y))


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

#creates all instances of all classes for pieces 

#setting up black side
pawn101 = pawn("black", "pawn101", 0, 50, False)
pawn102 = pawn("black", "pawn102", 50, 50, False)
pawn103 = pawn("black", "pawn103", 100, 50, False)
pawn104 = pawn("black", "pawn104", 150, 50, False)
pawn105 = pawn("black", "pawn105", 200, 50, False)
pawn106 = pawn("black", "pawn106", 250, 50, False)
pawn107 = pawn("black", "pawn107", 300, 50, False)
pawn108 = pawn("black", "pawn108", 350, 50, False)
rook101 = rook("black", "rook101", 0, 0, False)
rook102 = rook("black", "rook102", 350, 0, False)
knight101 = knight("black", "knight101", 50, 0, False)
knight102 = knight("black", "knight102", 300, 0, False)
bishop101 = bishop("black", "bishop101", 100, 0, False)
bishop102 = bishop("black", "bishop102", 250, 0, False)
queen101 = queen("black", "queen101", 200, 0, False)
king101 = king("black", "king101", 150, 0, False)

#setting up white side
pawn201 = pawn("white", "pawn201", 0, 300, False)
pawn202 = pawn("white", "pawn202", 50, 300, False)
pawn203 = pawn("white", "pawn203", 100, 300, False)
pawn204 = pawn("white", "pawn204", 150, 300, False)
pawn205 = pawn("white", "pawn205", 200, 300, False)
pawn206 = pawn("white", "pawn206", 250, 300, False)
pawn207 = pawn("white", "pawn207", 300, 300, False)
pawn208 = pawn("white", "pawn208", 350, 300, False)
rook201 = rook("white", "rook201", 0, 350, False)
rook202 = rook("white", "rook202", 350, 350, False)
knight201 = knight("white", "knight201", 50, 350, False)
knight202 = knight("white", "knight202", 300, 350, False)
bishop201 = bishop("white", "bishop201", 100, 350, False)
bishop202 = bishop("white", "bishop202", 250, 350, False)
queen201 = queen("white", "queen201", 200, 350, False)
king201 = king("white", "king201", 150, 350, False)

#it works... but please make a function to make this cleaner PLEASE


#list of all the pieces to draw

pieces = [pawn101, pawn102, pawn103, pawn104, pawn105, pawn106, pawn107, pawn108,
        rook101, knight101, bishop101, queen101, king101, bishop102, knight102, rook102,
        rook201, knight201, bishop201, queen201, king201, bishop202, knight202, rook202,
        pawn201, pawn202, pawn203, pawn204, pawn205, pawn206, pawn207, pawn208,]



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
                if mx in range(p.x, (p.x+50)):
                    if my in range(p.y, p.y+50):
                        if p.locked == False:
                            p.lockPos()
                            n = p.name
                            mx = (mx//50) * 50
                            my = (my//50) * 50
                            for i in pieces:
                                if ((i.x == mx) and (i.y == my)):
                                    if i.name != n: #makes sure u cant eat your own pawn as you move to blank space
                                            pieces.remove(i)
                                            break


                        else:
                            p.locked = False


    window()


#draws the pieces 
    for i in range(len(pieces)):
        p:piece = pieces[i]
        p.drawPiece()
        if not p.locked:
            p.move()


    pygame.time.wait(0)
    pygame.display.update()

