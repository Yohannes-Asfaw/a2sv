def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    sorted_arr = sorted(nums)
    answer = [0] * len(nums)
    for i in range(len(nums)):
        answer[i] = sorted_arr.index(nums[i])
    return answer
