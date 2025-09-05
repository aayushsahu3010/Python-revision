class stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(f"Pushed value {value}")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"

    def peel(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is Empty!"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    # Display the stack
    def display(self):
        print("Stack (bottom → top):", self.stack)
