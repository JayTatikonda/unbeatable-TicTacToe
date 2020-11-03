from random import randint
import copy
class Game:
    def __init__(self,board,available):
        self.board = board
        self.available = available
    
    def show_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("--+---+----")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("--+---+----")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def check_win(self,val):
        ret = False
        #check rows - 
        if self.board[0] == val and self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            return True
        if self.board[3] == val and self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            return True
        if self.board[6] == val and self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            return True   

 
        #check columns
        if self.board[0] == val and self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            return True
        if self.board[1] == val and self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            return True
        if self.board[2] == val and self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            return True     

        
        #check diagonals
        if self.board[0] == val and self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            return True
        if self.board[6] == val and self.board[6] == self.board[4] and self.board[4] == self.board[2]:
            return True
    
        return ret

    def check_free(self):
        if len(self.available) == 0:
            return False 

        return True
    
    def put_marker(self,index,player):
        if player == 0:
            self.board[index] = 'O'
            # print("index: "+ str(index))
            # print(self.available)
            self.available.remove(index)

        if player == 1:
            self.board[index] = 'X'
            self.available.remove(index)







def make_comp_play(game):
    flag = True
    max_index = game.available[0]
    for i in game.available:
        player = 0
        win = 0
        draw = 0
        lose = 0


        for k in range(1000):
            Copied = copy.deepcopy(game)
            Copied.put_marker(i,player)

            while(1):  
                if single_move(Copied,player):

                    if player == 0:
                        player = 1
                    else:
                        player = 0
                    continue
                else:
                    break

            if Copied.check_win('O'):
                win = win + 500
            elif Copied.check_win('X'):
                lose = lose - 300
            else:
                draw = draw + 500

        temp = draw + win + lose
        if flag:
            max = temp
            # print(str(max) + " ss")
            flag = False
        
        # print(str(temp) + "  " +str(i))
        if temp > max:
            max = temp
            max_index = i
            # print(max_index)
    
    game.put_marker(max_index,0)

    
    

def single_move(Copied,player):
    if len(Copied.available) ==0:
        return False
    avail_index = randint(0,(len(Copied.available)-1))

    val = Copied.available[avail_index]

    Copied.put_marker(val,player)
    return True

        

def play_a_new_game():

    board = ["-","-","-",
            "-","-","-",
            "-","-","-",]
    available = [0,1,2,3,4,5,6,7,8]
    tic = Game(board,available)
    make_comp_play(tic)
    while(1):
        print("LAYOUT:")
        print("1 | 2 | 3 \n--+---+---\n4 | 5 | 6 \n--+---+---\n7 | 8 | 9 \n ")
        tic.show_board()
        # print("available moves \t")
        # print(tic.available)

        val = int(input("Please enter a number to place your marker there "))
        tic.put_marker((val-1),1)
        # tic.show_board()
        if tic.check_win('O'):
            tic.show_board()
            print("AI WON!")
            break
        elif tic.check_win('X'):
            tic.show_board()
            print("YOU WON! YAY!")
            break
        elif len(tic.available) ==0 and (tic.check_win('O') == False) and (tic.check_win('X') == False):
            tic.show_board()
            print("DRAW!!")
            break 
        make_comp_play(tic)
        if tic.check_win('O'):
            tic.show_board()
            print("AI WON!")
            break
        elif tic.check_win('X'):
            tic.show_board()
            print("YOU WON! YAY!")
            break
        elif len(tic.available) ==0 and (tic.check_win('O') == False) and (tic.check_win('X') == False):
            tic.show_board()
            print("DRAW!!")
            break


if __name__ == '__main__':
  play_a_new_game()
