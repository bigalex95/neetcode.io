# NeetCode 150 - Complete Problem Set

This repository contains **149 coding challenge problems** from the NeetCode 150 list, organized by category with comprehensive test templates in both **Python** and **C++**.

## 📋 Problem Overview

| Category                | Problems | Difficulty Distribution     |
| ----------------------- | -------- | --------------------------- |
| Arrays & Hashing        | 9        | Easy: 3, Medium: 6          |
| Two Pointers            | 5        | Easy: 1, Medium: 3, Hard: 1 |
| Sliding Window          | 6        | Easy: 1, Medium: 3, Hard: 2 |
| Stack                   | 7        | Easy: 1, Medium: 5, Hard: 1 |
| Binary Search           | 7        | Easy: 1, Medium: 5, Hard: 1 |
| Linked List             | 11       | Easy: 3, Medium: 6, Hard: 2 |
| Trees                   | 15       | Easy: 6, Medium: 7, Hard: 2 |
| Tries                   | 3        | Medium: 2, Hard: 1          |
| Heap & Priority Queue   | 7        | Easy: 2, Medium: 4, Hard: 1 |
| Backtracking            | 9        | Medium: 8, Hard: 1          |
| Graphs                  | 13       | Medium: 12, Hard: 1         |
| 1-D Dynamic Programming | 12       | Easy: 2, Medium: 10         |
| Intervals               | 5        | Easy: 1, Medium: 4          |
| Greedy                  | 8        | Medium: 8                   |
| Advanced Graphs         | 6        | Medium: 4, Hard: 2          |
| 2-D Dynamic Programming | 11       | Medium: 6, Hard: 5          |
| Bit Manipulation        | 7        | Easy: 5, Medium: 2          |
| Math & Geometry         | 8        | Easy: 2, Medium: 5, Hard: 1 |

**Total: 149 problems** (37 Easy, 93 Medium, 19 Hard)

## 🚀 Quick Start

### For C++ Solutions

1. **Build all problems:**

   ```bash
   ./build.sh
   ```

2. **Run all tests:**

   ```bash
   ./test.sh
   ```

3. **List available problems:**

   ```bash
   ./build.sh --list
   ./test.sh --list
   ```

4. **Build/test specific problem:**
   ```bash
   ./build.sh 1    # Build first problem
   ./test.sh 1     # Test first problem
   ```

### For Python Solutions

1. **Test all Python solutions:**

   ```bash
   ./test_python.sh
   ```

2. **List available Python problems:**

   ```bash
   ./test_python.sh --list
   ```

3. **Test specific Python problem:**
   ```bash
   ./test_python.sh 1    # Test first problem
   ```

## 📁 Project Structure

