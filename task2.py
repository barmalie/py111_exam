


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
def calculate_path(total_costs, point):
rows = total_coasts[1][0]
cols = total_coasts[0][1]
    def get_step(i, j):
        if i == 0 and j == 0:
            return 1
        if not 0<=i<= rows:
            return 0
        if not 0<=j<= cols:
            return 0
        return sum([get_step(i + 1,j + 1),])
                    get_step(i - 1, j + 1),
                    get_step(i + 1, j - 1),
                    get_step(i - 1, j - 1),
                    get_step(i , j )])
        return get_step(i = point[0], j = point[1)