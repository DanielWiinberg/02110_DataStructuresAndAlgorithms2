# Robot can only move down and right, will it reach the goal
# If not could it have reached the goal, moving in any direction

n = int(input())
grid = [input() for _ in range(n)]
mod = 2**31 - 1

last_row = [0 for _ in range(n+1)] # Only care about the row I'm on and the last row
last_row[n-1] = 1 # By doing this one recursion is not needed

last_row_conn = [False for _ in range(n)]
last_row_conn[n-1] = True

for i in reversed(range(n)):
  curr_row = [0 for _ in range(n+1)]
  curr_row_conn = [False for _ in range(n+1)]
  for j in reversed(range(n)):
    if grid[i][j] == '.':
      curr_row[j] = (curr_row[j+1] + last_row[j]) % mod
      curr_row_conn[j] = curr_row_conn[j+1] or last_row_conn[j]
  last_row = curr_row
  last_row_conn = curr_row_conn
    
if last_row_conn[0]:
  print(last_row[0])
else:
  # DFS
  reachable = []
  for i in range(n+2): # Just make the grid bigger to handle edge cases
    reachable.append([])
    for j in range(n+2):
      if j != 0 and j != n+1 and i != 0 and i != n+1 and grid[i-1][j-1] == '.':
        reachable[i].append(-1)
      else:
        reachable[i].append(0)
  
  stack = [(int(1), int(1))]
  reachable[1][1] = 1
  while stack:
    i, j = stack.pop()
    reachable[i][j] = 2
    
    if reachable[i+1][j] == -1:
      pass
    # Many more cases here