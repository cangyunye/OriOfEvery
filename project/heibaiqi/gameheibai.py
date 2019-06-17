# 黑白棋游戏
import pygame, sys, random
from pygame.locals import *
from os import path
# from math import sqrt

# TODO：比赛完成后不退出游戏
# TODO：显示可落子位置
# TODO：增加
 

scriptname = path.realpath(__file__)
scriptdir = path.dirname(scriptname)
BACKGROUNDCOLOR = (255, 255, 255)
BLACK = (255, 255, 255)
BLUE = (0, 0, 255)
CELLWIDTH = 63
CELLHEIGHT = 63
PIECEWIDTH = 47
PIECEHEIGHT = 47
BOARDX = 39
BOARDY = 39
FPS = 40
directions = [ [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1] ]
# 退出
def terminate():
    pygame.quit()
    sys.exit()
 
 
# 重置棋盘
def resetBoard(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = 'none'
 
    # Starting pieces:
    board[3][3] = 'black'
    board[3][4] = 'white'
    board[4][3] = 'white'
    board[4][4] = 'black'
 
 
# 开局时建立新棋盘
def getNewBoard():
    board = []
    for i in range(8):
        # 无子状态计为none
        board.append(['none'] * 8)
 
    return board
 
 
# 有效落子判定
def isValidMove(board, tile, xstart, ystart):
    # 如果该位置已经有棋子或者出界了，返回False
    if not isOnBoard(xstart, ystart) or  board[xstart][ystart] != 'none':
        return False
 
    # 临时将tile 放到指定的位置
    board[xstart][ystart] = tile
 
    if tile == 'black':
        otherTile = 'white'
    else:
        otherTile = 'black'
 
    # 要被翻转的棋子
    tilesToFlip = []
    tmps=[]
    # 对八方向依次检索
    for xdirection, ydirection in directions:
        # 相对起点坐标
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while  isOnBoard(x,y) and  board[x][y] == otherTile :
            x += xdirection
            y += ydirection
            if not isOnBoard(x,y):
                # 出界换向
               break
            elif board[x][y] == otherTile:
                # 对方棋子则判断下一点位
                continue
            elif board[x][y] == tile:
                print(f"翻转起点:{xstart}_{ystart}")
                print(f"翻转尾端:{x}_{y}")
                while True:
                    x -= xdirection
                    y -= ydirection
                    # 回到了起点则结束
                    if x == xstart and y == ystart:
                        break
                    # 需要翻转的棋子
                    tilesToFlip.append([x, y])
                print(f"tilesToFlip:{tilesToFlip}")

 
    # 将前面临时放上的棋子去掉，即还原棋盘
    board[xstart][ystart] = 'none' # restore the empty space
 
    # 没有要被翻转的棋子，则走法非法。翻转棋的规则。
    if len(tilesToFlip) == 0:   # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip
 
 
# 是否出界
def isOnBoard(x, y):
    return 0<=x<=7 and 0<=y<=7
 
 
# 获取可落子的位置
def getValidMoves(board, tile):
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves
 
 
# 获取棋盘上黑白双方的棋子数
def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'black':
                xscore += 1
            if board[x][y] == 'white':
                oscore += 1
    return {'black':xscore, 'white':oscore}
 
 
# 谁先走
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return gameplayer
 
 
# 将一个tile棋子放到(xstart, ystart)
def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
 
    if tilesToFlip == False:
        return False
 
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True
 
# 复制棋盘
def getBoardCopy(board):
    dupeBoard = getNewBoard()
 
    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]
 
    return dupeBoard
 
# 是否在角上
def isOnCorner(x, y):
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)
 
 
# 电脑走法，AI
def getComputerMove(board, computerTile):
    # 获取所以合法走法
    possibleMoves = getValidMoves(board, computerTile)
 
    # 打乱所有合法走法
    random.shuffle(possibleMoves)
 
    # [x, y]在角上，则优先走，因为角上的不会被再次翻转
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]
 
    bestScore = -1
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        # 按照分数选择走法，优先选择翻转后分数最多的走法
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove
 
