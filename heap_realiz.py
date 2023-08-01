def heapify(lst, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and lst[left_child] > lst[largest]:
        largest = left_child

    if right_child < heap_size and lst[right_child] > lst[largest]:
        largest = right_child

    if largest != root_index:
        lst[root_index], lst[largest] = lst[largest], lst[root_index]
        heapify(lst, heap_size, largest)


def heap_sort(lst):
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    for i in range(n-1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i, 0)


# Функция вставляет элемент
def insert_element(lst, newNum):
    size = len(lst)
    if size == 0:
        lst.append(newNum)
    else:
        lst.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(lst, size, i)
