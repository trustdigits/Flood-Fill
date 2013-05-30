Flood-Fill
==========

Flood fill, also called seed fill, is an algorithm that determines the area connected 

to a given node in a multi-dimensional array. It is used in the "bucket" fill tool of paint programs 
to fill connected, similarly-colored areas with a different color. 
When applied on an image to fill a particular bounded area with color, it is also known as boundary fill.
http://en.wikipedia.org/wiki/Flood_fill


Implementation uses disjoint-set data structure. 

A disjoint-set data structure is a data structure that keeps track of a set of elements partitioned into 
a number of disjoint (nonoverlapping) subsets. A union-find algorithm is an algorithm that performs two 
useful operations on such a data structure:
Find: Determine which subset a particular element is in. 
 This can be used for determining if two elements are in the same subset.
Union: Join two subsets into a single subset.
http://en.wikipedia.org/wiki/Disjoint-set_data_structure

In tests, we build a structure - a matrix. We virtually click on one cell i,j. This cell and all connected
cells with same color are colored with replacement color. There are two ways to create a matrix: as an object
defined cell by cell, or as a string, like this 

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
