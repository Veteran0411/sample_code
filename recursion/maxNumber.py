def maxNumber(nums):
    if nums:
        n1 = nums[0]
        
        if len(nums)==1:
            return n1
        n2 = maxNumber(nums[1:])
        if n1 > n2:
            return n1
        else:
            return n2
    else:
        return


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 2, 99, 10]
    print("max number is:", maxNumber(nums))
