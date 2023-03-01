n = int(input())
longest_intersection = {}

for _ in range(n):
    left_range, right_range = input().split('-')# ['0,3', '1,2']
    left_range_start_idx, left_range_end_idx = tuple(map(int, left_range.split(',')))# 0, 3
    right_range_start_idx, right_range_end_idx = tuple(map(int, right_range.split(',')))# 1, 2
    left_set = {num for num in range(left_range_start_idx, left_range_end_idx + 1)}# {0, 1, 2, 3}
    right_set = {num for num in range(right_range_start_idx, right_range_end_idx +1)}# {1, 2}
    intersection = left_set.intersection(right_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {[x for x in longest_intersection]} with length {len(longest_intersection)}")

# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10

# 5
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11

