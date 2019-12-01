def selection_sort(nums):
    for i in range(len(nums)):
        min=i
        for j in range(i,len(nums)):
            if(nums[min]>nums[j]):
                min=j
        nums[i], nums[min] = nums[min], nums[i]
    return nums

if __name__ == "__main__":
    lis = [1,2,5,8,4,6]

    print(selection_sort(lis))