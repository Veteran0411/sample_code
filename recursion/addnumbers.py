# adding list of numbers
def addNumber(nums):
    if not nums:
        return 0
    else:
        return nums[0]+addNumber(nums[1:])

print(addNumber([1,2,3]))
    
# add 3 numbers
# def add3Numbers(a,b,c=None):
#     if c is None:
#         return a+b
#     else:
#         return add3Numbers(a+b,c)
    
# print(add3Number(1,2,3))