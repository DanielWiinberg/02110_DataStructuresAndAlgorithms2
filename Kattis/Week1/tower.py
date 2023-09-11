# https://open.kattis.com/problems/tornbygge?editsubmit=11622188

N = int(input())
M = list(map(int, input().split()))

number_of_towers = 1
for i in range(N-1):
  if M[i] < M[i+1]:
    number_of_towers += 1
    
print(number_of_towers)