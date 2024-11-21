nums=[12,1,3,55,93,44,13,9]
for i in range(len(nums)):
            swapped=False
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    swapped=True
            if(not swapped):
                break
print(nums,"bubble sort")