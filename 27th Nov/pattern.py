# %%
for i in range(4):
    print('*' , end = ' ')
# %%
for i in range(4):
    for j in range(4):
        print('*' , end = ' ')
    print()
# %%
for i in range(6):
    for j in range(i):
        print('* ',end = '')
    print()
# %%
for i in range(1,6):
    for j in range(i):
        print(' * ' , end= ' ')
    print()
# %%
for i in range(1,5):
    for j in range(i):
        print(j+1 , end= ' ')
    print()
# %%
for i in range(1,5):
    for j in range(1,i+1):
        print(j , end= ' ')
    print()
# %%
for i in range(1,5):
    for j in range(1,i+1):
        print(i , ' ' , end = '')
    print()
# %%
for i in range(5,0,-1):
    for j in range(i):
        print(' * ' , end = '')
    print()
# %%
for i in range(5,0,-1):
    for j in range(i):
        print(j+1 , end = ' ')
    print()
# %%
for i in range(5,0,-1):
    for j in range(6-i):
        print(i, end = ' ')
    print()
# %%
n = int(input('How many rows you want?'))
for i in range(n):
    for j in range(i+1):
        print(chr(65+i) , end = ' ')
    print()
# %%
n = int(input('How many rows you want?'))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j) , end = ' ')
    print()
# %%
#Table of 2
for i in range(2,21,2):
    print(i)
# %%
num = int(input())
for i in range(1,11):
    print(num, 'x' , i , '=' , num*i)
# %%
