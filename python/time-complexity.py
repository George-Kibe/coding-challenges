"""
    Time complexity is a way to show how the runtime of a program increases as the input size increases.
    n is the size of the input
    Big O notation is a way to show the time complexity of a program.
    O(1) is the best time complexity. - Constant time complexity
    O(n) is the worst time complexity.- Linear time complexity
    O(log n) is the average time complexity. - Logarithmic time complexity 
    O(n^2) is the worst time complexity. - Quadratic time complexity
    O(n^3) is the worst time complexity. - Cubic time complexity
    O(2^n) is the worst time complexity. - Exponential time complexity
    O(n!) is the worst time complexity. - Factorial time complexity
"""
# Time complexity is a way to show how the runtime of a program increases as the input size increases.
# n is the size of the input
# Big O notation is a way to show the time complexity of a program.
# O(1) is the best time complexity. - Constant time complexity
# O(n) is the worst time complexity.- Linear time complexity
# O(log n) is the average time complexity. - Logarithmic time complexity
# O(n^2) is the worst time complexity. - Quadratic time complexity
# O(n^3) is the worst time complexity. - Cubic time complexity
# O(2^n) is the worst time complexity. - Exponential time complexity
# O(n!) is the worst time complexity. - Factorial time complexity

# Example of O(1) time complexity


def constant_time_complexity(n):
    return n * 2

# Example of O(n) time complexity

class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def find_sum_tree(root):
    if root is None:
        return 0
    return root.data + find_sum_tree(root.left) + find_sum_tree(root.right)

# create a node example
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node6.right = node8
# call the find sum function
total_sum = find_sum_tree(node1)
print("Total sum of all nodes:", total_sum)



# Linear search using a list
def linear_search_list(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

numbers_list = [10, 20, 30, 40, 50]
target = 30
result = linear_search_list(numbers_list, target)
print("Linear search List Found at index:" if result != -1 else "Not found", result)


# Linear Search using an Array
import array

def linear_search_array(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

numbers_array = array.array('i', [10, 20, 30, 40, 50])
target = 30
result = linear_search_array(numbers_array, target)
print("Linear search Array Found at index:" if result != -1 else "Not found", result)


## Binary search Using a list O(log n)
def binary_search_list(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

numbers_list = [10, 20, 30, 40, 50]
target = 30
result = binary_search_list(numbers_list, target)
print("Binary search List Found at index:" if result != -1 else "Not found", result)


# Binary search using an array
def binary_search_array(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

numbers_array = array.array('i', [10, 20, 30, 40, 50])
target = 30
result = binary_search_array(numbers_array, target)
print("Binary search Array Found at index:" if result != -1 else "Not found", result)
