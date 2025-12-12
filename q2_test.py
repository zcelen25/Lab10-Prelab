import unittest
from q2 import Queue


class TestQueue(unittest.TestCase):
    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty(), "isEmpty() should return True for an empty queue.")

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertFalse(queue.isEmpty(), "Queue should not be empty after items are enqueued.")
        self.assertEqual(len(queue), 2, "Queue should have 2 items after enqueuing twice.")
        self.assertEqual(str(queue), "Front of queue -> 1, 2 <- Rear of queue", "String representation should match the enqueued items.")

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        dequeued_item = queue.dequeue()
        self.assertEqual(dequeued_item, 1, "dequeue() should return the first enqueued item (1).")
        self.assertEqual(len(queue), 1, "Queue should have 1 item left after dequeuing once.")
        self.assertEqual(str(queue), "Front of queue -> 2 <- Rear of queue", "String representation should update after dequeuing.")

    def test_peek(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 1, "peek() should return the first enqueued item (1) without removing it.")
        self.assertEqual(len(queue), 2, "Queue size should remain the same after peek().")

    def test_len(self):
        queue = Queue()
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(len(queue), 5, "Length of queue should be 5 after enqueuing 5 items.")

    def test_dequeue_empty(self):
        queue = Queue()
        with self.assertRaises(IndexError, msg="Dequeuing from an empty queue should raise IndexError."):
            queue.dequeue()

    def test_peek_empty(self):
        queue = Queue()
        with self.assertRaises(KeyError, msg="Peeking into an empty queue should raise KeyError."):
            queue.peek()

    def test_str_empty(self):
        queue = Queue()
        self.assertEqual(str(queue), "[]", "String representation of an empty queue should be '[]'.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQueue)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
