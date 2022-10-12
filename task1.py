text = "flfkxkckg lglglglvl glofkg, fkfkfkf."
modify_text = text.replace(" ", "")
modify_text = modify_text.replace(",", "")
modify_text = modify_text.replace(".", "")


count_slog = len(modify_text) // 2
for slog in range(1, count_slog + 1):
    list = []# список слогов
    list.append(slog)


    count_pleyer = 3
    assert count_pleyer < count_slog
    for i in range(1, count_pleyer+1):
        list2 = []# список игроков
        list2.append(i)

        print(list2)
        print(count_slog)
    for i in range(0, count_pleyer):
        if count_slog%slog == 0:
            list2.pop(slog) #out of range
            print(list2)
            print(slog)
