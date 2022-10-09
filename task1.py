text = "flfkxkckg lglglglvl glofkg, fkfkfkf."
modify_text = text.replace(" ", "")
modify_text = modify_text.replace(",", "")
modify_text = modify_text.replace(".", "")
# print(modify_text)

count_slog = len(modify_text) // 2
for slog in range(1, count_slog + 1):
    list = []
    list.append(slog)
    print(slog)

    count_pleyer = 3
    assert count_pleyer < count_slog
    # for i in range(1, count_pleyer+1):
    # list2 = []
    # list2.append(i)
    # print(i)
    # if count_slog == slog:
    # while list2 > list2[0]:
    # print(i,slog,"game over")
    # list2.pop()
    # print(i,slog,"game over")
    print([i for i in iter(iter(range(count_pleyer)).__next__, count_pleyer)])
    if count_slog == slog:
        print(i, slog, "game over")