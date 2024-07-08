# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from exceptions import Empty


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""

        __slots__ = "_element", "_next"  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ------------------------------- queue methods -------------------------------
    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0  # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element  # front aligned with head of list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # special case as queue is empty
            self._tail = None  # removed head had been the tail
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)  # node will be new tail node
        if self.is_empty():
            self._head = newest  # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest  # update reference to tail node
        self._size += 1

    def concatenate(self, Q2):
        """
        Concatenates another LinkedQueue to the end of this queue.
        """
        # Ensure the argument Q2 is a LinkedQueue
        if not isinstance(Q2, LinkedQueue):
            raise TypeError("Q2 must be a LinkedQueue")

        # No action needed if Q2 is empty
        if Q2.is_empty():
            return

        # If the current queue is empty, set its head to Q2's head
        if self.is_empty():
            self._head = Q2._head
        else:
            # Link the current queue's tail to Q2's head
            self._tail._next = Q2._head

        # Update the current queue's tail to Q2's tail
        self._tail = Q2._tail
        # Increase the size of the current queue by Q2's size
        self._size += Q2._size

        # Reset Q2 to an empty state
        Q2._head = None
        Q2._tail = None
        Q2._size = 0


def main():
    Q1 = LinkedQueue()
    Q2 = LinkedQueue()

    # Enqueue elements in Q1
    for i in range(5):
        Q1.enqueue(i)

    # Enqueue elements in Q2
    for j in range(5, 10):
        Q2.enqueue(j)

    print("Q1 before concatenate:")
    while not Q1.is_empty():
        print(Q1.dequeue(), end=" ")

    # Re-enqueue elements to Q1 for testing
    for i in range(5):
        Q1.enqueue(i)

    print("\nQ2 before concatenate:")
    while not Q2.is_empty():
        print(Q2.dequeue(), end=" ")

    # Re-enqueue elements to Q2 for testing
    for j in range(5, 10):
        Q2.enqueue(j)

    # Concatenate Q2 to Q1
    Q1.concatenate(Q2)

    print("\nQ1 after concatenate:")
    while not Q1.is_empty():
        print(Q1.dequeue(), end=" ")

    print("\nQ2 after concatenate:")
    print("Q2 is empty" if Q2.is_empty() else "Q2 is not empty")


if __name__ == "__main__":
    main()
