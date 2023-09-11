# https://open.kattis.com/problems/fallingapart

N = int(input())
M = list(map(int, input().split()))

alice = 0; bob = 0
for i in range(N):
  materialistic_number = max(M)
  if i % 2 == 0:
    alice += materialistic_number
  else:
    bob += materialistic_number
  M.remove(materialistic_number)
  
print(alice, bob)