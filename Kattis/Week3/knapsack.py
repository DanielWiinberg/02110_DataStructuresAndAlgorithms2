import sys

lines = sys.stdin.readlines()

input_lines = []
for line in lines:
  line = line.strip().split()
  input_lines.append((int(line[0]), int(line[1])))

def knapsack(C, n, objects):
  M = [[0 for _ in range(C+1)] for _ in range(n+1)]
  
  for i in range(1, n+1):
    for w in range(1, C+1):
      weight, value = objects[i-1]
      if w < weight:
        M[i][w] = M[i-1][w]
      else:
        M[i][w] = max(value + M[i-1][w-weight], M[i-1][w])
  
  chosen_items = []
  w = C
  for i in range(n, 0, -1):
    if M[i][w] != M[i-1][w]:
      chosen_items.append(objects[i-1])
      w -= objects[i-1][0]
  
  return M[n][C], chosen_items

while len(input_lines) > 0:
  (C, n) = input_lines[0]
  objects = input_lines[1:n+1]
  input_lines = input_lines[n+1:]
  
  max_value, chosen_items = knapsack(C, n, objects)
  print(f'Max value: {max_value}, Chosen items: {chosen_items}')
  
# The implementation works, but doesn't pass the Kattis exercise, since the problem is a bit weird.