n = int(input())

a = list(map(int,str(n))) #구글 검색 숫자를 리스트로 바꾸기..
result = 0 #한수
if len(a) < 3: # 왜냐하면 len은 iterable한 변수만 가능 1~99는 모두 한수니까
    for a in n :
        result += 1 
else : # 셋째자리 부터는.. 시작을 애초에 99로 시작을 하고 
    #result = 99
    for a in n :
        if a[0] - a[1] == a[1] - a[2] :
            result += 1
print(result)