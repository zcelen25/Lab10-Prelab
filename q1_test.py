import unittest
from q1 import Stack


class TestStack(unittest.TestCase):
    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty(), "isEmpty() should return True for an empty stack.")

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(len(stack), 1, "Stack should have 1 item after pushing 1 item.")
        self.assertFalse(stack.isEmpty(), "Stack should not be empty after an item is pushed.")

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        popped_item = stack.pop()
        self.assertEqual(popped_item, 2, "pop() should return the last pushed item (2).")
        self.assertEqual(len(stack), 1, "Stack should have 1 item left after popping once.")

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        top_item = stack.peek()
        self.assertEqual(top_item, 2, "peek() should return the last pushed item (2) without removing it.")
        self.assertEqual(len(stack), 2, "Stack size should remain the same after peek().")

    def test_len(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        self.assertEqual(len(stack), 5, "Length of stack should be 5 after pushing 5 items.")

    def test_pop_empty(self):
        stack = Stack()
        with self.assertRaises(IndexError, msg="Popping from an empty stack should raise IndexError."):
            stack.pop()

    def test_peek_empty(self):
        stack = Stack()
        with self.assertRaises(IndexError, msg="Peeking into an empty stack should raise IndexError."):
            stack.peek()

    def test_str(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(str(stack), "[1, 2 <- top of stack", "String representation of the stack should be '[1, 2 <- top of stack'.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStack)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
