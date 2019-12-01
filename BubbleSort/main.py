def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if(nums[j]>nums[j+1]):
                nums[j] , nums[j+1] = nums[j+1] , nums[j]

    return nums

if __name__ == "__main__":
    lis = [1,2,5,8,4,6]

    print(bubble_sort(lis))