```
neetcode.io/
├── CMakeLists.txt                      # C++ build configuration
├── build.sh                           # C++ build script
├── test.sh                            # C++ test script
├── test_python.sh                     # Python test script
├── run.sh                             # C++ execution script
├── generate_problems.py               # Problem generator script
├── templates/                         # Template files
│   ├── template.py                    # Python template
│   ├── template.cpp                   # C++ template
│   ├── array_hashing_template.py     # Array/Hashing specific template
│   └── two_pointers_template.py      # Two Pointers specific template
│
├── Arrays & Hashing/                  # 9 problems
│   ├── contains_duplicate.py/.cpp
│   ├── valid_anagram.py/.cpp
│   ├── two_sum.py/.cpp
│   ├── group_anagrams.py/.cpp
│   ├── top_k_frequent_elements.py/.cpp
│   ├── product_of_array_except_self.py/.cpp
│   ├── valid_sudoku.py/.cpp
│   ├── encode_and_decode_strings.py/.cpp
│   └── longest_consecutive_sequence.py/.cpp
│
├── Two Pointers/                      # 5 problems
│   ├── valid_palindrome.py/.cpp
│   ├── two_sum_ii_input_array_is_sorted.py/.cpp
│   ├── 3sum.py/.cpp
│   ├── container_with_most_water.py/.cpp
│   └── trapping_rain_water.py/.cpp
│
├── Sliding Window/                    # 6 problems
│   ├── best_time_to_buy_and_sell_stock.py/.cpp
│   ├── longest_substring_without_repeating_characters.py/.cpp
│   ├── longest_repeating_character_replacement.py/.cpp
│   ├── permutation_in_string.py/.cpp
│   ├── minimum_window_substring.py/.cpp
│   └── sliding_window_maximum.py/.cpp
│
├── Stack/                             # 7 problems
│   ├── valid_parentheses.py/.cpp
│   ├── min_stack.py/.cpp
│   ├── evaluate_reverse_polish_notation.py/.cpp
│   ├── generate_parentheses.py/.cpp
│   ├── daily_temperatures.py/.cpp
│   ├── car_fleet.py/.cpp
│   └── largest_rectangle_in_histogram.py/.cpp
│
├── Binary Search/                     # 7 problems
│   ├── binary_search.py/.cpp
│   ├── search_a_2d_matrix.py/.cpp
│   ├── koko_eating_bananas.py/.cpp
│   ├── find_minimum_in_rotated_sorted_array.py/.cpp
│   ├── search_in_rotated_sorted_array.py/.cpp
│   ├── time_based_key_value_store.py/.cpp
│   └── median_of_two_sorted_arrays.py/.cpp
│
├── Linked List/                       # 11 problems
│   ├── reverse_linked_list.py/.cpp
│   ├── merge_two_sorted_lists.py/.cpp
│   ├── reorder_list.py/.cpp
│   ├── remove_nth_node_from_end_of_list.py/.cpp
│   ├── copy_list_with_random_pointer.py/.cpp
│   ├── add_two_numbers.py/.cpp
│   ├── linked_list_cycle.py/.cpp
│   ├── find_the_duplicate_number.py/.cpp
│   ├── lru_cache.py/.cpp
│   ├── merge_k_sorted_lists.py/.cpp
│   └── reverse_nodes_in_k_group.py/.cpp
│
├── Trees/                             # 15 problems
│   ├── invert_binary_tree.py/.cpp
│   ├── maximum_depth_of_binary_tree.py/.cpp
│   ├── diameter_of_binary_tree.py/.cpp
│   ├── balanced_binary_tree.py/.cpp
│   ├── same_tree.py/.cpp
│   ├── subtree_of_another_tree.py/.cpp
│   ├── lowest_common_ancestor_of_a_binary_search_tree.py/.cpp
│   ├── binary_tree_level_order_traversal.py/.cpp
│   ├── binary_tree_right_side_view.py/.cpp
│   ├── count_good_nodes_in_binary_tree.py/.cpp
│   ├── validate_binary_search_tree.py/.cpp
│   ├── kth_smallest_element_in_a_bst.py/.cpp
│   ├── construct_binary_tree_from_preorder_and_inorder_traversal.py/.cpp
│   ├── binary_tree_maximum_path_sum.py/.cpp
│   └── serialize_and_deserialize_binary_tree.py/.cpp
│
├── Tries/                             # 3 problems
│   ├── implement_trie_prefix_tree.py/.cpp
│   ├── design_add_and_search_words_data_structure.py/.cpp
│   └── word_search_ii.py/.cpp
│
├── Heap & Priority Queue/             # 7 problems
│   ├── kth_largest_element_in_a_stream.py/.cpp
│   ├── last_stone_weight.py/.cpp
│   ├── k_closest_points_to_origin.py/.cpp
│   ├── kth_largest_element_in_an_array.py/.cpp
│   ├── task_scheduler.py/.cpp
│   ├── design_twitter.py/.cpp
│   └── find_median_from_data_stream.py/.cpp
│
├── Backtracking/                      # 9 problems
│   ├── subsets.py/.cpp
│   ├── combination_sum.py/.cpp
│   ├── permutations.py/.cpp
│   ├── subsets_ii.py/.cpp
│   ├── combination_sum_ii.py/.cpp
│   ├── word_search.py/.cpp
│   ├── palindrome_partitioning.py/.cpp
│   ├── letter_combinations_of_a_phone_number.py/.cpp
│   └── n_queens.py/.cpp
│
├── Graphs/                            # 13 problems
│   ├── number_of_islands.py/.cpp
│   ├── clone_graph.py/.cpp
│   ├── max_area_of_island.py/.cpp
│   ├── pacific_atlantic_water_flow.py/.cpp
│   ├── surrounded_regions.py/.cpp
│   ├── rotting_oranges.py/.cpp
│   ├── walls_and_gates.py/.cpp
│   ├── course_schedule.py/.cpp
│   ├── course_schedule_ii.py/.cpp
│   ├── redundant_connection.py/.cpp
│   ├── number_of_connected_components_in_an_undirected_graph.py/.cpp
│   ├── graph_valid_tree.py/.cpp
│   └── word_ladder.py/.cpp
│
├── 1-D Dynamic Programming/           # 12 problems
│   ├── climbing_stairs.py/.cpp
│   ├── min_cost_climbing_stairs.py/.cpp
│   ├── house_robber.py/.cpp
│   ├── house_robber_ii.py/.cpp
│   ├── longest_palindromic_substring.py/.cpp
│   ├── palindromic_substrings.py/.cpp
│   ├── decode_ways.py/.cpp
│   ├── coin_change.py/.cpp
│   ├── maximum_product_subarray.py/.cpp
│   ├── word_break.py/.cpp
│   ├── longest_increasing_subsequence.py/.cpp
│   └── partition_equal_subset_sum.py/.cpp
│
├── Intervals/                         # 5 problems
│   ├── insert_interval.py/.cpp
│   ├── merge_intervals.py/.cpp
│   ├── non_overlapping_intervals.py/.cpp
│   ├── meeting_rooms.py/.cpp
│   └── meeting_rooms_ii.py/.cpp
│
├── Greedy/                            # 8 problems
│   ├── maximum_subarray.py/.cpp
│   ├── jump_game.py/.cpp
│   ├── jump_game_ii.py/.cpp
│   ├── gas_station.py/.cpp
│   ├── hand_of_straights.py/.cpp
│   ├── merge_triplets_to_form_target_triplet.py/.cpp
│   ├── partition_labels.py/.cpp
│   └── valid_parenthesis_string.py/.cpp
│
├── Advanced Graphs/                   # 6 problems
│   ├── reconstruct_itinerary.py/.cpp
│   ├── min_cost_to_connect_all_points.py/.cpp
│   ├── network_delay_time.py/.cpp
│   ├── swim_in_rising_water.py/.cpp
│   ├── alien_dictionary.py/.cpp
│   └── cheapest_flights_within_k_stops.py/.cpp
│
├── 2-D Dynamic Programming/           # 11 problems
│   ├── unique_paths.py/.cpp
│   ├── longest_common_subsequence.py/.cpp
│   ├── best_time_to_buy_and_sell_stock_with_cooldown.py/.cpp
│   ├── coin_change_ii.py/.cpp
│   ├── target_sum.py/.cpp
│   ├── interleaving_string.py/.cpp
│   ├── longest_increasing_path_in_a_matrix.py/.cpp
│   ├── distinct_subsequences.py/.cpp
│   ├── edit_distance.py/.cpp
│   ├── burst_balloons.py/.cpp
│   └── regular_expression_matching.py/.cpp
│
├── Bit Manipulation/                  # 7 problems
│   ├── single_number.py/.cpp
│   ├── number_of_1_bits.py/.cpp
│   ├── counting_bits.py/.cpp
│   ├── reverse_bits.py/.cpp
│   ├── missing_number.py/.cpp
│   ├── sum_of_two_integers.py/.cpp
│   └── reverse_integer.py/.cpp
│
└── Math & Geometry/                   # 8 problems
    ├── rotate_image.py/.cpp
    ├── spiral_matrix.py/.cpp
    ├── set_matrix_zeroes.py/.cpp
    ├── happy_number.py/.cpp
    ├── plus_one.py/.cpp
    ├── pow_x_n.py/.cpp
    ├── multiply_strings.py/.cpp
    └── detect_squares.py/.cpp
```

