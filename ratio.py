from __future__ import annotations
from typing import Generic, TypeVar, List
import math
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        """
        Initialize the class, create a list to store the item.  
        Args: /
        Raises: /
        Returns: /
        Complexity: 
        - The complexity is always O(1). 
            Because the operation is constant. 
        """
        self.store: List[T] = []
    
    def add_point(self, item: T):
        """
        Add a item to the list to store. 
        Args: 
        - item: would be added into the list, Type[T]
        Raises: /
        Returns: /
        Complexity: 
        - The complexity is always O(logN), while n is the number of elements in the list, while the code did a binary search to insert item. 
        """
        low, high = 0, len(self.store)
        while low < high:
            mid = (low + high) // 2
            if self.store[mid] <= item:
                low = mid + 1
            else:
                high = mid
        self.store.insert(low, item)
    
    def remove_point(self, item: T):
        """
        Remove a item to the list to store. 
        Args: 
        - item: would be removed from the list, Type[T]
        Raises: /
        Returns: /
        Complexity: 
        - The complexity is always O(logN), which n is the number of elements in the list, while the code perform a binary search to find the item. 
        """
        low, high = 0, len(self.store)
        while low < high:
            mid = (low + high) // 2
            if self.store[mid] < item:
                low = mid + 1
            else:
                high = mid
        if low < len(self.store) and self.store[low] == item:
            self.store.pop(low)

    def ratio(self, x, y):
        """
        return a list that contain element which are biggers than x% of elements in the list but lower than y%. 
        Args: 
        - item: would be added into the list, Type[T]
        Raises: /
        Returns: /
        Complexity: 
        - The complexity is always O(logN), while n is the number of elements in the list, while the code did a binary search to insert item. 
        """
        if x == 0: 
            start_index = 0
            end_index = math.ceil(len(self.store) * (1 - y) / 100 - 1)
            return self.store[start_index:end_index]
        if y == 0: 
            start_index = math.ceil(len(self.store) * x / 100)
            end_index = -1
            return self.store[start_index:end_index]
        start_index = math.ceil(len(self.store) * x / 100)
        end_index = math.ceil(len(self.store) * (1 - y) / 100 - 1)
        return self.store[start_index:end_index]

if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
