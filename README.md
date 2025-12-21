# COMP100 Lab 10: Object Oriented Programming - Prelab

This Prelab focuses on Object Oriented Programming in Python, particulary implementation of Stack and Queeue classes. To understand how their operations work, you may check this website for better understanding: https://visualgo.net/en/list


## Question 1: Implementing a Stack Class

Implement a stack using Python lists. A stack is a data structure that follows the Last In, First Out (LIFO) principle.

### Tasks:

- Create a Python class named `Stack`.
- Your class should include the following methods:
  - `__init__(self)`: Constructor to initialize the stack.
  - `isEmpty(self) -> bool`: Checks if the stack is empty. Returns `True` if empty, else `False`.
  - `push(self, item: int) -> None`: Adds an item to the top of the stack.
  - `pop(self) -> int`: Removes and returns the top element of the stack. Raise `IndexError` if the stack is empty.
  - `peek(self) -> int`: Returns the top element of the stack without removing it. Raise `IndexError` if the stack is empty.
  - `__len__(self) -> int`: Returns the number of elements in the stack.
  - `__str__(self) -> str`: Returns a string representation of the stack.
- Use the "q1.py" file for your implementation.

#### Stack Operations and Outputs:
| Operation     | Stack Before       | Action     | Stack After        | Output                              |
|-----------    |--------------------|------------|--------------------|-------------------------------------|
| Push          | `[]`               | Push 1     | `[1]`              | None                                |
| Push          | `[1]`              | Push 2     | `[1, 2]`           | None                                |
| Push          | `[1, 2]`           | Push 3     | `[1, 2, 3]`        | None                                |
| Peek          | `[1, 2, 3]`        | Peek       | `[1, 2, 3]`        | 3                                   |
| Pop           | `[1, 2, 3]`        | Pop        | `[1, 2]`           | 3                                   |
| \_\_str\_\_   | `[1, 2]`           | Stringify  | `[1, 2]`           | "[1, 2 <- top of stack"             |
| \_\_len\_\_   | `[1, 2]`           | Length     | `[1, 2]`           | 2                                   |
| Pop           | `[1, 2]`           | Pop        | `[1]`              | 2                                   |
| Pop           | `[1]`              | Pop        | `[]`               | 1                                   |
| IsEmpty       | `[]`               | Check      | `[]`               | True                                |
| \_\_str\_\_   | `[]`               | Stringify  | `[]`               | "[]"                                |

## Question 2: Implementing a Queue Class

Implement a queue using Python lists. A queue is a data structure that follows the First In, First Out (FIFO) principle.

### Tasks:

- Create a Python class named `Queue`.
- Your class should include the following methods:
  - `__init__(self)`: Constructor to initialize the queue.
  - `isEmpty(self) -> bool`: Checks if the queue is empty. Returns `True` if empty, else `False`.
  - `enqueue(self, item: int) -> None`: Adds an item to the rear of the queue.
  - `dequeue(self) -> int`: Removes and returns the front element of the queue. Raise `IndexError` if the queue is empty.
  - `peek(self) -> int`: Returns the front element of the queue without removing it. Raise `IndexError` if the queue is empty.
  - `__len__(self) -> int`: Returns the number of elements in the queue.
  - `__str__(self) -> str`: Returns a string representation of the queue.
- Implement this in the "q2.py" file.

#### Queue Operations and Outputs:
| Operation | Queue Before      | Action      | Queue After       | Output                             |
|-----------|-------------------|-------------|-------------------|------------------------------------|
| Enqueue   | `[]`              | Enqueue 1   | `[1]`             | None                               |
| Enqueue   | `[1]`             | Enqueue 2   | `[1, 2]`          | None                               |
| Enqueue   | `[1, 2]`          | Enqueue 3   | `[1, 2, 3]`       | None                               |
| Peek      | `[1, 2, 3]`       | Peek        | `[1, 2, 3]`       | 1                                  |
| Dequeue   | `[1, 2, 3]`       | Dequeue     | `[2, 3]`          | 1                                  |
| \_\_str\_\_| `[2, 3]`         | Stringify   | `[2, 3]`          | "Front of queue -> 2, 3 <- Rear of queue"           |
| \_\_len\_\_| `[2, 3]`         | Length      | `[2, 3]`          | 2                                  |
| Dequeue   | `[2, 3]`          | Dequeue     | `[3]`             | 2                                  |
| Dequeue   | `[3]`             | Dequeue     | `[]`              | 3                                  |
| IsEmpty   | `[]`              | Check       | `[]`              | True                               |
| \_\_str\_\_| `[]`             | Stringify   | `[]`              | "[]"                               |

