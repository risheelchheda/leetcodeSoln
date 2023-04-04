def __init__(self, capacity: int):
        self.capacity = capacity
        
        # initialize an empty ordered dictionary to store the key-value pairs of the cache
        self.dict = collections.OrderedDict()
        
        # initialize the size of the cache to 0
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.dict:
            
            # move the key-value pair to the end of the ordered dictionary to indicate that it was recently used
            self.dict.move_to_end(key)
            
            # return the value of the key
            return self.dict[key]
        
        # if the key is not present in the cache
        else:
            
            # return -1 to indicate that the key is not present in the cache
            return -1

    def put(self, key: int, value: int) -> None:
        # if the key is already present in the cache
        if key in self.dict:
            
            # update the value of the key
            self.dict[key] = value
            
            # move the key-value pair to the end of the ordered dictionary to indicate that it was recently used
            self.dict.move_to_end(key)
        
        # if the key is not present in the cache
        else:
            
            # if the cache has not reached its capacity yet
            if self.size < self.capacity:
                
                # add the key-value pair to the cache
                self.dict[key] = value
                
                # increase the size of the cache by 1
                self.size += 1
            
            # if the cache has reached its capacity
            else:
                
                # remove the least recently used key-value pair from the cache
                self.dict.popitem(False)
                
                # add the new key-value pair to the cache
                self.dict[key] = value
