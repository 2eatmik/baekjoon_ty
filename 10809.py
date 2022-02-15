S = input()
alpabet = 'abcdefghijklmnopqrstuvwxyz'


for i in alpabet:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print('-1', end=' ')