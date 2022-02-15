N = int(input())
word = input()

def change_num(word):
    num_lst = []
    for i in word :
        ans = ord(i)-96
        num_lst.append(ans)
    return num_lst

#print(change_num('happy')) #-->[8, 1, 16, 16, 25]
#print(change_num('new')) #-->[14, 5, 23]
#print(change_num('year')) #-->[25, 5, 1, 18]
numbers1 = change_num(word)
numbers2 = set(numbers1)

cnt = 0
count = {}
if len(numbers1) == len(numbers2) :
    cnt += 1
else :
    
