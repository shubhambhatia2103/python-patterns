'''
A
B C
D E F
G H I J
K L M N O
'''
n = 5
k = 65
for i in range(n):
    for j in range(i+1):
        print(chr(k), end=" ")
        k+=1
    print()