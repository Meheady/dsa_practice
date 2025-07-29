stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack);

#peek

print("Peek:", stack[-1])

#pop

print("Pop:", stack.pop())

#stack after pop

print("Stack after pop:", stack)

#is stack empty
is_empty = not bool(stack)
print("Is stack empty?", is_empty)

#size of stack
print("Size of stack:", len(stack))