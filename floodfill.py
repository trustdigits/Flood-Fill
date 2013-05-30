####################################################################
#########   FLOOD - FILL algorithm
####################################################################
#### NOTE
## Python list is a stack
## Python dequeue is a LIFO


##
import pylab as pl

class FFill:

    image = []
    mat = []
    count = 0
    flagSpillOut = False

    def __init__(self, matrix):
        self.image = matrix
        self.mat = deepCopy(self.image)
        self.count = 0
        self.roomCount = 0
        
        
    def flood_fill(self,i,j,target_color,repl_color):
        ''' virtually click on cell i,j, if this cell has target color
        then replace all "connected" same colored cells with repl_color
        ''' 
        self.count += 1
      
        if(self.mat[i][j] != target_color):
            return
        
        self.mat[i][j] = repl_color
        
        if(i > 0):
            self.flood_fill(i-1,j,target_color,repl_color)
         
        if(j > 0):
            self.flood_fill(i,j-1,target_color,repl_color)
         
        if(i < len(self.mat)-1):
            self.flood_fill(i+1,j,target_color,repl_color)
         
        if(j < len(self.mat[0])-1):  
            self.flood_fill(i,j+1,target_color,repl_color)


         
    def flood_fill_room_counter(self,i,j,target_color,repl_color):

        self.count += 1
      
        if(self.mat[i][j] != target_color):
            return
        
        self.mat[i][j] = repl_color
        
        if(i > 0):
            self.flood_fill(i-1,j,target_color,repl_color)

        else :
            self.flagSpillOut = True
             
        
        if(j > 0):
            self.flood_fill(i,j-1,target_color,repl_color)

        else :
            self.flagSpillOut = True
         
        if(i < len(self.mat)-1):  
            self.flood_fill(i+1,j,target_color,repl_color)

        else :
            self.flagSpillOut = True
         
        if(j < len(self.mat[0])-1):     
            self.flood_fill(i,j+1,target_color,repl_color)

        else :
            self.flagSpillOut = True

            
    def roomCounter(self):
        print ' here'
        for i in range(len(self.mat)):
            
            for j in range(len(self.mat[0])):
                
                if(self.mat[i][j] == 0): # is current pixel empty

                    self.flagSpillOut = False
                    
                    self.flood_fill_room_counter(i,j,0,10)
                    
                    if(self.flagSpillOut == False): # filled surface is not a border place
                      
                        self.roomCount += 1
                        
                


def plotHeatMap(mat):
    pl.matshow(mat, cmap=pl.cm.jet)
    pl.show()

    
def deepCopy(mat):
    '''
    Deep copy for matrix
    '''
    cpy = []
    for i in range(len(mat)):
        tmp = []
        for j in range(len(mat[i])):
            tmp.append(mat[i][j])
        cpy.append([x for x in tmp])

    return cpy


def toMat(textmap):
    mat = []
    lines = textmap.strip().split('\n')
    n_row, n_col = len(lines), len(lines[0])
    for i in range(n_row):
        tmp = []
        for j in range(n_col):
            if(lines[i][j] == '.'):
                tmp.append(0)
            elif(lines[i][j] == '#'):
                tmp.append(1)
        mat.append([x for x in tmp])
    return mat

    
