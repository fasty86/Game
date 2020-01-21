arr = [12, 11, 13, 5, 6]

def insertion_desc(arr):
    """Сортируем  по уменьшению используя insertion sort alg"""
    length = len(arr)

    #делаем цикл со второго элемента
    for j in range(1, length):
        key = arr[j]
        # сравниваем с предшественниками
        i = j - 1
        while i >= 0:
            # Если jй  элемент больше, то передвигаем его в начало массива
            if key > arr[i]:
                arr[i+1] = arr[i]
                i -= 1
            else:
                break
        arr[i + 1] = key
    return arr

print(arr)
print(f'Sorted : {insertion_desc(arr)}')


