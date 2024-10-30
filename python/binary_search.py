from typing import Optional, List

def binary_search(items: List[int], item: int) -> Optional[int]:
    minimal_index, maximal_index = 0, (len(items) - 1)
    
    while minimal_index <= maximal_index:
        middle_index = (minimal_index + maximal_index) // 2
        value = items[middle_index]
       
        if value == item:
            return middle_index
        elif value > item:
            maximal_index = middle_index - 1
        else:
            minimal_index = middle_index + 1

    return None