#!/usr/bin/env python3

"""
NeetCode 150 Problem Generator
Generates Python and C++ template files for all NeetCode 150 problems
"""

import os
import re
from pathlib import Path

# NeetCode 150 problems organized by category
PROBLEMS = {
    'Arrays & Hashing': [
        ('Contains Duplicate', 217, 'Easy'),
        ('Valid Anagram', 242, 'Easy'),
        ('Two Sum', 1, 'Easy'),
        ('Group Anagrams', 49, 'Medium'),
        ('Top K Frequent Elements', 347, 'Medium'),
        ('Product of Array Except Self', 238, 'Medium'),
        ('Valid Sudoku', 36, 'Medium'),
        ('Encode and Decode Strings', 271, 'Medium'),
        ('Longest Consecutive Sequence', 128, 'Medium')
    ],
    'Two Pointers': [
        ('Valid Palindrome', 125, 'Easy'),
        ('Two Sum II Input Array Is Sorted', 167, 'Medium'),
        ('3Sum', 15, 'Medium'),
        ('Container With Most Water', 11, 'Medium'),
        ('Trapping Rain Water', 42, 'Hard')
    ],
    'Sliding Window': [
        ('Best Time to Buy And Sell Stock', 121, 'Easy'),
        ('Longest Substring Without Repeating Characters', 3, 'Medium'),
        ('Longest Repeating Character Replacement', 424, 'Medium'),
        ('Permutation In String', 567, 'Medium'),
        ('Minimum Window Substring', 76, 'Hard'),
        ('Sliding Window Maximum', 239, 'Hard')
    ],
    'Stack': [
        ('Valid Parentheses', 20, 'Easy'),
        ('Min Stack', 155, 'Medium'),
        ('Evaluate Reverse Polish Notation', 150, 'Medium'),
        ('Generate Parentheses', 22, 'Medium'),
        ('Daily Temperatures', 739, 'Medium'),
        ('Car Fleet', 853, 'Medium'),
        ('Largest Rectangle In Histogram', 84, 'Hard')
    ],
    'Binary Search': [
        ('Binary Search', 704, 'Easy'),
        ('Search a 2D Matrix', 74, 'Medium'),
        ('Koko Eating Bananas', 875, 'Medium'),
        ('Find Minimum In Rotated Sorted Array', 153, 'Medium'),
        ('Search In Rotated Sorted Array', 33, 'Medium'),
        ('Time Based Key Value Store', 981, 'Medium'),
        ('Median of Two Sorted Arrays', 4, 'Hard')
    ],
    'Linked List': [
        ('Reverse Linked List', 206, 'Easy'),
        ('Merge Two Sorted Lists', 21, 'Easy'),
        ('Reorder List', 143, 'Medium'),
        ('Remove Nth Node From End of List', 19, 'Medium'),
        ('Copy List With Random Pointer', 138, 'Medium'),
        ('Add Two Numbers', 2, 'Medium'),
        ('Linked List Cycle', 141, 'Easy'),
        ('Find The Duplicate Number', 287, 'Medium'),
        ('LRU Cache', 146, 'Medium'),
        ('Merge k Sorted Lists', 23, 'Hard'),
        ('Reverse Nodes In k Group', 25, 'Hard')
    ],
    'Trees': [
        ('Invert Binary Tree', 226, 'Easy'),
        ('Maximum Depth of Binary Tree', 104, 'Easy'),
        ('Diameter of Binary Tree', 543, 'Easy'),
        ('Balanced Binary Tree', 110, 'Easy'),
        ('Same Tree', 100, 'Easy'),
        ('Subtree of Another Tree', 572, 'Easy'),
        ('Lowest Common Ancestor of a Binary Search Tree', 235, 'Medium'),
        ('Binary Tree Level Order Traversal', 102, 'Medium'),
        ('Binary Tree Right Side View', 199, 'Medium'),
        ('Count Good Nodes In Binary Tree', 1448, 'Medium'),
        ('Validate Binary Search Tree', 98, 'Medium'),
        ('Kth Smallest Element In a Bst', 230, 'Medium'),
        ('Construct Binary Tree From Preorder And Inorder Traversal', 105, 'Medium'),
        ('Binary Tree Maximum Path Sum', 124, 'Hard'),
        ('Serialize And Deserialize Binary Tree', 297, 'Hard')
    ],
    'Tries': [
        ('Implement Trie Prefix Tree', 208, 'Medium'),
        ('Design Add And Search Words Data Structure', 211, 'Medium'),
        ('Word Search II', 212, 'Hard')
    ],
    'Heap & Priority Queue': [
        ('Kth Largest Element In a Stream', 703, 'Easy'),
        ('Last Stone Weight', 1046, 'Easy'),
        ('K Closest Points to Origin', 973, 'Medium'),
        ('Kth Largest Element In An Array', 215, 'Medium'),
        ('Task Scheduler', 621, 'Medium'),
        ('Design Twitter', 355, 'Medium'),
        ('Find Median From Data Stream', 295, 'Hard')
    ],
    'Backtracking': [
        ('Subsets', 78, 'Medium'),
        ('Combination Sum', 39, 'Medium'),
        ('Permutations', 46, 'Medium'),
        ('Subsets II', 90, 'Medium'),
        ('Combination Sum II', 40, 'Medium'),
        ('Word Search', 79, 'Medium'),
        ('Palindrome Partitioning', 131, 'Medium'),
        ('Letter Combinations of a Phone Number', 17, 'Medium'),
        ('N Queens', 51, 'Hard')
    ],
    'Graphs': [
        ('Number of Islands', 200, 'Medium'),
        ('Clone Graph', 133, 'Medium'),
        ('Max Area of Island', 695, 'Medium'),
        ('Pacific Atlantic Water Flow', 417, 'Medium'),
        ('Surrounded Regions', 130, 'Medium'),
        ('Rotting Oranges', 994, 'Medium'),
        ('Walls And Gates', 286, 'Medium'),
        ('Course Schedule', 207, 'Medium'),
        ('Course Schedule II', 210, 'Medium'),
        ('Redundant Connection', 684, 'Medium'),
        ('Number of Connected Components In An Undirected Graph', 323, 'Medium'),
        ('Graph Valid Tree', 261, 'Medium'),
        ('Word Ladder', 127, 'Hard')
    ],
    '1-D Dynamic Programming': [
        ('Climbing Stairs', 70, 'Easy'),
        ('Min Cost Climbing Stairs', 746, 'Easy'),
        ('House Robber', 198, 'Medium'),
        ('House Robber II', 213, 'Medium'),
        ('Longest Palindromic Substring', 5, 'Medium'),
        ('Palindromic Substrings', 647, 'Medium'),
        ('Decode Ways', 91, 'Medium'),
        ('Coin Change', 322, 'Medium'),
        ('Maximum Product Subarray', 152, 'Medium'),
        ('Word Break', 139, 'Medium'),
        ('Longest Increasing Subsequence', 300, 'Medium'),
        ('Partition Equal Subset Sum', 416, 'Medium')
    ],
    'Intervals': [
        ('Insert Interval', 57, 'Medium'),
        ('Merge Intervals', 56, 'Medium'),
        ('Non Overlapping Intervals', 435, 'Medium'),
        ('Meeting Rooms', 252, 'Easy'),
        ('Meeting Rooms II', 253, 'Medium')
    ],
    'Greedy': [
        ('Maximum Subarray', 53, 'Medium'),
        ('Jump Game', 55, 'Medium'),
        ('Jump Game II', 45, 'Medium'),
        ('Gas Station', 134, 'Medium'),
        ('Hand of Straights', 846, 'Medium'),
        ('Merge Triplets to Form Target Triplet', 1899, 'Medium'),
        ('Partition Labels', 763, 'Medium'),
        ('Valid Parenthesis String', 678, 'Medium')
    ],
    'Advanced Graphs': [
        ('Reconstruct Itinerary', 332, 'Hard'),
        ('Min Cost to Connect All Points', 1584, 'Medium'),
        ('Network Delay Time', 743, 'Medium'),
        ('Swim In Rising Water', 778, 'Hard'),
        ('Alien Dictionary', 269, 'Hard'),
        ('Cheapest Flights Within K Stops', 787, 'Medium')
    ],
    '2-D Dynamic Programming': [
        ('Unique Paths', 62, 'Medium'),
        ('Longest Common Subsequence', 1143, 'Medium'),
        ('Best Time to Buy And Sell Stock With Cooldown', 309, 'Medium'),
        ('Coin Change II', 518, 'Medium'),
        ('Target Sum', 494, 'Medium'),
        ('Interleaving String', 97, 'Medium'),
        ('Longest Increasing Path In a Matrix', 329, 'Hard'),
        ('Distinct Subsequences', 115, 'Hard'),
        ('Edit Distance', 72, 'Hard'),
        ('Burst Balloons', 312, 'Hard'),
        ('Regular Expression Matching', 10, 'Hard')
    ],
    'Bit Manipulation': [
        ('Single Number', 136, 'Easy'),
        ('Number of 1 Bits', 191, 'Easy'),
        ('Counting Bits', 338, 'Easy'),
        ('Reverse Bits', 190, 'Easy'),
        ('Missing Number', 268, 'Easy'),
        ('Sum of Two Integers', 371, 'Medium'),
        ('Reverse Integer', 7, 'Medium')
    ],
    'Math & Geometry': [
        ('Rotate Image', 48, 'Medium'),
        ('Spiral Matrix', 54, 'Medium'),
        ('Set Matrix Zeroes', 73, 'Medium'),
        ('Happy Number', 202, 'Easy'),
        ('Plus One', 66, 'Easy'),
        ('Pow(x, n)', 50, 'Medium'),
        ('Multiply Strings', 43, 'Hard'),
        ('Detect Squares', 2013, 'Medium')
    ]
}

