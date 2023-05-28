from dataclasses import dataclass
from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    #Used to compare the elements together to be able to list them in priority
    def __gt__(self, other):
        return min(self.capacity, self.volume)*self.nutrient_factor > min(other.capacity, other.volume)*other.nutrient_factor
    
    def __le__(self, other):
        return min(self.capacity, self.volume)*self.nutrient_factor <= min(other.capacity, other.volume)*other.nutrient_factor

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        #Creates a heap to store the beehives, use the heap for a priority queue
        self.selector_size = max_beehives
        self.heap = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        """
            Takes a list as an input and replaces all of the beehives in the current
            selector with the ones from the input list.

            hive_list - Input list to replace the current beehives.

            :Complexity:
                Worst-Case: O(M)*O(log(M)) where M is the number of new beehives to add.
        """
        new_heap = MaxHeap(self.selector_size) #O(1)

        for i in hive_list: #O(M)
            new_heap.add(i) #O(log(M))

        self.heap = new_heap
        
    #Adds the beehive using the heap function
    def add_beehive(self, hive: Beehive):
        """
            Adds a beehive to the pririoty queue based on the maximum emerald gain per gather.
            hive - The hive to add to the queue.

            :Complexity:
                Worst-Case: The tree is always balanced in a heap so the worst case complexity is
                            O(log(N))*O(comp) where N is the number of nodes in the. Meaning we have to 
                            only traverse along the depth.
                Best-Case: The best case is equal to the worst case.
        """

        self.heap.add(hive) #O(log(N))*O(comp)
    
    def harvest_best_beehive(self):
        """
            Extracts the BeeHive which will give the highest gain of emeralds per day.

            return - Returns the node with the largest emerald gain.

            :Complexity:
                Worst-Case: O(log(N)) where N is the number of nodes in the tree.
                Best-Case: Is te same as the worst case.
        """

        beehive = self.heap.get_max() #O(log(N))
        harvested = min(beehive.capacity, beehive.volume) #O(1)

        beehive.volume -= harvested #O(1)
        
        self.add_beehive(beehive) #O(log(N))
        return harvested*beehive.nutrient_factor
