
def fac(N): # 팩토리얼은 꼭 종료조건이 있어야함
    if N == 1:
        return 1 # N이 최소값을 찍으면 리턴하고 끝냄 
    else:
        return N * fac(N-1) # 재귀는 함수 안에 또다른 함수가 호출되어야하고 재귀니까 안의 함수는 N-1이여야함.

print(fac(10))