# Define a class named Stack to implement stack operations
class Stack():
    # Constructor to initialize an empty list to store stack elements
    def __init__(self):
        self.values = []

    # Method to push an element onto the stack
    def push(self, x):
        # Insert element at the beginning of the list (top of stack)
        self.values = [x] + self.values

    # Method to pop the top element from the stack
    def pop(self):
        # Remove and return the first element (top of stack)
        return self.values.pop(0)

# Create a Stack object
s = Stack()

# Push elements onto the stack
s.push(10)
s.push(20)
s.push(30)

# Print current stack
print(s.values)  # Output: [30, 20, 10]

# Pop the top element and print it
print(s.pop())   # Output: 30

# Print the stack after popping
print(s.values)  # Output: [20, 10]
