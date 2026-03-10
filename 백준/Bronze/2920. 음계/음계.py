play = list(map(int, input().split()))
result = 'ascending'
for i in range(1, len(play)-1) :
    if play[i] - play[i-1] == -1:
        result = 'descending'
    elif play[i] - play[i-1] != 1:
        result = 'mixed'
        break
print(result)