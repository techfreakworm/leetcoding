class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while(l<r):
            mid = l+ int((r-l)/2)
            are_halves_even = (r-mid)%2 == 0
            if nums[mid] == nums[mid + 1]:  # Either case 2 or case 3
                if are_halves_even: #case 2
                    l = mid + 2


                else: #case 3
                    r = mid - 1


            elif nums[mid] == nums[mid - 1]: # Either case 1 or case 4
                if are_halves_even: #case 1
                    r = mid - 2



                else: # case 4
                    l = mid + 1

            else: 
                return nums[mid]

        return nums[l]
        
        