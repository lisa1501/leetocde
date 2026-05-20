from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    """Return True if there are duplicate values in the list, False otherwise.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    return len(set(nums)) != len(nums);
    
    
if __name__ == "__main__":
    examples = [
        ([1, 2, 3, 3], True),
        ([1, 2, 3, 4], False),
    ]
    for nums, expec in examples:
        print(f"nums={nums}, hasDuplicate={hasDuplicate(nums)}")