from data_structure.queue import Queue
from data_structure.linked_list import LinkedList






# Пример использования
max_size = 3
queue = Queue()
#size = int(input("Введите размер очереди: "))

while True:
    print("\nМеню:")
    print("1. Добавить пользователя в очередь")
    print("2. Удалить и вернуть пользователя из очереди")
    print("3. Подсчитать количество пользователей в очереди")
    print("4. Проверить, пустая ли очередь")
    print("5. Вывести всех пользователей в очереди")
    print("6. Выход из меню")



    choice = int(input("Выберите действие: "))

    if choice == 1:
        login = input("Введите логин пользователя: ")
        password = input("Введите пароль пользователя: ")
        user = {login: password}
        count_queu = queue.count()

        if count_queu >= max_size:
            print("Очередь переполнена. Пользователь не может быть добавлен!")
        else:
            queue.enqueue(user)
            print("Пользователь добавлен в очередь")



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
        print(queue.show_items())

    elif choice == 6:
        break
    else:
        print("Неверный выбор операции")
