class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result_indexes = []
        mapper = {}
        for ind, cur in enumerate(nums):
            req = target - cur
            if req in mapper:
                return [ind, mapper[req]]
            mapper[cur] = ind 
                
        