class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # O(N) where N is the length of the longest array
        # O(N) space where N is the length of the longest array

        # keep pointers on all 3 arrays     
        num1 = num2 = num3 = 0
        final_list = []
        while num1 < len(arr1) and num2 < len(arr2) and num3 < len(arr3):
            p1 = arr1[num1]
            p2 = arr2[num2]
            p3 = arr3[num3]
            # if they are all the same number, then add them to final list
            if p1 == p2 == p3:
                final_list.append(p1) # append either of them, it doesn't matter
                num1 += 1
                num2 += 1
                num3 += 1
                continue

            max_number = max(p1, p2, p3)

            if p1 < max_number:
                num1 += 1
            if p2 < max_number:
                num2 += 1
            if p3 < max_number:
                num3 += 1

        return final_list

# can do this using python functions such as set and sorted:
def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(set(arr1) & set(arr2) & set(arr3))

# remember another method is you can also sort it and use pointers to find the common elements

# my most recent solution (11/01) ^ improved so much from the above lol
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common_table = {} # holds the items in the first list
        result = [] # returns the final output
        for i in nums1: # go through the first list
            common_table[i] = 0 # put all its elements into the hash table
        
        for j in nums2:
            if j in common_table:
                result.append(j)
        return set(result)