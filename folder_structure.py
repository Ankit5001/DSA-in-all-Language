import os
import re

def create_numbered_dsa_folder_structure_with_data(data):
    """
    Creates a numbered folder structure for the Dsa repository based on provided data,
    maintaining the order of topics and questions as given in the input and adding numbers to folders and files.

    Args:
        data: A list of dictionaries, where each dictionary contains:
              - "topic": The topic folder name.
              - "question_name": The question name to be used as filename.
    """
    root_folder = "Dsa_Numbered" # Changed root folder name to "Dsa_Numbered" to differentiate
    language_folders = ["python", "c", "c++", "java", "javascript"]

    # Create the root folder if it doesn't exist
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)
        print(f"Created root folder: {root_folder}")
    else:
        print(f"Root folder '{root_folder}' already exists.")

    # Create language folders and topic/file structure
    for language_folder in language_folders:
        language_path = os.path.join(root_folder, language_folder)
        if not os.path.exists(language_path):
            os.makedirs(language_path)
            print(f"  Created language folder: {language_folder}")
        else:
            print(f"  Language folder '{language_folder}' already exists.")

        # Create topic folders and files based on data
        topic_counter = 1 # Initialize topic counter
        current_topic = None # Track current topic to avoid redundant folder creation

        for item in data: # Iterate through data in the given order
            topic_name = item["topic"]
            question_name = item["question_name"]

            if topic_name != current_topic: # Check if topic has changed
                numbered_topic_name = f"{topic_counter}-{topic_name}" # Add number to topic folder name
                topic_path = os.path.join(language_path, numbered_topic_name)
                if not os.path.exists(topic_path):
                    os.makedirs(topic_path)
                    print(f"    Created topic folder: {numbered_topic_name} in {language_folder}")
                else:
                    print(f"    Topic folder '{numbered_topic_name}' already exists in {language_folder}")
                current_topic = topic_name # Update current topic
                question_counter = 1 # Reset question counter for new topic
                topic_counter += 1 # Increment topic counter

            else: # If topic is the same, use existing topic path
                numbered_topic_name = f"{topic_counter - 1}-{topic_name}" # Use previous topic counter
                topic_path = os.path.join(language_path, numbered_topic_name)


            # Create file in each language folder with respective extension
            file_extension = {
                "python": ".py",
                "c": ".c",
                "c++": ".cpp",
                "java": ".java",
                "javascript": ".js"
            }
            # Replace invalid characters with hyphen and spaces with underscores for filename
            file_name_base = re.sub(r'[<>:"/\\|?*]', '-', question_name) # Replace invalid characters
            numbered_question_name = f"{question_counter}-{file_name_base}" # Add number to question file name
            file_name = numbered_question_name.replace(" ", "_") + file_extension[language_folder]
            file_path = os.path.join(topic_path, file_name)

            if not os.path.exists(file_path):
                open(file_path, 'w').close() # Create empty file
                print(f"      Created file: {file_name} in {numbered_topic_name}/{language_folder}")
            else:
                print(f"      File '{file_name}' already exists in {numbered_topic_name}/{language_folder}")
            question_counter += 1 # Increment question counter


    print("DSA folder structure creation complete with numbered topics and files, maintaining question order.")

