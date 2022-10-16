text = "flfkxkckg lglglglvl glofkg, fkfkfkf."
# modify_text = text.replace(" ", "")
# modify_text = modify_text.replace(",", "")
# modify_text = modify_text.replace(".", "")
#
#
# count_slog = len(modify_text) // 2
# for slog in range(1, count_slog + 1):
#     list = []# список слогов
#     list.append(slog)
#
#
#     count_pleyer = 3
#     assert count_pleyer < count_slog
#     for i in range(1, count_pleyer+1):
#         list2 = []# список игроков
#         list2.append(i)
#
#         print(list2)
#         print(count_slog)
#     for i in range(0, count_pleyer):
#         if count_slog%slog == 0:
#             list2.pop(slog) #out of range
#             print(list2)
#             print(slog)

# Считалка
a= [10]
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