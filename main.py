import heapq
from Priority_quee import Entry


class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"(Значение {self.item}; Приоритет {self.priority})"


def execute_application():


    my_que = []
    while True:
        print("\nМеню:")
        print("1- Добавить  новую задачу")
        print("2- Выполнить текущую задачу")
        print("3- Изменить приоритет задачи ")

        choise = int(input("Выберите действие: "))
        if choise == 1:
            task = input("Введите задачу: ")
            prioritet = int(input("Введите приоритет задачи: "))
            list_task = [task,prioritet]
            heapq.heappush(my_que,list_task)
            heapq.heapify(my_que)

            print(my_que)
        elif choise == 2:

            print(f"Задача: {task} с приоритетом {prioritet} успешно выполнена !")
            heapq.heappop(my_que)

        elif choise == 3:
            new_prioritet = int(input("Введите новый приоритет задачи: "))
            task = my_que[-1][0]
            print(task)
            heapq.heapreplace(my_que,[task,new_prioritet])
            print(my_que)

        elif choise == 4:
            print(my_que[-1])

        else:
            print("Выбрали недопустимое действие")





if __name__ == "__main__":
    execute_application()




