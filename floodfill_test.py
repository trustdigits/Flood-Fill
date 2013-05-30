####################################################################
#########   FLOOD - FILL algorithm
####################################################################
import floodfill

def generateMat(): 
    mat = [[0,0,0,0,0,0,0,0]]*7
    mat = floodfill.deepCopy(mat)

    mat[0][0] = 1
    mat[0][1] = 1
    mat[1][1] = 1
    mat[1][2] = 1
    mat[2][2] = 1
    mat[3][2] = 1
    mat[4][2] = 1
    mat[5][2] = 1
    mat[5][1] = 1
    mat[5][0] = 1
    mat[4][4] = 1

    return mat

mat = generateMat()
ffill = floodfill.FFill(mat)
floodfill.plotHeatMap(ffill.image)
ffill.flood_fill(3,4,ffill.mat[3][4],6)
floodfill.plotHeatMap(ffill.mat)

mat = generateMat()
ffill = floodfill.FFill(mat)
ffill.flood_fill(3,0,ffill.mat[3][0],6)
floodfill.plotHeatMap(ffill.mat)

mat = generateMat()
ffill = floodfill.FFill(mat)
ffill.flood_fill(0,3,ffill.mat[0][3],6)
floodfill.plotHeatMap(ffill.mat)

mat = generateMat()
ffill = floodfill.FFill(mat)
ffill.flood_fill(4,4,ffill.mat[4][4],6)
floodfill.plotHeatMap(ffill.mat)

mat = generateMat()
ffill = floodfill.FFill(mat)
ffill.flood_fill(0,0,ffill.mat[0][0],6)
floodfill.plotHeatMap(ffill.mat)


######  room counting

textmap = """
........................#..............#..
........................#..............#..
........................#..............#..
.....######.............################..
.....#....#....######.....................
.....#....#....#....#.....#############...
.....######....##.###.....#...........#...
................#.#.......#############...
................#.#.......................
######.....######.#######.....######......
#....#.....#............#.....#....#......
###..#.....#............#.....#....#......
###..#.....##############.....#....#......
#....#........................######......
######....................................
"""
 
floodfill.plotHeatMap(floodfill.toMat(textmap))
ffill = floodfill.FFill(floodfill.toMat(textmap))
print ffill
ffill.roomCounter()
print ffill.roomCount
floodfill.plotHeatMap(ffill.mat)
