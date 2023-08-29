from collections import deque


class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        element = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return element

    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        element = self.queue1.popleft()
        self.queue2.append(element)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return element

    def empty(self) -> bool:
        return len(self.queue1) == 0

    def __str__(self):
        return "None"


# Your MyStack object will be instantiated and called as such:
myStack = MyStack()
print(myStack)
print(myStack.push(1))
print(myStack.push(2))
print(myStack.top())  # return 2
print(myStack.pop())  # return 2
print(myStack.empty())  # return False
