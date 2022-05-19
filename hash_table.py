from collections import deque
from typing import NamedTuple, Any

INITIAL_CAPACITY = 4

class Bucket(NamedTuple):
    key: Any
    value: Any
    
class HashTable:
    """
    Partial HashTable implementation
    """
    def __init__(self, capacity=INITIAL_CAPACITY):
        if capacity < 1:
            raise ValueError("We need to allocate at least one placeholder for future values.")
        self._buckets = [deque() for _ in range(capacity)]
        self._keys = []

    def __len__(self):
        return len(self._buckets)
    
    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
        
    def __getitem__(self, key):
            bucket = self._buckets[self._get_index(key)]
            for pair in bucket:
                if pair.key == key:
                    return pair.value
            raise KeyError(key)
    
    def __setitem__(self, key, value):
            bucket = self._buckets[self._get_index(key)]
            for index, pair in enumerate(bucket):
                if pair.key == key:
                    bucket[index] = Bucket(key, value)
                    break
            else:
                self._resize_and_rehash()
                bucket.append(Bucket(key, value))
                self._keys.append(key)
    
    def __delitem__(self, key):
        bucket = self._buckets[self._get_index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                del bucket[index]
                self._keys.remove(key)
                break
        else:
            raise KeyError(key)

    
    def __iter__(self):
        yield from self.keys
    
    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return self._buckets == other._buckets
    
    def _get_index(self, key):
        return hash(key) % self.capacity
            
    def _resize_and_rehash(self):
        copy = HashTable(capacity=self.capacity * 2)
        if len(self.items) >= 1:
            for key, value in self.items:
                copy[key] = value
        self = copy
    
    @property
    def keys(self):
        return self._keys.copy()

    @property
    def values(self):
        return [self[key] for key in self.keys]

    @property
    def items(self):
        return [(key, self[key]) for key in self.keys]
    
    @property
    def capacity(self):
        return len(self._buckets)

    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
