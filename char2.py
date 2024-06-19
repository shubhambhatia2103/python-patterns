'''
A
A B 
A B C 
A B C D
A B C D E
'''

n = 5
for i in range(n):
    k = 65
    for j in range(i+1):
        print(chr(k), end=" ")
        k+=1
    print()