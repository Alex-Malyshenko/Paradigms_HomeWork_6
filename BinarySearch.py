
def power_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == "__main__":
    g = [2, 5, 4, 8, 9, 11, -5, -4, 0, 7 ]
    print(sorted(g))
    print(power_search(sorted(g), int(input("Введите число: "))))

