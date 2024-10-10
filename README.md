# ListMaster

### Apa fungsi library ini ?

ListMaster adalah library yang memungkinkan anda untuk menyortir, memodifikasi, menggabungkan dan masih banyak lagi


# list_search

This repository contains Python implementations of various search algorithms, including linear search and binary search, along with a utility function to check if a list is sorted in ascending order.

## Functions

### 1. `is_sorted(arr)`

Checks if a list is sorted in ascending order.

- **Parameters:**
  - `arr`: A list of elements to check.
  
- **Returns:**
  - `True` if the list is sorted, `False` otherwise.

### 2. `linear_search(arr, target)`

Performs a linear search to find all occurrences of a target element in a list.

- **Parameters:**
  - `arr`: A list of elements to search.
  - `target`: The element to search for.
  
- **Returns:**
  - A list of indices where the target is found, or an empty list if not found.

- **Raises:**
  - `ValueError`: If the first argument is not a list.

### 3. `binary_search(arr, target)`

Performs a binary search to find all occurrences of a target element in a sorted list.

- **Parameters:**
  - `arr`: A sorted list of elements to search.
  - `target`: The element to search for.
  
- **Returns:**
  - A list of indices where the target is found, or an empty list if not found.

- **Raises:**
  - `ValueError`: If the first argument is not a list or if the list is not sorted in ascending order.

## Usage

To use these functions, simply import them into your Python script and call them with the appropriate parameters. Ensure that the list is sorted before using the `binary_search` function.

## Example

```python
arr = [1, 2, 2, 3, 4, 5]
target = 2

# Check if the list is sorted
print(is_sorted(arr))  # Output: True

# Perform linear search
print(linear_search(arr, target))  # Output: [1, 2]

# Perform binary search
print(binary_search(arr, target))  # Output: [1, 2]
```

