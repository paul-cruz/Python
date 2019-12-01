
def merge_sort(nums):
    if len(nums) >1: 
        mid = len(nums)//2 
        left = nums[:mid] 
        right = nums[mid:] 
  
        merge_sort(left) 
        merge_sort(right)  
  
        i = j = k = 0
          
        
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                nums[k] = left[i] 
                i+=1
            else: 
                nums[k] = right[j] 
                j+=1
            k+=1
          
        
        while i < len(left): 
            nums[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            nums[k] = right[j] 
            j+=1
            k+=1
  
if __name__ == '__main__': 
    with  open('input.txt','r') as input:
        lis = [int(i) for i in input.readline().split()]
    print = open('output.txt','w')
    merge_sort(lis) 
    for i in lis:
        print.write(str(i) + ' ')
    print.close()

