"""
Two Sum
LeetCode #1: https://leetcode.com/problems/two-sum/
NeetCode: https://neetcode.io/problems/two-integer-sum

Problem:
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Optional, Dict, Set, Tuple, Any
import time


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the array that add up to target and return their indices.

        Uses a hash map to store numbers we've seen and their indices.
        For each number, we check if its complement (target - current number)
        exists in our hash map.

        Args:
            nums: List of integers
            target: Target sum we're looking for

        Returns:
            List containing the indices of the two numbers that add up to target
        """
        # Hash map to store number -> index mapping
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num

            # If complement exists in our hash map, we found our answer
            if complement in num_to_index:
                return [num_to_index[complement], i]

            # Store current number and its index
            num_to_index[num] = i

        # This should never happen according to problem constraints
        return []


def test_solution():
    """Test cases for the problem"""
    solution = Solution()

    # Test case 1: Basic example from LeetCode
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0, 1]
    result1 = solution.twoSum(nums1, target1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"

    # Test case 2: Different order
    nums2 = [3, 2, 4]
    target2 = 6
    expected2 = [1, 2]
    result2 = solution.twoSum(nums2, target2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"

    # Test case 3: Duplicate numbers
    nums3 = [3, 3]
    target3 = 6
    expected3 = [0, 1]
    result3 = solution.twoSum(nums3, target3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"

    # Edge case 1: Negative numbers
    nums_edge1 = [-1, -2, -3, -4, -5]
    target_edge1 = -8
    expected_edge1 = [2, 4]  # -3 + (-5) = -8
    result_edge1 = solution.twoSum(nums_edge1, target_edge1)
    assert (
        result_edge1 == expected_edge1
    ), f"Edge case 1 failed: expected {expected_edge1}, got {result_edge1}"

    # Edge case 2: Zero target
    nums_edge2 = [-3, 4, 3, 90]
    target_edge2 = 0
    expected_edge2 = [0, 2]  # -3 + 3 = 0
    result_edge2 = solution.twoSum(nums_edge2, target_edge2)
    assert (
        result_edge2 == expected_edge2
    ), f"Edge case 2 failed: expected {expected_edge2}, got {result_edge2}"

    print("✅ All test cases passed!")


def test_performance():
    """Performance test for large inputs"""
    solution = Solution()

    # Create a large input where the answer is at the end
    large_nums = list(range(10000))
    large_nums.append(1)  # This will pair with nums[1] = 1 to make target = 2
    target = 2

    start_time = time.time()
    result = solution.twoSum(large_nums, target)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_time_ms = execution_time * 1000.0

    print(
        f"⏱️  Execution time: {execution_time:.4f} seconds ({execution_time_ms:.4f} ms)"
    )
    assert execution_time < 1.0, f"Solution took too long: {execution_time:.4f} seconds"
    assert result == [
        0,
        2,
    ], f"Performance test failed: expected [0, 2], got {result}"

    print("✅ Performance test passed!")


if __name__ == "__main__":
    test_solution()
    test_performance()
