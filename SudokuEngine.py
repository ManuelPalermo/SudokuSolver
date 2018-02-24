from copy import deepcopy

class Sudoku:
    '''
    self.sudoku = sudoku 2D array (9x9)
    self.options = dictionary( (pos): (options) ) where every pos has all the numbers which could fit, for a determinate state
    '''
    def __init__(self, sudoku):
        self.options = {}
        self.sudoku = sudoku
        self.find_alloptions()#updates options dictionary
        
    def getsudoku(self):
        return self.sudoku
    
    def getoptions(self):
        return self.options
    
    def oneoption(self):
        #if a pos only has one option, then the option can be chosen for the spot
        for i in self.options:
            if len(self.options[i])==1:
                self.sudoku[i[1]][i[0]]=self.options[i][0]
    
    def find_alloptions(self):
        #calls the find options function, for every pos in the sudoku
        for y in range(len(self.sudoku)):
            for x in range(len(self.sudoku)):
                self.findoptions([x,y])
    
    def findoptions(self,pos):
        #for a certain pos, finds the possible choices and updates the options.dictionary
        x=pos[0]    
        y=pos[1]
        if self.sudoku[y][x]!=0:self.options[tuple(pos)]=()
        else:
            inum=deepcopy(self.sudoku[y][x])
            opt=[n for n in range(1,10) if self.optionschecker(pos,n)==True]
            self.sudoku[y][x]=inum
            self.options[tuple(pos)]=tuple(opt)
        
    def optionschecker(self,pos,n):
        #checks if an option is valid(doesnt break any of the game rules)
        x=pos[0]
        y=pos[1]
        self.sudoku[y][x]=n
        if self.check_line_column(pos)==True: return False
        if self.check_square(pos)==True: return False
        return True
 
    def getsquarepos(self,s):
        #return the pos[x,y] of the every 3x3 square in the board
        square=None
        if s==1: square=[[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]
        elif s==2: square=[[3,0],[4,0],[5,0],[3,1],[4,1],[5,1],[3,2],[4,2],[5,2]]
        elif s==3: square=[[6,0],[7,0],[8,0],[6,1],[7,1],[8,1],[6,2],[7,2],[8,2]]
        elif s==4: square=[[0,3],[1,3],[2,3],[0,4],[1,4],[2,4],[0,5],[1,5],[2,5]]
        elif s==5: square=[[3,3],[4,3],[5,3],[3,4],[4,4],[5,4],[3,5],[4,5],[5,5]]
        elif s==6: square=[[6,3],[7,3],[8,3],[6,4],[7,4],[8,4],[6,5],[7,5],[8,5]]
        elif s==7: square=[[0,6],[1,6],[2,6],[0,7],[1,7],[2,7],[0,8],[1,8],[2,8]]
        elif s==8: square=[[3,6],[4,6],[5,6],[3,7],[4,7],[5,7],[3,8],[4,8],[5,8]]
        elif s==9: square=[[6,6],[7,6],[8,6],[6,7],[7,7],[8,7],[6,8],[7,8],[8,8]]
        return square
    
    def pos2square(self,pos):
        #gets a position and returns the square in which its located
        x=int(pos[0]*1.1/3)
        y=int(pos[1]*1.1/3)
        if x==0 and y==0: return 1
        if x==1 and y==0: return 2
        if x==2 and y==0: return 3
        if x==0 and y==1: return 4
        if x==1 and y==1: return 5
        if x==2 and y==1: return 6
        if x==0 and y==2: return 7
        if x==1 and y==2: return 8
        if x==2 and y==2: return 9
        
    def getsquare(self,s):
        #return the square as a 2D array
        array_pos=self.getsquarepos(s)
        lis=[]
        for l in range(3):
            ll=[]
            for c in array_pos[:3]:
                ll.append(self.sudoku[c[1]][c[0]])
            del array_pos[:3]
            lis.append(ll)
        return lis
        
    def printsudoku(self, sudoku):
        #prints the sudoku puzzle in a more view friendly way
        for l in range(len(sudoku)):
            st=""
            if l!=0 and (l%3==0):print(" - - - + - - - + - - -")
            for c in range(len(sudoku)):
                if c!=0 and c%3==0:  st=" ".join([st,"|"])
                st=" ".join([st,"%s"%(sudoku[l][c])])
            print(st)
        print()
            
    def transverse_line_column(self,pos):
        #makes sure the same number is not in the row/column(but transverses from the starting pos
        x=pos[0]
        y=pos[1]
        num=self.sudoku[y][x]
        for c in range(x+1,9):#Rigth
            if self.sudoku[y][c]==num:return False
        for c in range(1,x+1):#Left
            if self.sudoku[y][x-c]==num:return False
        for l in range(y+1,9):#Down
            if self.sudoku[l][x]==num:return False
        for l in range(1,y+1):#Up
            if self.sudoku[y-l][x]==num:return False
        return True
    
    def check_line_column(self,pos):
        #makes sure the same number is not in the row/column(returns False if not in the same line/row)
        x=pos[0]
        y=pos[1]
        num=self.sudoku[y][x]
        if num==0:return False
        for c in range(9):#checks the line
            if c!=x and self.sudoku[y][c]==num:return True
        for l in range(9):#checks the column
            if l!=y and self.sudoku[l][x]==num:return True
        return False
    
    def check_square(self,pos):
        #makes sure a number in a certain pos isnt repeated in a square(returns False if its not repeated)
        x=pos[0]
        y=pos[1]
        num=self.sudoku[y][x]
        s=self.pos2square([x,y])#gets the square where pos is located(from 1 to 9)
        sq=self.getsquare(self.pos2square(pos))#2D array with the square on which that pos belongs
        if num==0:return False
        if s==2:pos=[x-3,y]
        elif s==3:pos=[x-6,y]
        elif s==4:pos=[x,y-3]
        elif s==5:pos=[x-3,y-3]
        elif s==6:pos=[x-6,y-3]
        elif s==7:pos=[x,y-6]
        elif s==8:pos=[x-3,y-6]
        elif s==9:pos=[x-6,y-6]
        sq[pos[1]][pos[0]]=0
        return any(num in sublist for sublist in sq)
    
    def check_infractions(self):
        #check the whole board using simpler checks, to determine if an invalid move has been made
        if (True in [0 in i for i in self.sudoku])==True: return True #there are no empty spaces in the puzzle
        for y in range(len(self.sudoku)):
            for x in range(len(self.sudoku)):
                if self.check_line_column([x,y])==True: return True
                if self.check_square([x,y])==True:      return True
        return False
    
    def noheuristics(self):
        #solves teh puzzle only using backtracking and the options dict
        self.find_alloptions()
        self.printsudoku(self.sudoku)
    
    def auto_call(self):
        #calls heuristics repeatedly, until they can´t resolve any further
        while 1:
            copy=deepcopy(self.sudoku)
            self.find_alloptions()
            self.oneoption()
            self.printsudoku(self.sudoku)
            if copy==self.sudoku:
                return
            
    def get_minlen(self,options):
        #returns the dict key which has the lower len(value)
        try:
            choice=None
            minn=10
            for opt in options:
                if 0<len(options[opt])<minn:
                    minn=len(options[opt])
                    choice = opt
            return choice
        except: return None
        
    def solve(self):
        #solves the puzzle using backtracking and some heuristics
        #self.noheuristics()
        self.auto_call()
        old_state = deepcopy(self.sudoku)
        old_options = deepcopy(self.options)
        few_options_pos = self.get_minlen(self.options) #returns the position which has less options to try
        #no more options to try
        if few_options_pos!=None:
            for opt in self.options[few_options_pos]:
                self.sudoku[few_options_pos[1]][few_options_pos[0]] = opt
                self.find_alloptions()
                if self.solve()==True:
                    return True
                else:
                    self.sudoku=old_state
                    self.options=old_options
        if self.check_infractions()==False:
            return True

#empty
sk0=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#easy
sk1=[[5, 0, 7, 0, 9, 1, 0, 0, 6],
     [0, 0, 0, 0, 0, 7, 0, 4, 1],
     [0, 1, 0, 8, 5, 0, 2, 0, 0],
     [4, 0, 5, 0, 0, 6, 9, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 9, 1, 0, 0, 3, 0, 5],
     [0, 0, 1, 0, 7, 8, 0, 2, 0],
     [2, 4, 0, 5, 0, 0, 0, 0, 0],
     [8, 0, 0, 6, 2, 0, 1, 0, 9]]

#medium
sk2=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 5, 2, 3],
     [0, 0, 0, 0, 0, 0, 0, 1, 8],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 9, 0, 7, 4, 0, 6, 0],
     [0, 0, 4, 6, 1, 0, 0, 0, 7],
     [0, 5, 8, 0, 4, 3, 0, 0, 0],
     [0, 4, 0, 0, 2, 0, 0, 3, 0],
     [0, 6, 7, 0, 8, 1, 0, 9, 4]]

