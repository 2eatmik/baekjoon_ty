import random
lst = list(map(int,input()))

total = 0
sample = random.sample(lst,7)
for i in range(len(sample)):
    total += sample[i]
    if total == 100:
            print(lst)

