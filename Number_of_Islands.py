
import sys
sys.setrecursionlimit(10**8)
class solution:
    def numIslands(self,grid):
        rows=len(grid)
        print(rows)
        cols=len(grid[0])
        islands=0
        stack=[]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    islands+=1
                    stack.append([row,col])
                    print(stack)
                    grid[row][col]=0
                    while(stack):
                        newrow,newcol=stack.pop()
                        for r in range(newrow-1,newrow+2):
                            for c in range(newcol-1,newcol+2):
                                if r>=0 and c>=0 and r<rows and c<cols and grid[r][c]==1:
                                    grid[r][c]=0
                                    stack.append([r,c])
        return islands

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=solution()
        print(obj.numIslands(grid))
        

