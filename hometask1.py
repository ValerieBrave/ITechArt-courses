import random
# -------TASK1
a = int(input("a=\n"))
printed = 0
c = 1
while printed < a:
    i = 0
    while i < c and printed < a:
        print(c, end=" ")
        i += 1
        printed += 1
    c += 1
# -------TASK2
A = list(map(int, input().split()))
seek = int(input("seek for "))
found = []
for i in range(len(A)):
    if A[i] == seek:
        found.append(i)
if len(found) == 0:
    print("Not in list")
else:
    for i in range(len(found)):
        print(found[i], end=" ")
# -------TASK3
cols = int(input("columns :"))
rows = int(input("rows :"))
array = []
new_array = []
for i in range(rows):
    row = list(map(int, input().split()))
    new_array.append([])
    if len(row) == cols:
        array.append(row)
    else:
        print("wrong size, try again")
for j in range(rows):
    for i in range(cols):
        new_array[j].append(0)
print(array)
for i in range(rows):
    for j in range(cols):
        if i == 0 and j == 0:
            new_array[i][j] = array[rows-1][j] + array[i][cols-1] + array[i][j+1] + array[i+1][j]
        elif i == 0 and j == cols-1:
            new_array[i][j] = array[i][j-1] + array[i+1][j] + array[0][0] + array[rows-1][j]
        elif i == rows-1 and j == 0:
            new_array[i][j] = array[0][0] + array[i][cols-1] + array[i-1][j] + array[i][j+1]
        elif i == rows-1 and j == cols-1:
            new_array[i][j] = array[0][cols-1] + array[i][0] + array[i-1][j] + array[i][j-1]
        elif i == 0:
            new_array[i][j] = array[i][j+1] + array[i][j-1] + array[i+1][j] + array[rows-1][j]
        elif i == rows-1:
            new_array[i][j] = array[i-1][j] + array[i][j+1] + array[i][j-1] + array[0][j]
        elif j == 0:
            new_array[i][j] = array[i-1][j] + array[i+1][j] + array[i][j+1] + array[i][cols-1]
        elif j == cols-1:
            new_array[i][j] = array[i-1][j] + array[i+1][j] + array[i][j-1] + array[i][0]
        else:
            new_array[i][j] = array[i-1][j] + array[i][j+1] + array[i+1][j] + array[i][j-1]
print(new_array)
# ------TASK4
matrix = []
n = int(input("n = "))
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)
matrix[n//2][n//2] = n**2
st = 1
m = 0
for v in range(n//2):
    for i in range(n-m):
        matrix[v][i+v] = st
        st += 1
    for i in range(v+1, n-v):
        matrix[i][-v-1] = st
        st += 1
    for i in range(v+1, n-v):
        matrix[-v-1][-i-1] = st
        st += 1
    for i in range(v+1, n-(v+1)):
        matrix[-i-1][v] = st
        st += 1
    m += 2
# m+=2 потому что одна "рамка" занимает две колонки
print(matrix)

