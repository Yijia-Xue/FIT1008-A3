from __future__ import annotations
from typing import Generic, TypeVar, Tuple, List
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    #Sets the default connection list to 8 None variables in a list
    connections: List[BeeNode|None] = field(default_factory= lambda: [None]*8)
    subtree_size: int = 1

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        #Uses the bit position to determine where the item should go into the list
        position = 0
        for i in range(3):
            if point[i] >= self.key[i]:
                position |= (1 << i) 

        #Returns the child based on the position
        return self.connections[position]


class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        """
            Finds a node object based on the key input of the user.

            key - Key you want to search for.
            return - Returns None if the key cannot be found in the tree.
                     Else, if the key is found it will return the BeeNode object
                     at that position in the tree.

            :Complexity:
                Worst-Case: O(N)*O(Comp) N being the number of nodes in the tree.
                            This occurs when the tree is unbalanced and we are 
                            searching for a leafnode of the tree.
                Best-Case: O(1) this is when we have the root as the key we are 
                           looking for.
        """
        return self.__get_tree_node_by_key_aux(key, self.root)

    def __get_tree_node_by_key_aux(self, key: I, current: BeeNode):
        """
            Auxillary function used to find a node based on the key input.

            :Complexity: See get_tree_node for overall use case complexity.
        """
        if current is not None:
            if current.key == key:
                return current
            else:
                #Uses the bit position to determine where the item should go into the list
                position = 0
                for i in range(3):
                    if key[i] >= current.key[i]:
                        position |= (1 << i) 

                return self.__get_tree_node_by_key_aux(key, current.connections[position])

        return None

    def __setitem__(self, key: Point, item: I) -> None:
        #If the length is 0 then we know the only thing to add is the root
        #Put this above the position because position does not need to be calculated
        if self.length == 0:
            self.root = BeeNode(key, item)
            self.length += 1
        else:
            self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it

            current - The current node we are checkign the children of.
            key - The key which we are inserting the item into.
            item - The item we want to store at the node.

            :Complexity: 
                Worst-Case: Is O(N) where N is the number of nodes in the tree.
                            This will happen when the tree is unbalanced and the 
                            Node we are inserting goes to the bottom of the tree.
                Best-Case: Is O(log(N)) where N is the number of nodes in the tree.
                           This means we only have to traverse across teh depth of
                           the tree to find the correct posion. Happens when the 
                           tree is balanced.
        """
        #Calculates the position which needs to be appended or recursed
        position = 0
        for i in range(3):
            if key[i] >= current.key[i]:
                position |= (1 << i) 

        #Traverse to the next node in the position if it is not none
        if current.connections[position] is not None:
            new_node = self.insert_aux(current.connections[position], key, item)
            current.subtree_size = 1
    
        #Reaches the base case that the current node is none, then we can insert
        else:
            new_node = BeeNode(key, item)
            current.connections[position] = new_node
            self.length += 1

        #Adds the size of the lower subtrees to the current node
        for i in range(8):
            if current.connections[i] is not None:
                current.subtree_size += current.connections[i].subtree_size

        return new_node


    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        
        if len(current.connections) == [None]*8:
            return True
        else:
            return False

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
