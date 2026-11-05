
class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(char) for char in string)

    def add(self, key, value):
        key_hash = self.hash(key)

        if key_hash in self.collection:
            self.collection[key_hash][key] = value
        else:
            self.collection[key_hash] = {key: value}

    def remove(self, key):
        key_hash = self.hash(key)

        if key_hash in self.collection:
            if key in self.collection[key_hash]:
                del self.collection[key_hash][key]

    def lookup(self, key):
        key_hash = self.hash(key)

        if key_hash in self.collection:
            return self.collection[key_hash].get(key)

        return None
