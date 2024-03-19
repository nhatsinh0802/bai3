def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# Nhập vào n số nguyên
n = int(input("Nhập số lượng số nguyên: "))
arr = []
for i in range(n):
    num = int(input("Nhập số nguyên thứ {}: ".format(i + 1)))
    arr.append(num)

# Sắp xếp dãy số nguyên bằng Merge Sort
sorted_arr = merge_sort(arr)

# In ra dãy số nguyên đã được sắp xếp
print("Dãy số nguyên sau khi sắp xếp:")
for num in sorted_arr:
    print(num, end=" ")