#hard
sk3=[[0, 0, 4, 0, 0, 2, 0, 0, 0],
     [0, 6, 9, 0, 4, 7, 0, 2, 0],
     [0, 0, 8, 0, 5, 6, 0, 0, 1],
     [0, 0, 0, 0, 0, 9, 3, 4, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 6],
     [0, 0, 0, 0, 3, 0, 1, 8, 0],
     [0, 2, 0, 0, 0, 0, 0, 0, 0],
     [0, 9, 0, 0, 8, 0, 6, 7, 0],
     [3, 0, 0, 5, 7, 0, 0, 0, 0]]
  
#very Hard
sk4=[[8, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 3, 6, 0, 0, 0, 0, 0],
     [0, 7, 0, 0, 9, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 7, 0, 0, 0],
     [0, 0, 0, 0, 4, 5, 7, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 3, 0],
     [0, 0, 1, 0, 0, 0, 0, 6, 8],
     [0, 0, 8, 5, 0, 0, 0, 1, 0],
     [0, 9, 0, 0, 0, 0, 4, 0, 0]]

#Hardest
sk5=[[0, 0, 0, 0, 0, 4, 9, 0, 5],
     [0, 1, 0, 0, 9, 0, 0, 0, 0],
     [0, 2, 0, 8, 3, 0, 0, 0, 0],
     [0, 8, 0, 0, 0, 0, 3, 0, 2],
     [0, 0, 6, 3, 0, 7, 1, 0, 0],
     [7, 0, 1, 0, 0, 0, 0, 6, 0],
     [0, 0, 0, 0, 7, 3, 0, 5, 0],
     [0, 0, 0, 0, 8, 0, 0, 9, 0],
     [3, 0, 4, 5, 0, 0, 0, 0, 0]]


sk6=[[0, 6, 1, 0, 0, 7, 0, 0, 3],
     [0, 9, 2, 0, 0, 3, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 8, 5, 3, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 5, 0, 4],
     [5, 0, 0, 0, 0, 8, 0, 0, 0],
     [0, 4, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 1, 6, 0, 8, 0, 0],
     [6, 0, 0, 0, 0, 0, 0, 0, 0]]

#edit a puzzle if u want
skother=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
