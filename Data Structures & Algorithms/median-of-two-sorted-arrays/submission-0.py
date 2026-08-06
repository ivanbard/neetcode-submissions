class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # need O(log(m+n)) time solution
        # combine both arrays and find middle point?
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        total = n + m
        half = total // 2
        left, right = 0, n

        while left <= right:
            i = (left + right) // 2
            j = half - i

            nums1_left = nums1[i - 1] if i > 0 else float("-inf")
            nums1_right = nums1[i] if i < n else float("inf")
            nums2_left = nums2[j - 1] if j > 0 else float("-inf")
            nums2_right = nums2[j] if j < m else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2:
                    return min(nums1_right, nums2_right)
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2

            if nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1