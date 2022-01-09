def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}

    for i in range(len(nums)):
        number = target - nums[i]

        if (number in d):
            index1 = d[number]
            index2 = i
            if (index1 != index2):
                return[index1,index2]

        d[nums[i]]=i
