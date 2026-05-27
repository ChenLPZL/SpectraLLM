def bubble_sort(arr):
    """Bubble sort - O(n^2)"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(arr):
    """Quick sort - O(n log n) average"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """Merge sort - O(n log n)"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ===== Test cases =====
if __name__ == "__main__":
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([1], [1]),
        ([], []),
        ([3, 3, 3, 3], [3, 3, 3, 3]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([-3, -1, -7, 0, 5, 2], [-7, -3, -1, 0, 2, 5]),
    ]

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort),
    ]

    all_passed = True
    for name, algo in algorithms:
        print(f"\n{'='*40}")
        print(f"Testing {name}")
        print(f"{'='*40}")
        for inp, expected in test_cases:
            result = algo(inp[:])  # pass a copy to avoid in-place mutation issues
            passed = result == expected
            status = "PASS" if passed else "FAIL"
            if not passed:
                all_passed = False
            print(f"  {status}: {name}({inp}) -> {result} (expected {expected})")

    print(f"\n{'='*40}")
    print("All tests passed!" if all_passed else "Some tests FAILED!")
    print("Finished!")
