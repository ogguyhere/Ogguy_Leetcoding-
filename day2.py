 # Leetcode no 706 : Design HashMap
 
 class MyHashMap:
        
    def __init__(self):
        self.size = 1000000
        self.map = [-1] * self.size
        
  

    def put(self, key: int, value: int) -> None:
        self.map[key] = value
 
    def get(self, key: int) -> int:
        return self.map[key]
 
    def remove(self, key: int) -> None:
        self.map[key] = -1
 
    
def main():
    hashmap = MyHashMap()

    # Add key-value pairs
    hashmap.put(1, 100)
    hashmap.put(2, 200)
    hashmap.put(3, 300)

    # Retrieve values
    print("Get key 1:", hashmap.get(1))  # Should print 100
    print("Get key 2:", hashmap.get(2))  # Should print 200
    print("Get key 4 (not present):", hashmap.get(4))  # Should print -1

    # Remove a key
    hashmap.remove(2)

    # Try getting removed key
    print("Get key 2 after removal:", hashmap.get(2))  # Should print -1

    # Update a key
    hashmap.put(1, 999)
    print("Get updated key 1:", hashmap.get(1))  # Should print 999

if __name__ == "__main__":
    main()
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)