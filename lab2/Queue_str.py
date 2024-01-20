class Queue:
    capacity = 10

    def __init__(self):
        self.data = [None] * Queue.capacity #list instance with fixed capacity
        self.size = 0                       #current number of elements
        self.front = 0                      #index within data of the first element

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def clear(self):
        self.data = [] * Queue.capacity
    
    def enqueue(self, e):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return answer

    def resize(self, cap):
        old = self.data
        self.data = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self.data[self.front]
    
    def traverse(self):
        value = []
        for i in range(len(self.data)):
            value.append(self.data[i])
        return value
    
    def convertor(self, decimal):
        decimal = int(decimal)
        if decimal == 0:
            return '0'
        
        binary = Queue()

        while decimal > 0:
            remainder = decimal % 2
            binary.enqueue(remainder)
            decimal //= 2

        result = ''
        while not binary.is_empty():
            result += str(binary.dequeue())

        return result
    
if __name__ == '__main__':
    queue = Queue()

    queue.enqueue("one")
    queue.enqueue("two")
    queue.enqueue("three")
    queue.enqueue("four")

    queue.dequeue()

    print(queue.first())
    print(queue.traverse())

    print(queue.convertor("10"))





