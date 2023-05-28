from __future__ import annotations
from threedeebeetree import Point

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    raise NotImplementedError()
    """
    Reorder the import list.   
    Args: 
    - my_coordinate_list: a list with Point that would be inserted into 3dbt. 
    Raises: /
    Returns: 
    - return a list after sorting to allowed insert the point into 3dbt. 
    Complexity: 
    - The complexity is always O(nlogn ^ logn). 
    """
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    def is_coprime(a: int, b: int) -> bool:
        return gcd(a, b) == 1

    def reorder_points(points: list[Point], start: int, end: int, step: int) -> list[Point]:
        if start >= end:
            return []

        mid = (start + end) // 2
        reordered_list = []
        for j in range(start, end + 1, step):
            if is_coprime(step, j - start):
                reordered_list.append(points[j])

        left_points = reorder_points(points, start, mid, step * 2)
        right_points = reorder_points(points, mid + 1, end, step * 2)
        
        reordered_list.extend(left_points)
        reordered_list.extend(right_points)
        return reordered_list

    sorted_points = sorted(my_coordinate_list, key=lambda point: point[0])
    n = len(sorted_points)
    reordered_list = reorder_points(sorted_points, 0, n - 1, 1)
    return reordered_list