# 是否游戏结束
def isGameOver(board):
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'none':
                return False
    return True
 
 
# 初始化
pygame.init()
mainClock = pygame.time.Clock()
gameplayer = 'player'
# 加载图片
boardImage = pygame.image.load(path.join(scriptdir,'board.png'))
# 返回x,y轴
boardRect = boardImage.get_rect()
blackImage = pygame.image.load(path.join(scriptdir,'black.png'))
blackRect = blackImage.get_rect()
whiteImage = pygame.image.load(path.join(scriptdir,'white.png'))
whiteRect = whiteImage.get_rect()
 
basicFont = pygame.font.SysFont(None, 48)
gameoverStr = 'Game Over Score '
 
# 开启棋盘
mainBoard = getNewBoard()
# 初始化棋局
resetBoard(mainBoard)
 
# 先手执黑
turn = whoGoesFirst()
if turn == gameplayer:
    playerTile = 'black'
    computerTile = 'white'
else:
    playerTile = 'white'
    computerTile = 'black'
 
print(turn,"回合") 
 
# 设置窗口
windowSurface = pygame.display.set_mode((boardRect.width, boardRect.height))
pygame.display.set_caption('黑白棋')
 
 
gameOver = False
 
 
# 游戏主循环
while True:
    # 从事件队列处理
    for event in pygame.event.get():
        # 退出游戏
        if event.type == QUIT:
            terminate()
        if gameOver == False and turn == gameplayer and event.type == MOUSEBUTTONDOWN and event.button == 1:
            # 定位鼠标x,y轴
            x, y = pygame.mouse.get_pos()
            # 锁定棋盘行列
            col = int((x-BOARDX)/CELLWIDTH)
            row = int((y-BOARDY)/CELLHEIGHT)
            if makeMove(mainBoard, playerTile, col, row) == True:
                print(f"玩家落子第{row+1}行，第{col+1}列")
                # 电脑是否有可行走法
                if getValidMoves(mainBoard, computerTile) != []:
                    turn = 'computer'

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(boardImage, boardRect, boardRect)
 
    if (gameOver == False and turn == 'computer'):
        x, y = getComputerMove(mainBoard, computerTile)
        makeMove(mainBoard, computerTile, x, y)
        savex, savey = x, y
 
        # 玩家是否有可行走法
        if getValidMoves(mainBoard, playerTile) != []:
            turn = gameplayer
 
    # windowSurface.fill(BACKGROUNDCOLOR)
    # windowSurface.blit(boardImage, boardRect, boardRect)
    # 落子绘图
    for x in range(8):
        for y in range(8):
            rectDst = pygame.Rect(BOARDX+x*CELLWIDTH+2, BOARDY+y*CELLHEIGHT+2, PIECEWIDTH, PIECEHEIGHT)
            if mainBoard[x][y] == 'black':
                windowSurface.blit(blackImage, rectDst, blackRect)
            elif mainBoard[x][y] == 'white':
                windowSurface.blit(whiteImage, rectDst, whiteRect)
    # 游戏结束
    if isGameOver(mainBoard):
        scorePlayer = getScoreOfBoard(mainBoard)[playerTile]
        scoreComputer = getScoreOfBoard(mainBoard)[computerTile]
        outputStr = gameoverStr + str(scorePlayer) + ":" + str(scoreComputer)
        text = basicFont.render(outputStr, True, BLACK, BLUE)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery
        windowSurface.blit(text, textRect)
    
    pygame.display.update()
    mainClock.tick(FPS)

# 作者：孤舟钓客 
# 来源：CSDN 
# 原文：https://blog.csdn.net/guzhou_diaoke/article/details/8201542 
# 版权声明：本文为博主原创文章，转载请附上博文链接！