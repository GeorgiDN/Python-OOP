class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        last_element = self.data.pop()
        return last_element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("Tomato")
print(stack)
print(stack.top())
print(stack.pop())
print(stack)
print(stack.is_empty())
stack.pop()
stack.pop()
print(stack.is_empty())
