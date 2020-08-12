'''
need this to add delay
'''
import time

'''
board class having methods that create board,
check if the board is full etc.
'''
class Board:
    def __init__(self):
        self.board=None
    
    def create(self):
        self.board=[[None,None,None],
                    [None,None,None],
                    [None,None,None]]
    
    def change(self,player):
        while True:
            pos=player.enter_pos()
            i=pos[0]
            j=pos[1]
            if self.board[i][j]==None:
                self.board[i][j]=player.symbol
                break
            else:
                print('ERROR:Position already occupied!!!')
                continue
    
    def is_full(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j]==None:
                    return False
        return True

    def print_board(self):
        print('\n')
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j]==None:
                    print('_',end='     ')
                else:
                    print(self.board[i][j],end='     ')
            print('\n')
        print('\n')
'''
class player having methods to enter name,calculate score,
play their turn etc.
'''  
class player:
    def __init__(self,symbol):
        self.name=None
        self.points=0
        self.symbol=symbol

    def enter_name(self,name):
        self.name=name
    
    def won(self,board,player):
        for i in range(0,3):
            if board[i][0:3]==[player.symbol,player.symbol,player.symbol]:
                return True
            if board[0][i]==player.symbol and board[1][i]==player.symbol and board[2][i]==player.symbol:
                return True
        if board[0][0]==player.symbol and board[1][1]==player.symbol and board[2][2]==player.symbol:
            return True
        if board[0][2]==player.symbol and board[1][1]==player.symbol and board[2][0]==player.symbol:
            return True
        return False

    def inc_points(self):
        self.points=self.points+1

    def enter_pos(self):
        while True:
            pos=input('Enter the position - ')
            if pos.upper()=='Q':
                return [0,0]
            elif pos.upper()=='W':
                return [0,1]
            elif pos.upper()=='E':
                return [0,2]
            elif pos.upper()=='A':
                return [1,0]
            elif pos.upper()=='S':
                return [1,1]
            elif pos.upper()=='D':
                return [1,2]
            elif pos.upper()=='Z':
                return [2,0]
            elif pos.upper()=='X':
                return [2,1]
            elif pos.upper()=='C':
                return [2,2]
            else:
                print('ERROR:Value not valid!!!')
                continue

'''
more functions we are gonna need.
'''
def start_credits():
    print('~'*20)
    print('\tNOTICE')
    print('~'*20)
    print('Welcome to TicTacToe.')
    print('Position are :')
    print('\tq  w  e')
    print('\ta  s  d')
    print('\tz  x  c')
    print('~'*20)
    print('\tNOTICE')
    print('~'*20)

def print_points(player1,player2):
    print(player1.name+' has '+str(player1.points),' points')
    print(player2.name+' has '+str(player2.points),' points')

def print_dot():
    for i in range(0,3):
        time.sleep(0.5)
        print('.')
    time.sleep(0.5)
    
def print_emoji():
    print('\\(\'+\')/')
    print('\n')

'''
Driving Function
Game TicTacToe
'''
def main():
    start_credits()
    while True:                                                                 #while loop 1
        player1=player('x')                                                     #game start
        player2=player('o')                                                     #players have to enter their name
        player1.enter_name(name=input('Player 1 enter name-'))
        while True:
            player2.enter_name(name=input('Player 2 enter name-'))
            if player2.name==player1.name:
                print('ERROR:Enter a different name for player 2!!!')
            else:
                break

        while True:                                                             #While loop 2
            print('*'*30)                                                       #creates new board everytime
            print_points(player1,player2)
            print('*'*30)
            board=Board()
            board.create()
            print('Board is being created\n')
            print_dot()
            board.print_board()

            while True:                                                         #While loop 3,loop for turn
                print(player1.name+'\'s'+' Turn'+' ('+player1.symbol+')')       #player 1 turn
                board.change(player1)                                           #
                board.print_board()                                             #
                if player1.won(board.board,player1):                            #
                    print(player1.name+' won this round')                       #
                    player1.inc_points()                                        # 
                    print_emoji()
                    break

                if board.is_full():
                    print('Draw!\n')
                    break
                    
                print(player2.name+'\'s'+' Turn'+' ('+player2.symbol+')')       #player 2 turn
                board.change(player2)                                           #
                board.print_board()                                             #
                if player2.won(board.board,player2):                            #
                    print(player2.name+' won this round')                       #
                    player2.inc_points()                                        # 
                    print_emoji()
                    break
                
                if board.is_full():
                    print('Draw!\n')
                    break

            choice1=input('ENTER:Another round. ELSE:Go to main menu\n')      #take's back to while loop 1 
            if choice1=='':                                                   #can also continue on while loop 2
                pass
            else:
                break

        choice2=input('ENTER:Start from the begining. ELSE:Exit\n')               #exits the game
        if choice2=='':                                                           #can also continue on while loop 1
            pass
        else:
            print('Goodbye '+player1.name+' and '+player2.name)
            print('Developed By - Prabhat\n')
            break
                
main()