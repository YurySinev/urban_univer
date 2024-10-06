nums = [12, 18, 5, 35, 10, 16, 20, 7, 9, 17, 3, 4, 26, 19, 8, 14, 15, 2, 1, 11, 13, 25, 24, 6]


# пузырьковая сортировка:
def bubble_sort(ls: list) -> list:
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True
    return ls


def bubble_sort2(ls: list) -> list:
    for i in range(len(ls) - 1, 0, -1):
        for j in range(i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls


# сортировка выборкой:
def selection_sort(ls: list):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]
    return ls

# сортировка вставкой:
def insertion_sort(ls: list) -> list:
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls


if __name__ == '__main__':
    print(nums)
    # bubble_sort(nums)
    # bubble_sort2(nums)
    # selection_sort(nums)
    insertion_sort(nums)
    print(nums)
