T = int(input())

for tc in range(1, T+1):
    k = int(input())
    n = int(input())

    zero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    next = []

    for i in range(k):
        a = 0
        for i in range(len(zero)-1):
            a += zero[i]
            next.append(a)
    zero = []
    print(zero)

