import sys
sys.stdin = open('2578.txt')

arr = [list(map(int,input().split())) for _ in range(5)]
ans = [list(map(int,input().split())) for _ in range(5)]

def zero(arr, lst):
    ans => list

    return x,y

def cnt(arr):
    total_horizon = total_vertical = total_cross_r = total_cross_l = 0 #초기화
    for i in range(5):
        for j in range(5):
            total_horizon += arr[i][j]
            total_vertical += arr[j][i]
        total_cross_r += arr[i][i]
        total_cross_l += arr[i][4-i]

    cnt = 0 #일단 초기화...
    while ~~조건을 뭘 주고~~~
        cnt += 1
    return cnt