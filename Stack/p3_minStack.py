# 1. Brute Force


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        while len(tmp):
            self.stack.append(tmp.pop())

        return mini


obj = MinStack()

obj.push(1)
obj.push(2)
obj.push(0)

print(obj.getMin())  # 0

obj.pop()

print(obj.top())  # 2
print(obj.getMin())  # 1



#2 stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack:
            minimum = min(val, self.minStack[-1])
        else:
            minimum = val

        self.minStack.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# ---------------- Driver Code ----------------

obj = MinStack()

obj.push(5)
print("Stack      :", obj.stack)
print("Min Stack  :", obj.minStack)
print()

obj.push(8)
print("Stack      :", obj.stack)
print("Min Stack  :", obj.minStack)
print()

obj.push(2)
print("Stack      :", obj.stack)
print("Min Stack  :", obj.minStack)
print()

obj.push(7)
print("Stack      :", obj.stack)
print("Min Stack  :", obj.minStack)
print()

obj.push(1)
print("Stack      :", obj.stack)
print("Min Stack  :", obj.minStack)
print()

print("Top     :", obj.top())
print("Minimum :", obj.getMin())
print()

obj.pop()

print("After Pop")
print("Stack      :", obj.stack)
print("Min Stack  :", obj.minStack)
print("Top        :", obj.top())
print("Minimum    :", obj.getMin())