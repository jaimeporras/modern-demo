from typing import List

def process_numbers(nums: List[int]) -> List[int]:
    """Double positive numbers and drop non-positive ones."""
    return [n * 2 for n in nums if n > 0]
