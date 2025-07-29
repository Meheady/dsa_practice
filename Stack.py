class Stack:
    def __init__(self):
        self.items = [];

    def push(self, item):
        self.items.append(item);

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.items.pop();
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.items[-1];

    def isEmpty(self):
        return not bool(self.items);

    def size (self):
        return len(self.items)
    

myStack = Stack();

myStack.push("A");
myStack.push("B");
myStack.push("C");

print("Stack Class-------------");

print("Stack:", myStack.items);

print("Pop:", myStack.pop());
print("Stack after pop:", myStack.items);
print("Peek:", myStack.peek());
print("Is stack empty?", myStack.isEmpty());
print("Size of stack:", myStack.size())