def to_snake_case(text):
    """Convert text to snake_case for filenames"""
    # Remove special characters and replace with spaces
    text = re.sub(r'[^\w\s]', ' ', text)
    # Replace spaces with underscores and convert to lowercase
    text = re.sub(r'\s+', '_', text.strip()).lower()
    # Remove multiple consecutive underscores
    text = re.sub(r'_+', '_', text)
    return text

def generate_python_template(problem_name, leetcode_num, difficulty, category):
    """Generate Python template for a problem"""
    snake_name = to_snake_case(problem_name)
    
    return f'''"""
{problem_name}
LeetCode #{leetcode_num}: https://leetcode.com/problems/{snake_name.replace('_', '-')}/
NeetCode: https://neetcode.io/problems/{snake_name.replace('_', '-')}

Difficulty: {difficulty}
Category: {category}

Problem:
TODO: Add problem description

Example 1:
TODO: Add example

Example 2:
TODO: Add example

Constraints:
TODO: Add constraints

Time Complexity: TODO
Space Complexity: TODO
"""

from typing import List, Optional, Dict, Set, Tuple, Any
import time


class Solution:
    def solve(self, *args) -> Any:
        """
        TODO: Add method description
        
        Args:
            TODO: Add parameter descriptions
            
        Returns:
            TODO: Add return description
        """
        # TODO: Implement solution here
        pass


def test_solution():
    """Test cases for {problem_name}"""
    solution = Solution()
    
    # Test case 1: Basic functionality
    # TODO: Add test case 1
    # input1 = 
    # expected1 = 
    # result1 = solution.solve(input1)
    # assert result1 == expected1, f"Test 1 failed: expected {{expected1}}, got {{result1}}"
    
    # Test case 2: Edge case
    # TODO: Add test case 2
    # input2 = 
    # expected2 = 
    # result2 = solution.solve(input2)
    # assert result2 == expected2, f"Test 2 failed: expected {{expected2}}, got {{result2}}"
    
    # Test case 3: Another test case
    # TODO: Add test case 3
    # input3 = 
    # expected3 = 
    # result3 = solution.solve(input3)
    # assert result3 == expected3, f"Test 3 failed: expected {{expected3}}, got {{result3}}"
    
    print("✅ All test cases passed!")


def test_performance():
    """Performance test for large inputs"""
    solution = Solution()
    
    # TODO: Add performance test cases
    # Large input test
    # start_time = time.time()
    # result = solution.solve(large_input)
    # end_time = time.time()
    # execution_time = end_time - start_time
    # assert execution_time < 1.0, f"Solution took too long: {{execution_time:.4f}} seconds"
    
    print("✅ Performance test passed!")


if __name__ == "__main__":
    test_solution()
    test_performance()
'''

