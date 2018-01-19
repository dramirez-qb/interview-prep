class HashMap:
    """
    Hash table implementation
    """

    def __init__(self):
        self.hashmap = [[] for _ in range(256)]

    def insert(self, key, value):
        """
        inserts key, value tuple into hashmap
        O(1)
        """

        hash_key = hash(key) % len(self.hashmap)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def retrieve(self, key):
        """
        retrieves value from key in hashmap
        O(1)
        """

        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            return v
        raise KeyError
