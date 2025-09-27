def solveproblem(maze,x,y):
    return 0 <= x <= len(maze) - 1 and 0 <= y <= len(maze[0]) - 1 and maze[x][y] == 1

def solver(maze, x, y, sol):
    if x == len(maze) - 1 and y == len(maze[0]) - 1 and maze[x][y] == 1:
        sol[x][y] - 1
        return True
    
    if  solveproblem(maze, x, y):
        sol[x][y] = 1

        if solver(maze, x + 1, y, sol):
            return True
        
        if solver(maze, x, y + 1, sol):
            return True
        
        sol[x][y] = 0
        return False
    
    return False

def print_sol(maze):
    c = len(maze)
    g = [[0 for _ in range(c)] for _ in range(c)]
    if not solver(maze, 0, 0, g):
        print("maze is not found!")
        return
    else:
        print("path found")
        for i in g:
            print(i)

maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]

print_sol(maze)