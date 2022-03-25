def twoSum(nums, target):
    complement = {}
    
    for i, num in enumerate(nums):
        if num in complement:
            return [complement[num], i]
        complement[target-num] = i

if __name__ == '__main__':
    print(twoSum([1,2,3,4], 5))