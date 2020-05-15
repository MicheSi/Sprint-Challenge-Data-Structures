class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.size = 0

    def append(self, item):

        if len(self.data) == self.capacity:
            self.data[self.size] = item
        else:
            self.data.append(item)
        self.size = (self.size + 1) % self.capacity
        
    def get(self):
        return self.data
