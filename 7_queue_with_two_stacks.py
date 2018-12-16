# coding: utf-8

from collections import deque

class Stack(object):
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) == 0:
            raise IndexError('pop from an empty stack')
        return self.stack.pop()
    
    def __len__(self):
        return len(self.stack)

class QueueWithTwoStack(object):
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def push(self, item):
        self.stack_1.push(item)

    def pop(self):
        if len(self.stack_2) == 0:
            while len(self.stack_1) != 0:
                self.stack_2.push(self.stack_1.pop())

        return self.stack_2.pop()

    def __len__(self):
        return len(self.stack_1) + len(self.stack_2)


if __name__ == "__main__":
    queue = QueueWithTwoStack()

    for i in [1, 2, 3, 4, 5]:
        queue.push(i)
    
    while len(queue) != 0:
        print queue.pop()
    
