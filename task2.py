create pole
create item
price every step
controll item
algoryphm


coasts = [[2, 7, 9, 3], [12, 4, 1, 9], [1, 5, 2, 5]]

total_coasts = [[0 for _ in range(len(coasts[0]))] for _ in range(len(coasts))]#таблица стоимостей

total_coasts[0][0] = 2


print(total_coasts)
for j in range(1, len(coasts[0])):
    total_coasts[0][j] = total_coasts[0][j - 1] + coasts[0][j]# все время вправо
for j in range(1, len(coasts[1])):
    total_coasts[1][j] = total_coasts[1][j - 1] + coasts[1][j]
for j in range(1, len(coasts[2])):
    total_coasts[2][j] = total_coasts[2][j - 1] + coasts[2][j]
    print(coasts)
for i in range(1, len(coasts[0])):
    total_coasts[i][0] = total_coasts[i][1] + coasts[i][0]# все время вниз
for i in range(1, len(coasts[1])):
    total_coasts[i][1] = total_coasts[i-1][1] + coasts[i][1]
for i in range(1, len(coasts[2])):
    total_coasts[i][2] = total_coasts[i-1][2] + coasts[i][2]
print(coasts)
print(total_coasts)