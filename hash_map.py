# Course: CS261 - Data Structures
# Assignment: 5
# Student: Connor LaCour
# Description: This program utilizes DynamicArray and LinkedList classes to implement a HashMap. The class
# HashMap contains the following methods: empty_buckets, table_load, clear, put, contains_key, get, remove,
# resize_table, get_keys.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import DynamicArray
from a5_include import LinkedList


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        TODO: Write this implementation
        """

        if self.size == 0:
            return

        for i in range(self.capacity):
            bucket = self.buckets.get_at_index(i)

            for node in bucket:
                bucket.remove(node.key)
                self.size -= 1

    def get(self, key: str) -> object:
        """
        TODO: Write this implementation
        """

        if self.size == 0:
            return None

        for i in range(self.capacity):
            bucket = self.buckets.get_at_index(i)

            for node in bucket:
                if node.key == key:
                    return node.value

        return None

    def put(self, key: str, value: object) -> None:
        """
        TODO: Write this implementation
        """

        generate_hash = self.hash_function(key)
        index = generate_hash % self.capacity

        bucket = self.buckets.get_at_index(index)

        if bucket.contains(key) is not None:
            bucket.remove(key)
            bucket.insert(key, value)

        else:
            bucket.insert(key, value)
            self.size += 1

    def remove(self, key: str) -> None:
        """
        TODO: Write this implementation
        """

        if self.size == 0:
            return

        for i in range(self.capacity):
            bucket = self.buckets.get_at_index(i)

            for node in bucket:
                if node.key == key:
                    bucket.remove(key)
                    self.size -= 1

        return

    def contains_key(self, key: str) -> bool:
        """
        TODO: Write this implementation
        """
        if self.size == 0:
            return False

        for i in range(self.capacity):
            bucket = self.buckets.get_at_index(i)

            for node in bucket:
                if node.key == key:
                    return True

        return False

    def empty_buckets(self) -> int:
        """
        TODO: Write this implementation
        """

        tally = 0

        for i in range(self.buckets.length()):
            if self.buckets.get_at_index(i).length() == 0:
                tally += 1

        return tally

    def table_load(self) -> float:
        """
        TODO: Write this implementation
        """
        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        TODO: Write this implementation
        """

        if new_capacity < 1:
            pass

        new_hash_map = HashMap(new_capacity, self.hash_function)

        for i in range(self.capacity):
            bucket = self.buckets.get_at_index(i)
            for node in bucket:
                new_hash_map.put(node.key, node.value)

        self.clear()
        cap_difference = new_capacity - self.capacity
        for i in range(cap_difference):
            self.buckets.append(LinkedList())
            self.capacity += 1

        for i in range(new_hash_map.capacity):
            bucket = new_hash_map.buckets.get_at_index(i)
            for node in bucket:
                self.put(node.key, node.value)

    def get_keys(self) -> DynamicArray:
        """
        TODO: Write this implementation
        """

        keys_arr = DynamicArray()

        for i in range(self.capacity-1, -1, -1):
            bucket = self.buckets.get_at_index(i)
            j = 0
            for node in bucket:
                """
                print(node)
                print(node.next)
                """
                if j % 2 == 0:
                    if node.next is not None:
                        keys_arr.append(node.next.key)
                    if node is not None:
                        keys_arr.append(node.key)
                j += 1
        """
        # reverse for gradescope
        half_length = int(keys_arr.length() / 2)
        full_length = int(keys_arr.length())

        for n in range(half_length):
            mirror = (full_length - 1) - n
            keys_arr.swap(n, mirror)
        """

        return keys_arr


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')
    
    
    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))

    
    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    
    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)
    
        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')
    
        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))

    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())

