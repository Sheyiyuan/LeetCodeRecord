# Problem: https://leetcode.cn/problems/spiral-matrix-ii/
# Accepted at: 2026年8月30日 13:39

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        cur,x,y,face = 0,0,0,0
        left,top = 0,0
        right,bottom = n-1,n-1
        while cur < n*n:
            cur += 1
            mat[x][y] = cur
            if face == 0:
                if y == right :
                    top +=1
                    face = (face+1)%4
                    x += 1
                else:
                    y += 1 
            elif face == 1:
                if x == bottom :
                    right -=1
                    face = (face+1)%4
                    y -= 1
                else:
                    x += 1
            elif face == 2:
                if y == left :
                    bottom -=1
                    face = (face+1)%4
                    x -= 1
                else:
                    y -= 1
            else :
                if x == top :
                    left +=1
                    face = (face+1)%4
                    y += 1
                else:
                    x -= 1
        return mat