def generate_cpp_template(problem_name, leetcode_num, difficulty, category):
    """Generate C++ template for a problem"""
    snake_name = to_snake_case(problem_name)
    
    return f'''/*
{problem_name}
LeetCode #{leetcode_num}: https://leetcode.com/problems/{snake_name.replace('_', '-')}/
NeetCode: https://neetcode.io/problems/{snake_name.replace('_', '-')}

Difficulty: {difficulty}
Category: {category}

Problem:
TODO: Add problem description

Example 1:
TODO: Add example

Example 2:
TODO: Add example

Constraints:
TODO: Add constraints

Time Complexity: TODO
Space Complexity: TODO
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

using namespace std;

class Solution {{
public:
    // TODO: Replace with actual function signature
    auto solve() -> auto {{
        // TODO: Implement solution
        return 0;
    }}
}};

// Helper function to compare vectors (for testing)
template<typename T>
bool areEqual(const vector<T>& a, const vector<T>& b) {{
    if (a.size() != b.size()) return false;
    for (size_t i = 0; i < a.size(); i++) {{
        if (a[i] != b[i]) return false;
    }}
    return true;
}}

// Helper function to print vector
template<typename T>
void printVector(const vector<T>& vec) {{
    cout << "[";
    for (size_t i = 0; i < vec.size(); i++) {{
        cout << vec[i];
        if (i < vec.size() - 1) cout << ", ";
    }}
    cout << "]";
}}

// Test function
void runTests() {{
    Solution solution;

    cout << "Running tests for {problem_name}..." << endl;

    // Test case 1: Basic functionality
    {{
        // TODO: Define test inputs and expected output
        // auto input = ;
        // auto expected = ;
        // auto result = solution.solve(input);
        // assert(result == expected);
        cout << "✅ Test 1 passed" << endl;
    }}

    // Test case 2: Edge case
    {{
        // TODO: Define test inputs and expected output
        // auto input = ;
        // auto expected = ;
        // auto result = solution.solve(input);
        // assert(result == expected);
        cout << "✅ Test 2 passed" << endl;
    }}

    // Test case 3: Another test case
    {{
        // TODO: Define test inputs and expected output
        // auto input = ;
        // auto expected = ;
        // auto result = solution.solve(input);
        // assert(result == expected);
        cout << "✅ Test 3 passed" << endl;
    }}

    cout << "🎉 All tests passed!" << endl;
}}

// Performance test function
void runPerformanceTests() {{
    Solution solution;
    
    cout << "Running performance tests..." << endl;
    
    // TODO: Add performance test cases here
    // Example:
    // auto start = chrono::high_resolution_clock::now();
    // auto result = solution.solve(large_input);
    // auto end = chrono::high_resolution_clock::now();
    // auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);
    // assert(duration.count() < 1000); // Should complete within 1 second
    
    cout << "✅ Performance tests passed!" << endl;
}}

int main() {{
    runTests();
    runPerformanceTests();
    return 0;
}}
'''

