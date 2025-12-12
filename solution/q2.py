class Queue:
    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.items = []

    def isEmpty(self) -> bool:
        """
        Checks if the queue is empty.
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def enqueue(self, item: int) -> None:
        """
        Adds an item to the rear of the queue.
        Parameters:
            item (int): The item to be added to the queue.
        """
        self.items.append(item)

    def dequeue(self) -> int:
        """
        Removes the front item from the queue and returns it.
        Returns:
            int: The front item of the queue.
        Raises:
            IndexError: If the queue is empty.
        """
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self) -> int:
        """
        Returns the front item of the queue without removing it.
        Returns:
            int: The front item of the queue.
        Raises:
            IndexError: If the queue is empty.
        """
        if self.isEmpty():
            raise KeyError("peek from empty queue")
        return self.items[0]

    def __len__(self) -> int:
        """
        Returns the number of items in the queue.
        Returns:
            int: The number of items in the queue.
        """
        return len(self.items)

    def __str__(self) -> str:
        """
        Returns a string representation of the queue.
        Returns:
            str: The string representation of the queue.
        """
        if self.isEmpty():
            return "[]"
        return f"Front of queue -> {', '.join(map(str, self.items))} <- Rear of queue"
