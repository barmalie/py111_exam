import random

# def repeat(number=1):
#     """ Повтор декорированной функции заданное количество раз.
#     В результате возвращается последнее значение оригинальной функции.
#     : number — количество повторов, по умолчанию равно 3.
#     """
#
#     def actual_decorator(function):
#         def wrapper(*args, **kwargs):
#             result = None
#             for _ in range(number):
#                 result = function(*args, **kwargs)
#             return result
#
#         return wrapper
#
#     return actual_decorator
#
#
# @repeat(20)
def print_my_call():
    count = []
    range_ = range(random.randint(1, 23))
    for i in range_:
        start_time = random.randint(0, 23)
        end_time = random.randint(1, 24)
        zayavka = (start_time, end_time)

        if start_time < end_time:
            count.append(zayavka)

    sort_index = sorted(count, key=lambda zayavka :zayavka[0])
    #print(sort_index)
    n = 0
    list_wish = []
    for wish in sort_index:
        if sort_index[n+1][0] > sort_index[n][1]:
            list_wish.append(wish)
            print(list_wish)
        else:
            print(wish)


        #print(set(list_wish))

    #print(list_wish[n])


print_my_call()
