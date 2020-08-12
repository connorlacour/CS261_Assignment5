# Course: CS261 - Data Structures
# Assignment: 5
# Student: Connor LaCour
# Description: This program utilizes the imported DynamicArray class to implement a MinHeap. The
# MinHeap class creates a heap object with the following methods: add, get_min, remove_min, and
# build_heap.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import DynamicArray
from a5_include import LinkedList


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        add adds the given node into the heap
        """

        # add to next available node
        self.heap.append(node)

        new_node_index = self.heap.length() - 1
        new_node_value = self.heap.get_at_index(new_node_index)
        parent_index = ((new_node_index - 1) // 2)
        parent_value = self.heap.get_at_index(parent_index)

        while new_node_index != 0 and new_node_value < parent_value:

            self.heap.swap(new_node_index, parent_index)
            new_node_index = parent_index
            parent_index = ((new_node_index - 1) // 2)
            parent_value = self.heap.get_at_index(parent_index)

        return

    def get_min(self) -> object:
        """
        get_min returns the minimum value in the heap
        """
        if self.heap.length() == 0:
            raise MinHeapException

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        remove_min removes the minimum value in the heap
        """
        if self.heap.length() == 0:
            raise MinHeapException

        min_val = self.get_min()

        if self.heap.length() == 1:
            self.heap.pop()

        else:

            last_in_heap = self.heap.get_at_index(self.heap.length() - 1)
            self.heap.set_at_index(0, last_in_heap)
            self.heap.pop()

            replacement_index = 0
            replacement_value = last_in_heap

            left_child_index = (replacement_index * 2) + 1
            right_child_index = (replacement_index * 2) + 2

            if left_child_index < self.heap.length():
                left_child_value = self.heap.get_at_index(left_child_index)
            else:
                left_child_value = None

            if right_child_index < self.heap.length():
                right_child_value = self.heap.get_at_index(right_child_index)
            else:
                right_child_value = None

            while left_child_value is not None or right_child_value is not None:

                if left_child_value is None:
                    if replacement_value > right_child_value:
                        self.heap.swap(replacement_index, right_child_index)
                        break
                    else:
                        break

                if right_child_value is None:
                    if replacement_value > left_child_value:
                        self.heap.swap(replacement_index, left_child_index)
                        break
                    else:
                        break

                if left_child_value < right_child_value:
                    if replacement_value > left_child_value:
                        self.heap.swap(replacement_index, left_child_index)

                        replacement_index = left_child_index
                        left_child_index = (replacement_index * 2) + 1
                        right_child_index = (replacement_index * 2) + 2

                        if left_child_index < self.heap.length():
                            left_child_value = self.heap.get_at_index(left_child_index)
                        else:
                            left_child_value = None
                        if right_child_index < self.heap.length():
                            right_child_value = self.heap.get_at_index(right_child_index)
                        else:
                            right_child_value = None

                    else:
                        break

                else:
                    if replacement_value > right_child_value:
                        self.heap.swap(replacement_index, right_child_index)

                        replacement_index = right_child_index
                        left_child_index = (replacement_index * 2) + 1
                        right_child_index = (replacement_index * 2) + 2
                        if left_child_index < self.heap.length():
                            left_child_value = self.heap.get_at_index(left_child_index)
                        else:
                            left_child_value = None
                        if right_child_index < self.heap.length():
                            right_child_value = self.heap.get_at_index(right_child_index)
                        else:
                            right_child_value = None
                    else:
                        break

        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        build_heap creates a heap out of a given DynamicArray object
        """
        new_arr = DynamicArray()
        for i in range(da.length()):
            new_arr.append(da.get_at_index(i))

        self.heap = new_arr
        if self.heap.length() == 0:
            raise MinHeapException

        k = (da.length() - 2) // 2

        while k != -1:

            cur_index = k
            cur_value = da.get_at_index(k)
            left_child_index = (cur_index * 2) + 1
            right_child_index = (cur_index * 2) + 2

            if left_child_index < self.heap.length():
                left_child_value = self.heap.get_at_index(left_child_index)
            else:
                left_child_value = None
            if right_child_index < self.heap.length():
                right_child_value = self.heap.get_at_index(right_child_index)
            else:
                right_child_value = None

            while left_child_value is not None or right_child_value is not None:

                if left_child_value is None:
                    if cur_value > right_child_value:
                        self.heap.swap(cur_index, right_child_index)
                        break
                    else:
                        break

                if right_child_value is None:
                    if cur_value > left_child_value:
                        self.heap.swap(cur_index, left_child_index)
                        break
                    else:
                        break

                if left_child_value < right_child_value:
                    if cur_value > left_child_value:
                        self.heap.swap(cur_index, left_child_index)

                        cur_index = left_child_index
                        left_child_index = (cur_index * 2) + 1
                        right_child_index = (cur_index * 2) + 2

                        if left_child_index < self.heap.length():
                            left_child_value = self.heap.get_at_index(left_child_index)
                        else:
                            left_child_value = None
                        if right_child_index < self.heap.length():
                            right_child_value = self.heap.get_at_index(right_child_index)
                        else:
                            right_child_value = None

                    else:
                        break

                else:
                    if cur_value > right_child_value:
                        self.heap.swap(cur_index, right_child_index)

                        cur_index = right_child_index
                        left_child_index = (cur_index * 2) + 1
                        right_child_index = (cur_index * 2) + 2
                        if left_child_index < self.heap.length():
                            left_child_value = self.heap.get_at_index(left_child_index)
                        else:
                            left_child_value = None
                        if right_child_index < self.heap.length():
                            right_child_value = self.heap.get_at_index(right_child_index)
                        else:
                            right_child_value = None
                    else:
                        break
            k -= 1


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
