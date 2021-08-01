class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyspace = 3000
        self.buckets = [[] for _ in range(self.keyspace)]


    def add(self, key: int) -> None:
        hash_key = key % self.keyspace
        b = self.buckets[hash_key]
        if key in b:
            return
        b.append(key)
        #found = False
        #for element in b:       #if key in b: return
            #if key == element:
                #found = True
                #break
                #return
        #b.append(key)


    def remove(self, key: int) -> None:
        hash_key = key % self.keyspace
        b = self.buckets[hash_key]
        #found = False
        #i = -1
        for index, element in enumerate(b):
            if key == element:
                b[index] = -1
                return
                #found = True
                #i = index
                #break
        #if found == True:
            #b[i] = -1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_key = key % self.keyspace
        b = self.buckets[hash_key]
        if key in b:
            return True
        return False
