from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """Return indices of the two numbers that add up to target.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("No two sum solution")


if __name__ == "__main__":
    examples = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]
    for nums, target in examples:
        print(f"nums={nums}, target={target} -> {twoSum(nums, target)}")