if __name__ == "__main__":
    data = [
        {"topic": "Arrays", "question_name": "Maximum and Minimum Element in an Array"},
        {"topic": "Arrays", "question_name": "Reverse the Array"},
        {"topic": "Arrays", "question_name": "Maximum-Subarray"},
        {"topic": "Arrays", "question_name": "Contains Duplicate"},
        {"topic": "Arrays", "question_name": "Chocolate Distribution Problem"},
        {"topic": "Arrays", "question_name": "Search in Rotated Sorted Array"},
        {"topic": "Arrays", "question_name": "Next Permutation"},
        {"topic": "Arrays", "question_name": "Best time to Buy and Sell Stock"},
        {"topic": "Arrays", "question_name": "Repeat and Missing Number Array"},
        {"topic": "Arrays", "question_name": "Kth-Largest Element in an Array"},
        {"topic": "Arrays", "question_name": "Trapping Rain Water"},
        {"topic": "Arrays", "question_name": "Product of Array Except Self"},
        {"topic": "Arrays", "question_name": "Maximum Product Subarray"},
        {"topic": "Arrays", "question_name": "Find Minimum in Rotated Sorted Array"},
        {"topic": "Arrays", "question_name": "Find Pair with Sum in Sorted & Rotated Array"},
        {"topic": "Arrays", "question_name": "3Sum"},
        {"topic": "Arrays", "question_name": "Container With Most Water"},
        {"topic": "Arrays", "question_name": "Given Sum Pair"},
        {"topic": "Arrays", "question_name": "Kth - Smallest Element"},
        {"topic": "Arrays", "question_name": "Merge Overlapping Intervals"},
        {"topic": "Arrays", "question_name": "Find Minimum Number of Merge Operations to Make an Array Palindrome"},
        {"topic": "Arrays", "question_name": "Given an Array of Numbers Arrange the Numbers to Form the Biggest Number"},
        {"topic": "Arrays", "question_name": "Space Optimization Using Bit Manipulations"},
        {"topic": "Arrays", "question_name": "Subarray Sum Divisible K"},
        {"topic": "Arrays", "question_name": "Print all Possible Combinations of r Elements in a Given Array of Size n"},
        {"topic": "Arrays", "question_name": "Mo's Algorithm"},
        {"topic": "Strings", "question_name": "Valid Palindrome"},
        {"topic": "Strings", "question_name": "Valid Anagram"},
        {"topic": "Strings", "question_name": "Valid parentheses"},
        {"topic": "Strings", "question_name": "Remove Consecutive Characters"},
        {"topic": "Strings", "question_name": "Longest Common Prefix"},
        {"topic": "Strings", "question_name": "Convert a Sentence into its Equivalent Mobile Numeric Keypad Sequence"},
        {"topic": "Strings", "question_name": "Print all the Duplicates in the Input String"},
        {"topic": "Strings", "question_name": "Longest Substring without Repeating Characters"},
        {"topic": "Strings", "question_name": "Longest Repeating Character Replacement"},
        {"topic": "Strings", "question_name": "Group Anagrams"},
        {"topic": "Strings", "question_name": "Longest Palindromic Substring"},
        {"topic": "Strings", "question_name": "Palindromic Substrings"},
        {"topic": "Strings", "question_name": "Next Permutation"},
        {"topic": "Strings", "question_name": "Count Palindromic Subsequences"},
        {"topic": "Strings", "question_name": "Smallest Window in a String Containing all the Characters of Another String"},
        {"topic": "Strings", "question_name": "Wildcard String Matching"},
        {"topic": "Strings", "question_name": "Longest Prefix Suffix"},
        {"topic": "Strings", "question_name": "Rabin-Karp Algorithm for Pattern Searching"},
        {"topic": "Strings", "question_name": "Transform One String to Another using Minimum Number of Given Operation"},
        {"topic": "Strings", "question_name": "Minimum Window Substring"},
        {"topic": "Strings", "question_name": "Boyer Moore Algorithm for Pattern Searching"},
        {"topic": "Strings", "question_name": "Word Wrap"},
        {"topic": "2D Arrays", "question_name": "Zigzag (or diagonal) Traversal of Matrix"},
        {"topic": "2D Arrays", "question_name": "Set Matrix Zeroes"},
        {"topic": "2D Arrays", "question_name": "Spiral Matrix"},
        {"topic": "2D Arrays", "question_name": "Rotate Image"},
        {"topic": "2D Arrays", "question_name": "Word Search"},
        {"topic": "2D Arrays", "question_name": "Find the Number of Islands | Set 1 (Using DFS)"},
        {"topic": "2D Arrays", "question_name": "Given a Matrix of ‘O’ and ‘X’, Replace ‘O’ with ‘X’ if Surrounded by ‘X’"},
        {"topic": "2D Arrays", "question_name": "Find a Common Element in all Rows of a Given Row-Wise Sorted Matrix"},
        {"topic": "2D Arrays", "question_name": "Create a Matrix with Alternating Rectangles of O and X"},
        {"topic": "2D Arrays", "question_name": "Maximum Size Rectangle of all 1s"},
        {"topic": "Searching & Sorting", "question_name": "Permute Two Arrays such that Sum of Every Pair is Greater or Equal to K"},
        {"topic": "Searching & Sorting", "question_name": "counting sort"},
        {"topic": "Searching & Sorting", "question_name": "find common elements three sorted arrays"},
        {"topic": "Searching & Sorting", "question_name": "Searching in an array where adjacent differ by at most k"},
        {"topic": "Searching & Sorting", "question_name": "ceiling in a sorted array"},
        {"topic": "Searching & Sorting", "question_name": "Piar with given difference"},
        {"topic": "Searching & Sorting", "question_name": "majority element"},
        {"topic": "Searching & Sorting", "question_name": "count triplets with sum smaller that a given value"},
        {"topic": "Searching & Sorting", "question_name": "Maximum Sum Subsequence with no adjacent elements"},
        {"topic": "Searching & Sorting", "question_name": "Merge Sorted Arrays using O(1) Space"},
        {"topic": "Searching & Sorting", "question_name": "Inversion of Array"},
        {"topic": "Searching & Sorting", "question_name": "Find Duplicates in O(n) Time and O(1) Extra Space"},
        {"topic": "Searching & Sorting", "question_name": "Radix Sort"},
        {"topic": "Searching & Sorting", "question_name": "Product of Array except itself"},
        {"topic": "Searching & Sorting", "question_name": "Make all Array Elements Equal"},
        {"topic": "Searching & Sorting", "question_name": "Check if Reversing a Sub Array Make the Array Sorted"},
        {"topic": "Searching & Sorting", "question_name": "Find Four Elements that Sum to a Given Value"},
        {"topic": "Searching & Sorting", "question_name": "Median of Two Sorted Array with Different Size"},
        {"topic": "Searching & Sorting", "question_name": "Median of Stream of Integers Running Integers"},
        {"topic": "Searching & Sorting", "question_name": "Print Subarrays with 0 Sum"},
        {"topic": "Searching & Sorting", "question_name": "Aggressive Cows"},
        {"topic": "Searching & Sorting", "question_name": "Allocate Minimum number of Pages"},
        {"topic": "Searching & Sorting", "question_name": "Minimum Swaps to Sort"},
        {"topic": "Backtracking", "question_name": "Backtracking Set 2 Rat in a Maze"},
        {"topic": "Backtracking", "question_name": "Combinational Sum"},
        {"topic": "Backtracking", "question_name": "Crossword-Puzzle"},
        {"topic": "Backtracking", "question_name": "Longest Possible Route in a Matrix with Hurdles"},
        {"topic": "Backtracking", "question_name": "Printing all solutions in N-Queen Problem"},
        {"topic": "Backtracking", "question_name": "Solve the Sudoku"},
        {"topic": "Backtracking", "question_name": "Partition Equal Subset Sum"},
        {"topic": "Backtracking", "question_name": "M Coloring Problem"},
        {"topic": "Backtracking", "question_name": "Knight Tour"},
        {"topic": "Backtracking", "question_name": "Sudoku"},
        {"topic": "Backtracking", "question_name": "Remove Invalid Parentheses"},
        {"topic": "Backtracking", "question_name": "Word Break Problem using Backtracking"},
        {"topic": "Backtracking", "question_name": "Print all Palindromic Partitions of a String"},
        {"topic": "Backtracking", "question_name": "Find Shortest Safe Route in a Path with Landmines"},
        {"topic": "Backtracking", "question_name": "Partition of Set into K Subsets with Equal Sum"},
        {"topic": "Backtracking", "question_name": "Backtracking set-7 hamiltonian cycle"},
        {"topic": "Backtracking", "question_name": "tug-of-war"},
        {"topic": "Backtracking", "question_name": "Maximum Possible Number by doing at most K swaps"},
        {"topic": "Backtracking", "question_name": "Backtracking set-8 solving cryptarithmetic puzzles"},
        {"topic": "Backtracking", "question_name": "Find paths from corner cell to middle cell in maze"},
        {"topic": "Backtracking", "question_name": "Arithmetic Expressions"},
        {"topic": "Linked List", "question_name": "Reverse Linked List"},
        {"topic": "Linked List", "question_name": "Linked List Cycle"},
        {"topic": "Linked List", "question_name": "Merge Two Sorted Lists"},
        {"topic": "Linked List", "question_name": "Delete without Head node"},
        {"topic": "Linked List", "question_name": "Remove duplicates from an unsorted linked list"},
        {"topic": "Linked List", "question_name": "Sort a linked list of 0s-1s-or-2s"},
        {"topic": "Linked List", "question_name": "Multiply two numbers represented linked lists"},
        {"topic": "Linked List", "question_name": "Remove nth node from end of list"},
        {"topic": "Linked List", "question_name": "Reorder List"},
        {"topic": "Linked List", "question_name": "Detect and remove loop in a linked list"},
        {"topic": "Linked List", "question_name": "Write a Function to get the Intersection Point of two Linked Lists"},
        {"topic": "Linked List", "question_name": "Flatten a linked list with next and child pointers"},
        {"topic": "Linked List", "question_name": "Linked list in zig-zag fashion"},
        {"topic": "Linked List", "question_name": "Reverse a doubly linked list"},
        {"topic": "Linked List", "question_name": "Delete nodes which have a greater value on right side"},
        {"topic": "Linked List", "question_name": "Segregate even and odd Elements in a Linked List"},
        {"topic": "Linked List", "question_name": "Point to next higher value node in a linked list with an Arbitrary Pointer"},
        {"topic": "Linked List", "question_name": "Rearrange a given linked list in place"},
        {"topic": "Linked List", "question_name": "Sort Biotonic Doubly Linked Lists"},
        {"topic": "Linked List", "question_name": "Merge K Sorted Lists"},
        {"topic": "Linked List", "question_name": "Merge sort for linked list"},
        {"topic": "Linked List", "question_name": "Quicksort on singly-linked list"},
        {"topic": "Linked List", "question_name": "Sum of two linked lists"},
        {"topic": "Linked List", "question_name": "Flattening a linked list"},
        {"topic": "Linked List", "question_name": "Clone a linked list with next and random Pointer"},
        {"topic": "Linked List", "question_name": "Subtract two numbers represented as linked lists"},
        {"topic": "Stacks & Queues", "question_name": "Implement two stacks in an Array"},
        {"topic": "Stacks & Queues", "question_name": "Evaluation of Postfix Expression"},
        {"topic": "Stacks & Queues", "question_name": "Implement Stack using Queues"},
        {"topic": "Stacks & Queues", "question_name": "Queue Reversal"},
        {"topic": "Stacks & Queues", "question_name": "Implement Stack Queue using Deque"},
        {"topic": "Stacks & Queues", "question_name": "Reverse first k elements of queue"},
        {"topic": "Stacks & Queues", "question_name": "Design Stack with Middle Operation"},
        {"topic": "Stacks & Queues", "question_name": "Infix to Postfix"},
        {"topic": "Stacks & Queues", "question_name": "Design and Implement Special stack"},
        {"topic": "Stacks & Queues", "question_name": "Longest Valid String"},
        {"topic": "Stacks & Queues", "question_name": "Find if an expression has duplicate parenthesis or not"},
        {"topic": "Stacks & Queues", "question_name": "Stack permutations check if an array is stack permutation of other"},
        {"topic": "Stacks & Queues", "question_name": "Count natural numbers whose permutation greater number"},
        {"topic": "Stacks & Queues", "question_name": "Sort a stack using Recursion"},
        {"topic": "Stacks & Queues", "question_name": "Queue based approach for first non repeating character in a stream"},
        {"topic": "Stacks & Queues", "question_name": "The Celebrity Problem"},
        {"topic": "Stacks & Queues", "question_name": "Next larger Element"},
        {"topic": "Stacks & Queues", "question_name": "Distance of nearest cell"},
        {"topic": "Stacks & Queues", "question_name": "Rotten-oranges"},
        {"topic": "Stacks & Queues", "question_name": "Next smaller element"},
        {"topic": "Stacks & Queues", "question_name": "Circular-tour"},
        {"topic": "Stacks & Queues", "question_name": "Efficiently implement k-stacks single array"},
        {"topic": "Stacks & Queues", "question_name": "The celebrity problem"},
        {"topic": "Stacks & Queues", "question_name": "Iterative tower of hanoi"},
        {"topic": "Stacks & Queues", "question_name": "Find the maximum of minimums for every window size in a given array"},
        {"topic": "Stacks & Queues", "question_name": "lru cache implementation"},
        {"topic": "Stacks & Queues", "question_name": "Find a tour that visits all stations"},
        {"topic": "Greedy", "question_name": "Activity selection problem greedy algo"},
        {"topic": "Greedy", "question_name": "Greedy algorithm to find minimum number of coins"},
        {"topic": "Greedy", "question_name": "Minimum sum two numbers formed digits array-2"},
        {"topic": "Greedy", "question_name": "Minimum sum absolute difference pairs two arrays"},
        {"topic": "Greedy", "question_name": "Find maximum height pyramid from the given array of objects"},
        {"topic": "Greedy", "question_name": "Minimum cost for acquiring all coins with k extra coins allowed with every coin"},
        {"topic": "Greedy", "question_name": "Find maximum equal sum of every three stacks"},
        {"topic": "Greedy", "question_name": "Job sequencing problem"},
        {"topic": "Greedy", "question_name": "Greedy algorithm egyptian fraction"},
        {"topic": "Greedy", "question_name": "Fractional knapsack problem"},
        {"topic": "Greedy", "question_name": "Maximum length chain of pairs"},
        {"topic": "Greedy", "question_name": "Find smallest number with given number of digits and digit sum"},
        {"topic": "Greedy", "question_name": "Maximize sum of consecutive differences circular-array"},
        {"topic": "Greedy", "question_name": "paper-cut minimum number squares"},
        {"topic": "Greedy", "question_name": "Lexicographically smallest array-k consecutive swaps"},
        {"topic": "Greedy", "question_name": "Problems-CHOCOLA"},
        {"topic": "Greedy", "question_name": "Find minimum time to finish all jobs with given constraints"},
        {"topic": "Greedy", "question_name": "Job sequencing using disjoint set union"},
        {"topic": "Greedy", "question_name": "Rearrange characters string such that no two adjacent are same"},
        {"topic": "Greedy", "question_name": "Minimum edges to reverse to make path from a source to a destination"},
        {"topic": "Greedy", "question_name": "Minimize Cash Flow among a given set of friends who have borrowed money from each other"},
        {"topic": "Greedy", "question_name": "Minimum Cost to cut a board into squares"},
        {"topic": "Binary Trees", "question_name": "Maximum Depth of Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Reverse Level Order Traversal"},
        {"topic": "Binary Trees", "question_name": "Subtree of Another Tree"},
        {"topic": "Binary Trees", "question_name": "Invert Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Binary Tree Level Order Traversal"},
        {"topic": "Binary Trees", "question_name": "Left View of Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Right View of Binary Tree"},
        {"topic": "Binary Trees", "question_name": "ZigZag Tree Traversal"},
        {"topic": "Binary Trees", "question_name": "Create a mirror tree from the given binary tree"},
        {"topic": "Binary Trees", "question_name": "Leaf at same level"},
        {"topic": "Binary Trees", "question_name": "Check for Balanced Tree"},
        {"topic": "Binary Trees", "question_name": "Transform to Sum Tree"},
        {"topic": "Binary Trees", "question_name": "Check if Tree is Isomorphic"},
        {"topic": "Binary Trees", "question_name": "Same Tree"},
        {"topic": "Binary Trees", "question_name": "Construct Binary Tree from Preorder and Inorder Traversal"},
        {"topic": "Binary Trees", "question_name": "Height of Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Diameter of a Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Top View of Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Bottom View of Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Diagonal Traversal of Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Boundary Traversal of binary tree"},
        {"topic": "Binary Trees", "question_name": "Construct Binary Tree from String with Brackets"},
        {"topic": "Binary Trees", "question_name": "Minimum swap required to convert binary tree to binary search tree"},
        {"topic": "Binary Trees", "question_name": "Duplicate subtree in Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Check if a given graph is tree or not"},
        {"topic": "Binary Trees", "question_name": "Lowest Common Ancestor in a Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Min distance between two given nodes of a Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Duplicate Subtrees"},
        {"topic": "Binary Trees", "question_name": "Kth ancestor of a node in binary tree"},
        {"topic": "Binary Trees", "question_name": "Binary Tree Maximum Path Sum"},
        {"topic": "Binary Trees", "question_name": "Serialize and Deserialize Binary Tree"},
        {"topic": "Binary Trees", "question_name": "Binary Tree to DLL"},
        {"topic": "Binary Trees", "question_name": "Print all k-sum paths in a binary tree"},
        {"topic": "Binary Search Trees", "question_name": "Lowest Common Ancestor of a Binary Search Tree"},
        {"topic": "Binary Search Trees", "question_name": "Binary Search Tree | Set 1 (Search and Insertion)"},
        {"topic": "Binary Search Trees", "question_name": "Minimum element in BST"},
        {"topic": "Binary Search Trees", "question_name": "Predecessor and Successor"},
        {"topic": "Binary Search Trees", "question_name": "Check whether BST contains Dead End"},
        {"topic": "Binary Search Trees", "question_name": "Binary Tree to BST"},
        {"topic": "Binary Search Trees", "question_name": "Kth largest element in BST"},
        {"topic": "Binary Search Trees", "question_name": "Validate Binary Search Tree"},
        {"topic": "Binary Search Trees", "question_name": "Kth Smallest Element in a BST"},
        {"topic": "Binary Search Trees", "question_name": "Delete Node in a BST"},
        {"topic": "Binary Search Trees", "question_name": "Flatten BST to sorted list"},
        {"topic": "Binary Search Trees", "question_name": "Preorder to Postorder"},
        {"topic": "Binary Search Trees", "question_name": "Count BST nodes that lie in a given range"},
        {"topic": "Binary Search Trees", "question_name": "Populate Inorder Successor for all Nodes"},
        {"topic": "Binary Search Trees", "question_name": "Convert Normal BST to Balanced BST"},
        {"topic": "Binary Search Trees", "question_name": "Merge two BSTs"},
        {"topic": "Binary Search Trees", "question_name": "Given n appointments, find all conflicting appointments"},
        {"topic": "Binary Search Trees", "question_name": "Replace every element"},
        {"topic": "Binary Search Trees", "question_name": "Construct BST from given preorder traversal"},
        {"topic": "Binary Search Trees", "question_name": "Find median of BST in O(n) time and O(1) space"},
        {"topic": "Binary Search Trees", "question_name": "Largest BST in a Binary Tree"},
        {"topic": "Heaps & Hashing", "question_name": "Choose k array elements such that difference of maximum and minimum is minimized"},
        {"topic": "Heaps & Hashing", "question_name": "Heap Sort"},
        {"topic": "Heaps & Hashing", "question_name": "Top K Frequent Elements"},
        {"topic": "Heaps & Hashing", "question_name": "k largest elements in an array"},
        {"topic": "Heaps & Hashing", "question_name": "Next Greater Element"},
        {"topic": "Heaps & Hashing", "question_name": "K’th Smallest/Largest Element in Unsorted Array"},
        {"topic": "Heaps & Hashing", "question_name": "Find the maximum repeating number in O(n) time and O(1) extra space"},
        {"topic": "Heaps & Hashing", "question_name": "K-th smallest element after removing some integers from natural numbers"},
        {"topic": "Heaps & Hashing", "question_name": "Find k closest elements to a given value"},
        {"topic": "Heaps & Hashing", "question_name": "K’th largest element in a stream"},
        {"topic": "Heaps & Hashing", "question_name": "Connect Ropes"},
        {"topic": "Heaps & Hashing", "question_name": "Cuckoo Hashing"},
        {"topic": "Heaps & Hashing", "question_name": "Itinerary from a List of Tickets"},
        {"topic": "Heaps & Hashing", "question_name": "Largest Subarray with 0 Sum"},
        {"topic": "Heaps & Hashing", "question_name": "Count distinct elements in every window of size  k"},
        {"topic": "Heaps & Hashing", "question_name": "Group Shifted Strings"},
        {"topic": "Heaps & Hashing", "question_name": "Merge K Sorted lists"},
        {"topic": "Heaps & Hashing", "question_name": "Find Median from Data Stream"},
        {"topic": "Heaps & Hashing", "question_name": "Sliding Window Maximum"},
        {"topic": "Heaps & Hashing", "question_name": "Find the smallest positive number"},
        {"topic": "Heaps & Hashing", "question_name": "Find Surpasser Count of each element in array"},
        {"topic": "Heaps & Hashing", "question_name": "Tournament Tree and Binary Heap"},
        {"topic": "Heaps & Hashing", "question_name": "Check for palindrome"},
        {"topic": "Heaps & Hashing", "question_name": "Length of the largest subarray with contiguous elements"},
        {"topic": "Heaps & Hashing", "question_name": "Palindrome Substring Queries"},
        {"topic": "Heaps & Hashing", "question_name": "Subarray distinct elements"},
        {"topic": "Heaps & Hashing", "question_name": "Find the recurring function"},
        {"topic": "Heaps & Hashing", "question_name": "K maximum sum combinations from two arrays"},
        {"topic": "Graphs", "question_name": "BFS"},
        {"topic": "Graphs", "question_name": "DFS"},
        {"topic": "Graphs", "question_name": "Flood Fill Algorithm"},
        {"topic": "Graphs", "question_name": "Number of Triangles"},
        {"topic": "Graphs", "question_name": "Detect cycle in a graph"},
        {"topic": "Graphs", "question_name": "Detect cycle in an undirected graph"},
        {"topic": "Graphs", "question_name": "Rat in a Maze Problem"},
        {"topic": "Graphs", "question_name": "Steps by Knight"},
        {"topic": "Graphs", "question_name": "Clone graph"},
        {"topic": "Graphs", "question_name": "Number of Operations to Make Network Connected"},
        {"topic": "Graphs", "question_name": "Dijkstra’s shortest path algorithm"},
        {"topic": "Graphs", "question_name": "Topological Sort"},
        {"topic": "Graphs", "question_name": "Oliver and the Game"},
        {"topic": "Graphs", "question_name": "Minimum time taken by each job to be completed given by a Directed Acyclic Graph"},
        {"topic": "Graphs", "question_name": "Find whether it is possible to finish all tasks or not from given dependencies"},
        {"topic": "Graphs", "question_name": "Find the number of islands"},
        {"topic": "Graphs", "question_name": "Prim's Algo"},
        {"topic": "Graphs", "question_name": "Negative Weighted Cycle"},
        {"topic": "Graphs", "question_name": "Floyd Warshall"},
        {"topic": "Graphs", "question_name": "Graph Coloring"},
        {"topic": "Graphs", "question_name": "Snakes and Ladders"},
        {"topic": "Graphs", "question_name": "Kosaraju's Theorem"},
        {"topic": "Graphs", "question_name": "Journey to moon"},
        {"topic": "Graphs", "question_name": "Vertex Cover"},
        {"topic": "Graphs", "question_name": "M Coloring Problem"},
        {"topic": "Graphs", "question_name": "Cheapest Flights Within K Stops"},
        {"topic": "Graphs", "question_name": "Find if there is a path of more than k length from a source"},
        {"topic": "Graphs", "question_name": "Bellman Ford"},
        {"topic": "Graphs", "question_name": "Bipartitie Graph"},
        {"topic": "Graphs", "question_name": "Word-Ladder"},
        {"topic": "Graphs", "question_name": "Allen Dictionary"},
        {"topic": "Graphs", "question_name": "Kruskals MST"},
        {"topic": "Graphs", "question_name": "Total number spanning trees graph"},
        {"topic": "Graphs", "question_name": "Travelling Salesman"},
        {"topic": "Graphs", "question_name": "Find longest path directed acyclic graph"},
        {"topic": "Graphs", "question_name": "Two Clique Problem"},
        {"topic": "Graphs", "question_name": "Minimise the cash flow"},
        {"topic": "Graphs", "question_name": "Chinese postman"},
        {"topic": "Graphs", "question_name": "Water Jug"},
        {"topic": "Graphs", "question_name": "Water Jug 2"},
        {"topic": "Tries", "question_name": "Construct a trie from scratch"},
        {"topic": "Tries", "question_name": "Print unique rows in a given boolean matrix"},
        {"topic": "Tries", "question_name": "Word Break Problem | (Trie solution)"},
        {"topic": "Tries", "question_name": "Given a sequence of words, print all anagrams together"},
        {"topic": "Tries", "question_name": "Find shortest unique prefix for every word in a given list"},
        {"topic": "Tries", "question_name": "Implement a Phone Directory"},
        {"topic": "DP", "question_name": "Knapsack with Duplicate Items"},
        {"topic": "DP", "question_name": "BBT counter"},
        {"topic": "DP", "question_name": "Reach a given score"},
        {"topic": "DP", "question_name": "Maximum difference of zeros and ones in binary string"},
        {"topic": "DP", "question_name": "Climbing Stairs"},
        {"topic": "DP", "question_name": "Permutation Coefficient"},
        {"topic": "DP", "question_name": "Longest Repeating Subsequence"},
        {"topic": "DP", "question_name": "Pairs with specific difference"},
        {"topic": "DP", "question_name": "Longest subsequence-1"},
        {"topic": "DP", "question_name": "Coin Change"},
        {"topic": "DP", "question_name": "LIS"},
        {"topic": "DP", "question_name": "Longest Common Subsequence"},
        {"topic": "DP", "question_name": "Word Break"},
        {"topic": "DP", "question_name": "Combination Sum IV"},
        {"topic": "DP", "question_name": "House Robber"},
        {"topic": "DP", "question_name": "Houe Robber 2"},
        {"topic": "DP", "question_name": "Decode Ways"},
        {"topic": "DP", "question_name": "Unique Paths"},
        {"topic": "DP", "question_name": "Jumps Game"},
        {"topic": "DP", "question_name": "Knapsack Problem"},
        {"topic": "DP", "question_name": "nCr"},
        {"topic": "DP", "question_name": "Catalan Number"},
        {"topic": "DP", "question_name": "Edit Distance"},
        {"topic": "DP", "question_name": "Subset Sum"},
        {"topic": "DP", "question_name": "Gold mine"},
        {"topic": "DP", "question_name": "Assembly Line Scheduling"},
        {"topic": "DP", "question_name": "Maximize The Cut Segments"},
        {"topic": "DP", "question_name": "Maximum sum increasing subsequence"},
        {"topic": "DP", "question_name": "Count all subsequences having product less than K"}
    ]
    create_numbered_dsa_folder_structure_with_data(data)