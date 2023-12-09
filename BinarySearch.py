
def power_search(array, number):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == number:
            return mid
        elif array[mid] < number:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == "__main__":
    g = [2, 5, 4, 8, 9, 11, -5, -4, 0, 7 ]
    print(sorted(g))
    print(power_search(sorted(g), int(input("Введите число: "))))

