# uses binary search to carryout operation
from bisect import bisect_left, bisect_right, insort_left, insort_right

sorted_list = [1, 2, 2, 3, 4, 5, 6]
target_value = 3

# bisect_left: Find the leftmost index where target_value should be inserted
left_index = bisect_left(sorted_list, target_value)
print("bisect_left:", left_index)

# def bisect_left(arr, x, lo=0, hi=None):
#     if hi is None:
#         hi = len(arr)
    
#     while lo < hi:
#         mid = (lo + hi) // 2
#         if arr[mid] < x:
#             lo = mid + 1
#         else:
#             hi = mid
    
#     return lo


# bisect_right: Find the rightmost index where target_value should be inserted
right_index = bisect_right(sorted_list, target_value)
print("bisect_right:", right_index)

# insort_left: Insert target_value into the sorted list at the leftmost position
insort_left(sorted_list, target_value)
print("insort_left:", sorted_list)

# insort_right: Insert target_value into the sorted list at the rightmost position
insort_right(sorted_list, target_value)
print("insort_right:", sorted_list)
