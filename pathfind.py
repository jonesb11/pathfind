

rows, cols = (5, 6) 
A = [["." for i in range(cols)] for j in range(rows)] 

A[1][1] = "#"
A[1][2] = "#"
A[1][3] = "#"


P = [0,1]
Q = [3,2]


A[P[0]][P[1]] = "P"
A[Q[0]][Q[1]] = "Q"

for i in range(0, len(A)):
    print(A[i])


print(len(A))
print(len(A[0]))

def evaluateSquare(maze, currentX, currentY):
    #Using len(maze[0]) for x as this is the length of a row or num of columns
    #Using len(maze) for y as this is the number of rows  
    if((currentX < 0 or currentX > len(maze[0])) or (currentY < 0 or currentY > len(maze))):
        return False
    elif(maze[currentY][currentX] == "#"):
        return False
    elif(maze[currentY][currentX] == True):
        return False
    return True


def recursiveCall(maze, currentX, currentY):
    
    #LEFT
    if(evaluateSquare(maze, currentX-1, currentY)):
        recursiveCall(maze, currentX-1, currentY)


    #RIGHT

    #TOP

    #DOWN


    return


def pathfind(a, p, q):

    recursiveCall(A, p[0], p[0])

    return 0

# print(evaluateSquare(A, 3, 0+1))