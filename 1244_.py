def girl(arr, card_num):
    if arr[card_num-1] != arr[card_num+1]:
        arr[card_num] += 1 # 0이면 1이되고 , 1이면 2가 됨
        if arr[card_num] == 2:
            arr[card_num] = 0
    else:
        i = 0
        arr[card_num] += 1
        while True:
            i += 1
            if arr[card_num-i] != arr[card_num+i]:
                break
            elif arr[card_num-i] == arr[card_num+i]:
                arr[card_num - i] += 1
                arr[card_num + i] += 1
                for a in range(N+1):
                    if arr[a] == 2:
                        arr[a] = 0
            if card_num - i == 1 or card_num + i == N:
                break
    return arr

def boy(arr, card_num):
    for i in range(1, N+1):
        if i % card_num == 0:
            arr[i] += 1 # 이러면 0은 1이되고 1은 2가됨
        if arr[i] == 2:
            arr[i] = 0
    return arr

N = int(input()) #스위치의 개수
arr = [0] + list(map(int, input().split())) + [99]
student_num = int(input())
for stu in range(student_num):
    stu_lst = list(map(int, input().split()))
    #print(stu_lst)
    if stu_lst[0] == 1:
        arr = boy(arr, stu_lst[1])
        #print(arr[1:])
    else:
        arr = girl(arr, stu_lst[1])
arr.pop(-1)
for i in range(1, N+1, 20):
    print(*arr[i:i+20])