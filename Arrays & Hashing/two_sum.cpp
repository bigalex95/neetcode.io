/*
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
*/

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <queue>
#include <stack>
#include <climits>
#include <cmath>
#include <chrono>
#include <iomanip>

using namespace std;

class Solution
{
public:
    /**
     * Find two numbers in the array that add up to target and return their indices.
     *
     * Uses an unordered_map to store numbers we've seen and their indices.
     * For each number, we check if its complement (target - current number)
     * exists in our hash map.
     *
     * @param nums Vector of integers
     * @param target Target sum we're looking for
     * @return Vector containing the indices of the two numbers that add up to target
     */
    vector<int> twoSum(vector<int> &nums, int target)
    {
        // Hash map to store number -> index mapping
        unordered_map<int, int> numToIndex;

        for (int i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];

            // If complement exists in our hash map, we found our answer
            if (numToIndex.find(complement) != numToIndex.end())
            {
                return {numToIndex[complement], i};
            }

            // Store current number and its index
            numToIndex[nums[i]] = i;
        }

        // This should never happen according to problem constraints
        return {};
    }
};

// Helper function to compare vectors (for testing)
template <typename T>
bool areEqual(const vector<T> &a, const vector<T> &b)
{
    if (a.size() != b.size())
        return false;
    for (size_t i = 0; i < a.size(); i++)
    {
        if (a[i] != b[i])
            return false;
    }
    return true;
}

// Helper function to print vector
template <typename T>
void printVector(const vector<T> &vec)
{
    cout << "[";
    for (size_t i = 0; i < vec.size(); i++)
    {
        cout << vec[i];
        if (i < vec.size() - 1)
            cout << ", ";
    }
    cout << "]";
}

// Test function
void runTests()
{
    Solution solution;

    cout << "Running tests for Two Sum..." << endl;

    // Test case 1: Basic example from LeetCode
    {
        vector<int> nums = {2, 7, 11, 15};
        int target = 9;
        vector<int> expected = {0, 1};
        vector<int> result = solution.twoSum(nums, target);
        assert(areEqual(result, expected));
        cout << "✅ Test 1 passed" << endl;
    }

    // Test case 2: Different order
    {
        vector<int> nums = {3, 2, 4};
        int target = 6;
        vector<int> expected = {1, 2};
        vector<int> result = solution.twoSum(nums, target);
        assert(areEqual(result, expected));
        cout << "✅ Test 2 passed" << endl;
    }

    // Test case 3: Duplicate numbers
    {
        vector<int> nums = {3, 3};
        int target = 6;
        vector<int> expected = {0, 1};
        vector<int> result = solution.twoSum(nums, target);
        assert(areEqual(result, expected));
        cout << "✅ Test 3 passed" << endl;
    }

    // Edge case 1: Negative numbers
    {
        vector<int> nums = {-1, -2, -3, -4, -5};
        int target = -8;
        vector<int> expected = {2, 4}; // -3 + (-5) = -8
        vector<int> result = solution.twoSum(nums, target);
        assert(areEqual(result, expected));
        cout << "✅ Edge case 1 passed" << endl;
    }

    // Edge case 2: Zero target
    {
        vector<int> nums = {-3, 4, 3, 90};
        int target = 0;
        vector<int> expected = {0, 2}; // -3 + 3 = 0
        vector<int> result = solution.twoSum(nums, target);
        assert(areEqual(result, expected));
        cout << "✅ Edge case 2 passed" << endl;
    }

    cout << "🎉 All tests passed!" << endl;
}

// Performance test function
void runPerformanceTests()
{
    Solution solution;

    cout << "Running performance tests..." << endl;

    // Create a large input where the answer is at the end
    vector<int> largeNums;
    for (int i = 0; i < 10000; i++)
    {
        largeNums.push_back(i);
    }
    largeNums.push_back(1); // This will pair with nums[1] = 1 to make target = 2
    int target = 2;

    auto startTime = chrono::high_resolution_clock::now();
    vector<int> result = solution.twoSum(largeNums, target);
    auto endTime = chrono::high_resolution_clock::now();

    auto duration = chrono::duration_cast<chrono::microseconds>(endTime - startTime);
    double executionTimeMs = duration.count() / 1000.0; // Convert to milliseconds
    double executionTimeSec = executionTimeMs / 1000.0; // Convert to seconds

    cout << "⏱️  Execution time: " << fixed << setprecision(4) << executionTimeSec << " seconds (" << executionTimeMs << " ms)" << endl;
    assert(executionTimeMs < 1000.0); // Should be less than 1 second (1000ms)

    vector<int> expected = {0, 2};
    assert(areEqual(result, expected));

    cout << "✅ Performance tests passed!" << endl;
}

int main()
{
    runTests();
    runPerformanceTests();
    return 0;
}