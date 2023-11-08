import pygame
pygame.init()
import numpy as np
import sys
import math
Row_count = 6
Col_count = 7
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,255,0)
Black = (0,0,0)
def create_board():
    board = np.zeros((6,7))
    return board
print (create_board())
board = create_board()
game_over = False
turn = 0
def drop_piece(board , row , col  , piece):
     board[row][col] = piece
     
def is_valid(board,col):
    return(board[Row_count-1][col] == 0)
 
def get_next_open_row(board,col):
    for row in range(Row_count):
        if board[row][col]==0:
            return row
def print_board(board):
    print(np.flip(board,0)) 

def win_game_horizental(board,row,num,col_start):
    intial_place=1
    count_Right = 0
    count_left = 0#for player 1
    for col in range (col_start+1,Col_count):
        if board[row][col]==num:
            count_Right+=1
        else:
            break
            
    for col in range(col_start-1,-1,-1):
        if board[row][col]==num:
            count_left+=1
        else:
            break
    if count_left+count_Right+intial_place>3:
        return True
    else:
        return False

def win_game_vertical(board,row_start,num,col):
    if (turn%2==0 and num==1)or(turn%2!=0 and num==2):
        initial_place=1
        count_up = 0
        count_down = 0
        for row in range (row_start+1,Row_count,+1):
            if board[row][col]==num:
                count_up+=1
            else:
             row=Row_count+1
        for row in range (row_start-1,-1,-1):
            if board[row][col]==num:
                count_down+=1
            else:
             row=-1
    
        if count_down + count_up+initial_place==4:
         return True
        else:
            count_down=0
            count_up=0
            return False

def win_game_diagonals(board , piece):
    for c in range(Col_count-3):
        for r in range (Row_count-3):
         if board[r][c]==piece and board[r+1][c+1] == piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
            return True
    
    
    
    for c in range(Col_count-3):
        for r in range (3,Row_count):
         if board[r][c]==piece and board[r-1][c+1] == piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
             return True

square_size = 100                           
height = (Row_count+1)*square_size
width = Col_count*square_size
size = (width,height)
radius = int(square_size/2-7)

screen = pygame.display.set_mode(size)
def draw_board(board):
  
    for r in range(Row_count):
        for c in range(Col_count):
            pygame.draw.rect(screen,Blue,(c*square_size,r*square_size+square_size,square_size,square_size))
            pygame.draw.circle(screen,Black,(int(c*square_size+square_size/2),int(r*square_size+square_size+square_size/2)),radius)
    for r in range(Row_count):
        for c in range(Col_count):
            if board[r][c]==1:
                pygame.draw.circle(screen,Red,(int(c*square_size+square_size/2),height- int(r*square_size+square_size+square_size/2)+square_size),radius)          
            if board[r][c]==2:
                 pygame.draw.circle(screen,Green,( int(c*square_size+square_size/2),height-int(r*square_size+square_size+square_size/2)+square_size),radius)
    pygame.display.update()       
draw_board(board)

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEMOTION:
            posX = event.pos[0]
            pygame.draw.rect(screen,Black,(0,0,width,square_size))
            if turn%2==0:
                pygame.draw.circle(screen,Red,(posX,int(square_size/2)),radius)
                
            else:
                pygame.draw.circle(screen,Green,(posX,int((square_size/2))),radius)
               
            pygame.display.update()    
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if turn%2==0:
             posX=event.pos[0]
             print(posX)
             col = int(math.floor(posX/100))
             print(col)
             if is_valid(board,col):
                row = get_next_open_row(board , col)
                drop_piece(board , row , col , 1)
                if win_game_horizental(board,row,1,col):
                    print("player 1 is winner")
                    game_over=True
                if win_game_vertical(board,row,1,col):
                    game_over=True
                    print("player 1 is winner")
                if win_game_diagonals(board , board[row][col]):
                    game_over=True
                    print("player 1 is winner")
                
            else:
             posX=event.pos[0]
             col = int(math.floor(posX/100))
             print(col)
             if is_valid(board,col):
                row = get_next_open_row(board , col)
                drop_piece(board , row , col , 2)
               
                if win_game_horizental(board,row,2,col):
                    game_over=True
                    print("player 2 is winner")
                if win_game_vertical(board,row,2,col):
                    game_over=True
                    print("player 2 is winner")
                if win_game_diagonals(board , board[row][col]):
                    game_over=True
                    print("player 2 is winner")
                
                
            print_board(board)
            print(turn)     
            turn+=1
            draw_board(board)
print("wp")