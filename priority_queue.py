from heap_realiz import *


class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"(Значение: {self.item}; Приоритет: {self.priority})"


class PriorityQueue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.__queue])

    # Проверяет пустая ли очередь
    def is_empty(self):
        return len(self.__queue) == 0

    #Добаляет значение в очередь
    def insert(self, item, priority):
        self.__queue.append(Entry(item, priority))
        self.__queue.sort()


    #Улаление элемента с максимальной приоритетностью из очереди
    def deletes(self):
        return self.__queue.pop().item


    def peek(self):
        return self.__queue[-1]

    def show_quee(self):
        for item in self.__queue:
            print(item)


def execute_application():
    qyeeee = PriorityQueue()
    #qyeeee.insert_element("Помыть машину", 5)
    qyeeee.insert_element("Сделать ДЗ", 7)
    print(qyeeee)
    qyeeee.delete_element(7)


if __name__ == "__main__":
    execute_application()
