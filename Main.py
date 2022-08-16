class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.maxSize = k
        self.head = 0
        self.tail = -1
    def enQueue(self, val: int) -> bool:
        if self.isFull(): return False
        self.tail = (self.tail + 1) % self.maxSize
        self.data[self.tail] = val
        return True
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.head == self.tail: self.head, self.tail = 0, -1
        else: self.head = (self.head + 1) % self.maxSize
        return True
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.tail]
    def isEmpty(self) -> bool:
        return self.tail == -1
    def isFull(self) -> bool:
        return not self.isEmpty() and (self.tail + 1) % self.maxSize == self.head

# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
