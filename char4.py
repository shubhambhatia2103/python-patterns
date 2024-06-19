'''
ABCDE
 ABCD
  ABC
   AB
    A
'''

n = 5
for i in range(n):
    p = 65
    for j in range(i+1):
        print(' ', end='')
    for j in range(i, n):
        print(chr(p), end='')
        p +=1
    print()