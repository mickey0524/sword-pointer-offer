# coding: utf-8

from collections import deque

class MinStack(object):
    def __init__(self):
        self.data_stack = deque()
        self.min_stack = deque()
    
    def push(self, v):
        self.data_stack.append(v)
        if len(self.min_stack) == 0:
            self.min_stack.append(v)
        elif v <= self.min_stack[-1]:
            self.min_stack.append(v)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if len(self.data_stack) == 0:
            raise IndexError('pop from an empty stack')

        self.data_stack.pop()
        self.min_stack.pop()

    def min(self):
        if len(self.min_stack) == 0:
            raise IndexError('find min from an empty stack')

        return self.min_stack[-1]
    

if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(2)
    print min_stack.min()
    min_stack.push(3)
    print min_stack.min()
    min_stack.push(1)
    print min_stack.min()
    min_stack.pop()
    print min_stack.min()
    min_stack.pop()
    print min_stack.min()
