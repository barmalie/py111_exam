text = "flfkxkckg lglglglvl glofkg, fkfkfkfrdreh."
modify_text = text.replace(" ", "")
modify_text = modify_text.replace(",", "")
modify_text = modify_text.replace(".", "")

print(len(modify_text)//2)
count_slog = len(modify_text) // 2
for slog in range(1, count_slog + 1):
    list = []# список слогов
    list.append(slog)


    count_pleyer = 3
    list_count_player = []
    assert count_pleyer < count_slog
    for player in range(1, count_pleyer+1):
        #list2 = []# список игроков
        list_count_player.append(player)
    for player in list_count_player:

        players = len(list_count_player)
        counter = 0
        pointer = 1
    while slog > player:
        if count_slog % count_pleyer == 0:
            list_count_player.pop()
            print(list_count_player)
            pointer -= 1
    #while slog > player:
        #number = count_slog % players

        # if player == 1:
        #      #print(player)
        #      counter -=1
        #
        # else:
        #     pointer -= 1
        #     #print("победитель", player)
        # if counter == (count_slog):
        #     counter = 0
#print(count_slog)




    # for players in range(1, count_pleyer+1):
    #
    #     if count_slog % players == 0:
    #         list_count_player.pop(players-1) #out of range
    #         print(list_count_player)


"""         
# Считалка
a = [10]
#a = list(map(int, input().split()))
list_count_player = [i for i in range(1, a[0] + 1)]  # формируем список из кол-во человек
list_player_exit = []  # новый массив для списка из тех кто выбыл
i1 = 1
while 0 < len(list_count_player):  # пока в массиве не останется 1 элемент
    while i1 <= a[0]:  # цикл накручивает до второго числа ( который мы вводили в инпут )
        if i1 == a[0]:  # тут если он проходит проверку идет дальше
            for i1 in list_count_player:  # начинаем считать с этого индекса
                list_player_exit.append(list_count_player[i1])  # и сразу же добавляем в новый
                list_count_player.remove(i1)  # а отсюда удаляем
                i1 = 0  # ставим счетчик на ноль чтобы след действие не сбило его
        i1 += 1  # и увеличиваем до первоначального состояния

print(list_player_exit)  # выводим новый массив

members = []
n = 4
for i in range(-1, n):
    members.append('mem' + str(i + 1))
print(members)
# print (len(members))
k = 16
point = 1
index = 0
while len(members) > 1:
    if k % n == 0:
        # del members[index]
        members.pop(i)
        point = point - 1
        print(members)

    else:
        k % n == 1
        # del members[index-1]
        members.pop(i)
        point += 1
        index += 1

    if index == len(members):
        index = 0
# print(members)


"""
"""
if point == k:
      #print (index)
      #del members[index]

      point = 1
      members.pop(index)
      print(members)
      print(k)
   else:
      point +=1
      index +=1
   if index == len(members):
      index = 0
      #print(k)
print(members)
"""

