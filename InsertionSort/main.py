def insertion_sort(nums):
    for i in range(1, len(nums)):
        aux = nums[i]
        j = i - 1
        while j >= 0 and aux < nums[j]:
            nums[j+1], nums[j] = nums[j], aux
            j -= 1
    return nums


if __name__ == "__main__":
    lis = [1, 8, 9, 0, 3, 1, 4, 8, 2]

    print(insertion_sort(lis))
