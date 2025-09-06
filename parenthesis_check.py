class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        print(f"pushed valuse {val}")

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if not self.is_empty():
            self.stack.pop()

    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def display(self):
        print(f"the stack is {self.stack}")

    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        self.stack = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                self.stack.append(s[i])
            else:
                len(self.stack) == 0
                if not (len(self.stack) == 0):
                    topele = self.stack[-1]
                    if (
                        (s[i] == ")" and topele == "(")
                        or (s[i] == "]" and topele == "[")
                        or (s[i] == "}" and topele == "{")
                    ):
                        self.stack.pop()

                    else:
                        return False
                else:
                    return False
        if len(self.stack) == 0:
            return True

        else:
            return False

            # if(self.)


a = Stack()
a.push(10)
a.push(20)
a.push(30)
a.push(40)


a.display()

a.peek()
