num = int(input())
for i in range(num) :
    OX = list(input())
    score = 0
    add = 0
    for j in OX :
        add = add + 1 if j =='O' else 0
        score += add
    print(score)