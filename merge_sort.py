def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:(len(arr)//2)]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        left_index = 0
        right_index = 0
        merge_index = 0

        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] < right_arr[right_index]:
                arr[merge_index] = left_arr[left_index]
                left_index += 1
            else:
                arr[merge_index] = right_arr[right_index]
                right_index += 1
            merge_index += 1

        while left_index < len(left_arr):
            arr[merge_index] = left_arr[left_index]
            left_index += 1
            merge_index += 1

        while right_index < len(right_arr):
            arr[merge_index] = right_arr[right_index]
            right_index += 1
            merge_index += 1




example = [1, 5, 2, 6, 7, 8, 9, 11, 3]

merge_sort(example)
print(example)