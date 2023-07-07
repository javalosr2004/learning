import random

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def hash(self, s: str) -> int:
        sum = 0
        for char in s:
            sum += ord(char)

        return sum % self.capacity

    def rehash(self, s: str, hash: int) -> int:
        rehash = hash
        count = 1
        while self.table[rehash] and self.table[rehash][0] != s:
            rehash = (hash + pow(count, 2)) % self.capacity
            count += 1
            if count > self.capacity:
                raise Exception('Hash table is full.')
        return rehash

    def resize(self):
        old_capacity = self.capacity
        self.capacity *= 2
        new_table = [None] * self.capacity
        for i in range(old_capacity):
            if self.table[i] is not None:
                hash = self.hash(self.table[i][0])
                new_table[hash] = self.table[i]
        self.table = new_table

    def add(self, key: str, val: str):
        if self.size + 1 > self.capacity / 2:
            self.resize()

        hash = self.hash(key)
        if self.table[hash] is None or self.table[hash][0] == key:
            self.table[hash] = (key, val)
        else:
            hash = self.rehash(key, hash)
            self.table[hash] = (key, val)

        self.size += 1

    def get(self, key: str):
        hash = self.hash(key)
        if self.table[hash] and self.table[hash][0] == key:
            return self.table[hash][1]
        else:
            hash = self.rehash(key, hash)
            if self.table[hash] and self.table[hash][0] == key:
                return self.table[hash][1]
            else:
                raise Exception('Key not found in hash table.')
    

h1 = HashTable(10)

for name, val in zip(['apple', 'tom', 'cruise', 'zape', 'cop', 'crab', 'bananna', 'jesus', 'zane', 'josh', 'jeeesus', 'dajwbdjwbajdbwajdbjwabd'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
    h1.add(name, val)

for i in ['apple', 'tom', 'cruise', 'zape', 'cop', 'crab', 'bananna', 'jesus', 'zane', 'josh', 'jeeesus', 'dajwbdjwbajdbwajdbjwabd']:
    print(h1.get(i))

print()
    



# key -> hash -> check -> rehash?? -> resize?? 

