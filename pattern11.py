11111
 2222
  333
   44
    5

n = 5
p = 1
for i in range(n):
    for j in range(i+1):
        print(' ', end='')
    for j in range(i, n):
        print(p, end='')
    p +=1
    print()
    
    