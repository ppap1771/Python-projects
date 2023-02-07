from collections import deque

class Queue():
    def __init__(self):
        self.element = deque()
    
    def enqueue(self, element):
        self.element.append(element)

    def dequeue(self):
        self.element.popleft() 


q1 = Queue()

