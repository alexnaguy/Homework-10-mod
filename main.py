import time
# Задание 1
# Создайте функцию, возвращающую список со всеми простыми числами
# от 0 до 1000. Используя механизм декораторов посчитайте сколько секунд,
# потребовалось для вычисления всех простых чисел. Отобразите на экран
# количество секунд и простые числа .
#
# Задание 2.
# Добавьте к первому заданию возможность передавать границы
# диапазона для поиска всех простых чисел


def decor_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Время работы функции {end - start}")
        return res
    return wrapper


def easy_number(number):
    """
        Возвращает True если число простое,иначе  False
        :param number(int): Число
        :return:
                bool
        """

    if number > 0:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True

@decor_time
def easy_numb_list (start: int = 0, end: int = 1000) -> list[int]:
    """

    :param start: Первая граница
    :param end: Вторая граница
    :return:
            list -список простых чимсел
    """
    return [i for i in range(start, end + 1) if easy_number(i)]

# Задание 3.
# Создайте функцию для отображения текущего времени. Функция не
# принимает параметров.
# Задание 4.
# Используя синтаксис декораторов, произведите декорирование
# функции из задания 3. Потенциальный вывод данных на экран после
# декорирования:
# ***************************
# 23:00
# ***************************

def decor_stars(func):
    def wrapper(*args, **kwargs):
        print(f"Текущее время:")
        print("*********************************")
        res = func(*args, **kwargs)
        print("*********************************")
        return res
    return wrapper()


@decor_stars
def now_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print (current_time)



def execute_application():
    #1
    print(f"Простые числа от 0 до 1000 {easy_numb_list()}")

    #2
    print(f"Простые числа от 1 до 50 {easy_numb_list(1,50)}")

    #3,4
    now_time


if __name__ == "__main__":
    execute_application()




