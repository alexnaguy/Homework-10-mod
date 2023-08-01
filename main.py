from heap_realiz import *
from priori_quee import *



def execute_application():

    #
    # que.insert("Взять кредит под 10 %", 10)
    # que.insert("Оплатить услуги жкх", 2)
    # que.insert("Взять ипотеку", 7)
    # que.insert("Сделать вклад", 5)

    que = PriorityQueue()
    while True:
        print("\nМеню:")
        print("1- Добавить  пользователя в очередь с приоритетом")
        print("2- Удалить и вернуть пользователя из очереди с высшим приоритетом")
        print("3- Вернуть пользователя самого большого приоритета ")
        print("4- Проверить, пустая ли очередь")
        print("5- Вывести всех пользователей в очереди (с приоритетом)")
        print("0- Выход из меню")
        try:
            choice = int(input("Выберите действие: "))
        except ValueError as e:
            print("Выбор действия должен быть типом int")

        if choice == 1:
            item = input("Выберете цель визита посетителя в банк : ")
            priority = int(input("Выберите приоритет данной операции: "))
            que.insert(item, priority)


        elif choice == 2:
            que.deletes()

        elif choice == 3:
            print(que.peek())

        elif choice == 4:
            if que.is_empty():
                print("Очередь пустая")
            else:
                print("Очередь не пустая")

        elif choice == 5:
            if que.is_empty():
                print("Очередь пустая")
            que.show_quee()

        elif choice == 0:
            break
        else:
            print("Вы ввели недопустимое действие")



if __name__ == "__main__":
    execute_application()
