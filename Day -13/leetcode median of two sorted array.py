class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr3: List[int] = nums1 + nums2
        arr3.sort()
        len3: int = len(arr3)
        return (arr3[len3//2-1]/2.0 + arr3[len3//2] / 2.0, arr3[len3//2])[len3 %2] if len3 else None
