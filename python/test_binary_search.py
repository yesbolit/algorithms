from unittest import TestCase
from binary_search import binary_search2

def test_binary_search():
              #0 #1 #2 #3 #4 #5
    numbers = [1, 2, 4, 5, 7, 12]
    assert binary_search2(numbers, 4) == 2
    assert binary_search2(numbers, 12) == 5
    assert binary_search2(numbers, 15) == None
