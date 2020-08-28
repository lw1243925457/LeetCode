## iNOC产品部-杨辉三角的变形
# row = int(input())
row = 83

if row == 1:
    print(-1)
    exit(0)

curRow = [1]
colAmount = 1
for i in range(2, row + 1):
    nextRow = [0] * (colAmount + 2)
    for j in range(0, len(curRow)):
        nextRow[j] += curRow[j]
        nextRow[j+1] += curRow[j]
        nextRow[j+2] += curRow[j]
    print(curRow, nextRow)
    colAmount += 2
    curRow = nextRow.copy()

for i in range(0, len(curRow)):
    if curRow[i] % 2 == 0:
        print(i+1)
        exit(0)
print(-1)