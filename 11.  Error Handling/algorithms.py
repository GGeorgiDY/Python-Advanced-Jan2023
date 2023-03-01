def binary_search(nums, target_value):
    left = 0
    right = len(nums) -1

    while left <= right:
        middle_index = (left + right) // 2
        middle_element = nums[middle_index]

        if middle_element == target_value:
            return middle_index

        if target_value > middle_element:
            left = middle_index + 1
        else:
            right = middle_index - 1


nums = [int(x) for x in input().split(', ')]
target_value = int(input())
result = binary_search(nums, target_value)
print(f'Target value index is {result}')

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 4