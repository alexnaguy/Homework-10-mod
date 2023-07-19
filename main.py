from data_structure.queue import Queue
# Пример использования

queue = Queue()
#size = int(input("Введите размер очереди: "))
size = 2
while True:
    print("\nМеню:")
    print("1. Добавить пользователя в очередь")
    print("2. Удалить и вернуть пользователя из очереди")
    print("3. Подсчитать количество пользователей в очереди")
    print("4. Проверить, пустая ли очередь")
    print("5. Вывести всех пользователей в очереди")
    print("6. Выход из меню")



    choice = int(input("Укажите операцию: "))

    if choice == 1:
        login = input("Введите логин пользователя: ")
        password = input("Введите пароль пользователя: ")
        user = {login: password}
        if queue.count() <= size:
            queue.enqueue(user)
            print("Пользователь добавлен в очередь")
        else:
            print("Очередь переполнена")


    elif choice == 2:
        user = queue.dequeue()
        if user:
            print(f"Удален и возвращен пользователь: {user}")

    elif choice == 3:
        count = queue.count()
        print(f"Количество пользователей в очереди: {count}")

    elif choice == 4:
        if queue.is_empty():
            print("Очередь пустая")
        else:
            print("Очередь не пуста")

    elif choice == 5:
        print("Пользователи в очереди:")
        r = queue.displayss()
        print(r)

    elif choice == 6:
        break
    else:
        print("Неверный выбор операции")
