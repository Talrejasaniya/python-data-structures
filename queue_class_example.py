# Define a class named Queue to implement queue operations
class Queue():
    # Constructor to initialize an empty list to store queue elements
    def __init__(self):
        self.values = []

    # Method to add an element at the end of the queue
    def enqueue(self, x):
        self.values.append(x)

    # Method to remove and return the front element of the queue
    def dequeue(self):
        front = self.values[0]        # Get the front element
        self.values = self.values[1:] # Remove the front element
        return front

# Create a Queue object
q1 = Queue()

# Enqueue elements
q1.enqueue(30)
q1.enqueue(20)
q1.enqueue(10)

# Print current queue
print(q1.values)     # Output: [30, 20, 10]

# Dequeue the front element and print it
print(q1.dequeue())  # Output: 30

# Print the queue after dequeue operation
print(q1.values)     # Output: [20, 10]
