# 统计每个月兔子的总数
f1, f2 = 1, 1
while 1:
    try:
        month = int(input())
        if month < 3:
            print(1)
            break
        ans = 0
        for i in range(3, month+1):
            ans = f2 + f1
            f1 = f2
            f2 = ans
        print(ans)
    except Exception as e:
        break