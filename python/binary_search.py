from typing import Optional

def binary_search(numbers, search_number) -> Optional[int]:
    min_idx, max_index = 0, len(numbers) - 1

    while min_idx <= max_index:
        mid_idx = (min_idx + max_index) // 2
        found = numbers[mid_idx]

        if found > search_number:
            max_index = mid_idx - 1
        elif found < search_number:
            min_idx = mid_idx + 1
        else:
            return mid_idx
    
    return None