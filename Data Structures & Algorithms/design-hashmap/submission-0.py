class MyHashMap:

    def __init__(self):
        self.items=[[],[]]
        

    def put(self, key: int, value: int) -> None:
        if key in self.items[0]:
            self.items[1][self.items[0].index(key)]=value
        else:
            self.items[0].append(key)
            self.items[1].append(value)


    def get(self, key: int) -> int:
        if key in self.items[0]:
            return self.items[1][self.items[0].index(key)]
        else:
            return -1
    def remove(self, key: int) -> None:
        if key in self.items[0]:
            self.items[1].pop(self.items[0].index(key))
            self.items[0].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)