def create_directory_if_not_exists(path):
    """Create directory if it doesn't exist"""
    Path(path).mkdir(parents=True, exist_ok=True)

def generate_all_problems():
    """Generate all NeetCode 150 problems"""
    base_dir = Path.cwd()
    
    total_problems = 0
    
    for category, problems in PROBLEMS.items():
        print(f"Generating {category} problems...")
        
        # Create category directory
        category_dir = base_dir / category
        create_directory_if_not_exists(category_dir)
        
        for problem_name, leetcode_num, difficulty in problems:
            # Generate filename
            filename = to_snake_case(problem_name)
            
            # Generate Python file
            python_content = generate_python_template(problem_name, leetcode_num, difficulty, category)
            python_path = category_dir / f"{filename}.py"
            
            # Only create file if it doesn't exist
            if not python_path.exists():
                with open(python_path, 'w') as f:
                    f.write(python_content)
                print(f"  Created: {python_path}")
            else:
                print(f"  Skipped: {python_path} (already exists)")
            
            # Generate C++ file
            cpp_content = generate_cpp_template(problem_name, leetcode_num, difficulty, category)
            cpp_path = category_dir / f"{filename}.cpp"
            
            # Only create file if it doesn't exist
            if not cpp_path.exists():
                with open(cpp_path, 'w') as f:
                    f.write(cpp_content)
                print(f"  Created: {cpp_path}")
            else:
                print(f"  Skipped: {cpp_path} (already exists)")
            
            total_problems += 1
    
    print(f"\\nGenerated {total_problems} problems across {len(PROBLEMS)} categories!")
    print("\\nNext steps:")
    print("1. Update CMakeLists.txt to include new C++ problems")
    print("2. Run ./build.sh to compile C++ solutions")
    print("3. Run ./test.sh to test C++ solutions")
    print("4. Run ./test_python.sh to test Python solutions")

if __name__ == "__main__":
    generate_all_problems()