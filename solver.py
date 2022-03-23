class Solution:
   def solve(self, matrix):
      n = len(matrix)

      rows = set()
      cols = set()
      diags = set()
      rev_diags = set()

      for i in range(n):
         for j in range(n):
            if matrix[i][j]:
               rows.add(i)
               cols.add(j)
               diags.add(i - j)
               rev_diags.add(i + j)

      return len(rows) == len(cols) == len(diags) == len(rev_diags) == n

ob = Solution()
matrix = [
   [0, 0, 0, 1, 0, 0, 0, 0],
   [1, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 1, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 1, 0],
   [0, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 1],
   [0, 0, 0, 0, 0, 1, 0, 0],
]
print(ob.solve(matrix))