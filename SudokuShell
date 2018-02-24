from cmd import Cmd
from SudokuEngine import *
import time


class SudokuShell(Cmd):
    intro = 'Welcome to Sudoku! Type "help" for a list of avaiable commands.'
    prompt = 'Sudoku> '
    
    def do_show(self, arg):
        'Prints the sudoku puzzle in a more view friendly way'
        print()
        for l in range(len(sk.sudoku)):
            st=""
            if l!=0 and (l%3==0):print(" - - - + - - - + - - -")
            for c in range(len(sk.sudoku)):
                if c!=0 and c%3==0:  st=" ".join([st,"|"])
                st=" ".join([st,"%s"%(sk.sudoku[l][c])])
            print(st)
        print()
     
    def do_check(self, arg):
        'Check the whole board to determine if an invalid move has been made'
        if self.check()==True:print('An invalid move has been made')
        else: print('No invalid moves were made so far')
    
    def check(self):
        for y in range(len(sk.sudoku)):
            for x in range(len(sk.sudoku)):
                if sk.check_line_column([x,y])==True: return True
                if sk.check_square([x,y])==True:      return True
        return False
    
    def do_possible(self, arg):
        'Show a list with all the possible numbers for each position'
        sk.find_alloptions()
        for opt in sk.options:
            print(opt, ":" , sk.options[opt])
    
    def do_solve(self, arg):
        'Solves the sudoku puzzle automaticaly'
        start_time = time.clock()
        result = sk.solve()
        end_time = (time.clock() - start_time)#######stop timer
        if result==True:
            print(" Solved puzzle:")
            sk.printsudoku(sk.sudoku)
            print("The sudoku puzzle has successfuly been solved in %.5s seconds"%(end_time))
        else: print('The puzzle couldn´t be solved')
      
    def do_quit(self, arg):
        'Exits game'
        print("Some homo goodbye message")
        return True

if __name__ == "__main__":
    sh = SudokuShell()
    sk = Sudoku(sk5) #takes as argument, the sudoku puzzle to be solved
    sh.do_show("")
    sh.cmdloop()


#Choose the puzzle to use when calling sk=sudoku( x )
#The puzzles below are defined in the SudokuEngine.py
#sk0: empty puzzle
#sk1: Very Easy
#sk2: Easy
#sk3: Medium
#sk4: Hard
#sk5: Very Hard
#sk6: Impossibru (takes about 5 min to finish!)
