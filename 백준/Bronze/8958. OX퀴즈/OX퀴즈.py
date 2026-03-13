num = int(input())
result = list()
for i in range(num) :
    OX = input()
    score = 0
    add = 0
    for j in range(len(OX)) :
        add = add + 1 if OX[j] =='O' else 0
        score += add
    result.append(score)

for i in range(num) :
    print(result[i])