## 🛠️ Template Structure

Each problem includes:

### Python Template Features:

- ✅ Complete function signature placeholders
- ✅ Comprehensive test cases with assertions
- ✅ Performance testing framework
- ✅ Proper error handling and edge cases
- ✅ Type hints and documentation
- ✅ LeetCode and NeetCode links

### C++ Template Features:

- ✅ Modern C++17 standards
- ✅ Comprehensive header inclusions
- ✅ Helper functions for testing
- ✅ Performance testing framework
- ✅ Assert-based testing
- ✅ CMake integration for easy building

## 📊 Progress Tracking

Track your progress by implementing solutions in the template files. Each file contains:

- **Problem description placeholders** - Fill in from LeetCode/NeetCode
- **TODO sections** - Clear markers for what needs implementation
- **Test cases** - Ready-to-use test framework
- **Performance tests** - Validate efficiency of solutions

## 🔧 Development Workflow

1. **Choose a problem** from any category
2. **Read the problem description** from the provided LeetCode link
3. **Implement your solution** in the `solve()` method
4. **Update the test cases** with proper inputs/outputs
5. **Run tests** to validate your solution
6. **Optimize** if performance tests fail

## 📈 Recommended Study Order

1. **Arrays & Hashing** - Fundamental data structure operations
2. **Two Pointers** - Essential technique for array problems
3. **Sliding Window** - Optimize substring/subarray problems
4. **Stack** - LIFO operations and parentheses problems
5. **Binary Search** - Efficient searching algorithms
6. **Linked List** - Pointer manipulation and list operations
7. **Trees** - Tree traversal and manipulation
8. **Tries** - String prefix operations
9. **Heap & Priority Queue** - Priority-based operations
10. **Backtracking** - Recursive problem solving
11. **Graphs** - Graph traversal and algorithms
12. **1-D Dynamic Programming** - Fundamental DP concepts
13. **Intervals** - Interval manipulation and merging
14. **Greedy** - Optimal choice algorithms
15. **Advanced Graphs** - Complex graph algorithms
16. **2-D Dynamic Programming** - Advanced DP techniques
17. **Bit Manipulation** - Bitwise operations
18. **Math & Geometry** - Mathematical problem solving

## 🎯 Goals

- **Complete all 149 problems** with working solutions
- **Achieve optimal time complexity** for each solution
- **Master core algorithms and data structures**
- **Build systematic problem-solving skills**

## 📚 Resources

- [NeetCode Website](https://neetcode.io/)
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode](https://leetcode.com/)
- [NeetCode YouTube Channel](https://www.youtube.com/c/neetcode)

## 🤝 Contributing

Feel free to contribute by:

- Adding more detailed problem descriptions
- Improving test cases
- Adding alternative solution approaches
- Fixing bugs in templates

---

**Happy Coding!** 🚀 Master these 149 problems and you'll be well-prepared for any coding interview!
