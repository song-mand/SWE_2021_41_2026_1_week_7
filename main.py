from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}  # 값: 인덱스

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []
