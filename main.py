from data_structure.dequee import Deque
from collections import deque

# Задание 1.
# Реализуйте структуру данных «Двусторонняя очередь» на основе
# связного списка (LinkedList)
# На ветке dev/class-10.2 в файле deque.py находится шаблон структуры.
# Протестируйте полученную структуру. Сравните работу своей
# структуры с встроенным классом deque модуля collections.


def execute_application():
    print("Работа  структуры данных на основе Linked_list : ")
    deq = Deque()
    print(f"Пустая двусторонняя очередь:")
    print(deq)

    print("Добавление элемента в начало очереди:")
    deq.add_first(2)
    print(deq)
    print("Добавление элемента в конец очереди:")
    deq.add_last(4)
    print(deq)
    print("Добавление элемента в конец очереди:")
    deq.add_last(8)
    print(deq)
    print("Добавление элемента в начало очереди:")
    deq.add_first(1)
    print(deq)
    print(f"Длина двусторонней очереди: {deq.__len__()}")

    print("Удаление элемента из конца очереди:")
    deq.remove_last()
    print(deq)
    print("Удаление элемента из начала очереди:")
    deq.remove_first()
    print(deq)
    print(f"Длина двусторонней очереди: {deq.__len__()}")

    print()
    print(f"Двустороняя очередь через модуль collections:")
    print("Пустая очередь")
    deq = deque()
    print(deq)
    print("Добавление элемента в начало:")
    deq.appendleft(2)
    print(deq)
    print("Добавление элемента в конец:")
    deq.append(4)
    print(deq)
    print("Добавление элемента в начало:")
    deq.appendleft(1)
    print(deq)
    print("Добавление элемента в конец:")
    deq.append(8)
    print(deq)
    print("Удаление элемента из конца очереди:")
    deq.pop()
    print(deq)
    print("Удаление элемента из начала очереди:")
    deq.popleft()
    print(deq)

    print("Добавление в конец очереди элементов итерируемого объекта:")
    deq.extend([2, 8, 14,])
    print(deq)
    print("Количество элементов в очереди:")
    r = deq.count(2)
    print(r)

    print("Разворот элементов очереди:")
    deq.reverse()
    print(deq)






if __name__ == "__main__":
    execute_application()