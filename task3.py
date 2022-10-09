import random

def repeat(number=1):
    """ Повтор декорированной функции заданное количество раз.
    В результате возвращается последнее значение оригинальной функции.
    : number — количество повторов, по умолчанию равно 3.
    """

    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result

        return wrapper

    return actual_decorator


@repeat(20)
def print_my_call():
    start_time = random.randint(0, 23)
    end_time = random.randint(1, 24)
    if start_time > end_time:
        zayavka = (end_time, start_time)
        print(zayavka, end=' ')




print_my_call()