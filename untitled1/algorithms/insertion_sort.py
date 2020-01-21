arr = [12, 11, 13, 5, 6]


def insertion_sort(arr):
    """implemening insertion sort algorithm"""
    length = len(arr)
    # начинаем сортировку со второго элемента массива
    for j in range(1, length):
        key = arr[j]
        # Сравниваем   элементами стоящим перед j
        i = j - 1
        while i >= 0:
            # если предыдущий элемент больше jго то передвигаем его вперед и сравниваем  дальше
            if arr[i] > key:
                arr[i + 1] = arr[i]
                i -= 1
            else:
                break
        arr[i + 1] = key
    return arr


print(arr)
print(f'Sorted : {insertion_sort(arr)}')
