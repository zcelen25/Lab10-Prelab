class Stack:
    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.items = []

    def isEmpty(self) -> bool:
        """
        Checks if the stack is empty.
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item: int) -> None:
        """
        Adds an item to the top of the stack.
        Parameters:
            item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self) -> int:
        """
        Removes the top item from the stack and returns it.
        Returns:
            The top item of the stack.
        Raises:
            IndexError: If the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self) -> int:
        """
        Returns the top item of the stack without removing it.
        Returns:
            The top item of the stack.
        Raises:
            IndexError: If the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def __len__(self) -> int:
        """
        Returns the number of items in the stack.
        Returns:
            int: The number of items in the stack.
        """
        return len(self.items)

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.
        Returns:
            str: The string representation of the stack.
        """
        if self.isEmpty():
            return "[]"
        return f"[{', '.join(map(str, self.items))} <- top of stack"
