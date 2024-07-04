# Lab Assignment #4 – Using ADT Stacks, Queues, and Lists

## Exercise 1

**If your first name starts with a letter from A-J inclusively:**

Suppose we want to extend the **PositionalList** ADT with a method,
***indexOf(p)***, that returns the current index of the element stored
at position p. Write this method using only other methods of the
**PositionalList** interface (not details of our LinkedPositionalList
implementation).

Write the necessary code to test the method. **Hint:** Count the steps
while traversing the list until encountering position p.

**If your first name starts with a letter from K-Z inclusively:**

Suppose we want to extend the PositionalList abstract data type with a
method, ***findPosition(e)***, that returns the first position
containing an element equal to e (or null if no such position exists).

Implement this method using only existing methods of the PositionalList
interface (not details of our LinkedPositionalList implementation).
Write the necessary code to test the method.

**Hint:** use the *equals* method to test equality.

(5 marks)

## Exercise 2

**If your first name starts with a letter from A-J inclusively:**

Implement a method with signature *transfer(S, T)* that transfers all
elements from stack S onto stack T, so that the element that starts at
the top of S is the first to be inserted onto T, and the element at the
bottom of S ends up at the top of T. Write the necessary code to test
the method.

(2 marks)

**If your first name starts with a letter from K-Z inclusively:**

Write a recursive method for removing all the elements from a stack S.
Write the necessary code to test the method.

**Hint:** First check if the stack is already empty.

## Exercise 3

Implement a method with signature ***concatenate(LinkedQueue\<E\> Q2)***
for the **LinkedQueue\<E\>** class that takes all elements of Q2 and
appends them to the end of the original queue. The operation should run
in **O(1)** time and should result in Q2 being an empty queue. Write the
necessary code to test the method. **Hint:** You may just modify the
SinglyLinkedList class to add necessary support.

(3 marks)

## Distribution Codes

### positional_list.py

```python
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

from .doubly_linked_base import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
  """A sequential container of elements allowing positional access."""

  #-------------------------- nested Position class --------------------------
  class Position:
    """An abstraction representing the location of a single element.

    Note that two position instaces may represent the same inherent
    location in the list.  Therefore, users should always rely on
    syntax 'p == q' rather than 'p is q' when testing equivalence of
    positions.
    """

    def __init__(self, container, node):
      """Constructor should not be invoked by user."""
      self._container = container
      self._node = node
    
    def element(self):
      """Return the element stored at this Position."""
      return self._node._element
      
    def __eq__(self, other):
      """Return True if other is a Position representing the same location."""
      return type(other) is type(self) and other._node is self._node

    def __ne__(self, other):
      """Return True if other does not represent the same location."""
      return not (self == other)               # opposite of __eq__
    
  #------------------------------- utility methods -------------------------------
  def _validate(self, p):
    """Return position's node, or raise appropriate error if invalid."""
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    if p._node._next is None:                  # convention for deprecated nodes
      raise ValueError('p is no longer valid')
    return p._node

  def _make_position(self, node):
    """Return Position instance for given node (or None if sentinel)."""
    if node is self._header or node is self._trailer:
      return None                              # boundary violation
    else:
      return self.Position(self, node)         # legitimate position
    
  #------------------------------- accessors -------------------------------
  def first(self):
    """Return the first Position in the list (or None if list is empty)."""
    return self._make_position(self._header._next)

  def last(self):
    """Return the last Position in the list (or None if list is empty)."""
    return self._make_position(self._trailer._prev)

  def before(self, p):
    """Return the Position just before Position p (or None if p is first)."""
    node = self._validate(p)
    return self._make_position(node._prev)

  def after(self, p):
    """Return the Position just after Position p (or None if p is last)."""
    node = self._validate(p)
    return self._make_position(node._next)

  def __iter__(self):
    """Generate a forward iteration of the elements of the list."""
    cursor = self.first()
    while cursor is not None:
      yield cursor.element()
      cursor = self.after(cursor)

  #------------------------------- mutators -------------------------------
  # override inherited version to return Position, rather than Node
  def _insert_between(self, e, predecessor, successor):
    """Add element between existing nodes and return new Position."""
    node = super()._insert_between(e, predecessor, successor)
    return self._make_position(node)

  def add_first(self, e):
    """Insert element e at the front of the list and return new Position."""
    return self._insert_between(e, self._header, self._header._next)

  def add_last(self, e):
    """Insert element e at the back of the list and return new Position."""
    return self._insert_between(e, self._trailer._prev, self._trailer)

  def add_before(self, p, e):
    """Insert element e into list before Position p and return new Position."""
    original = self._validate(p)
    return self._insert_between(e, original._prev, original)

  def add_after(self, p, e):
    """Insert element e into list after Position p and return new Position."""
    original = self._validate(p)
    return self._insert_between(e, original, original._next)

  def delete(self, p):
    """Remove and return the element at Position p."""
    original = self._validate(p)
    return self._delete_node(original)  # inherited method returns element

  def replace(self, p, e):
    """Replace the element at Position p with e.

    Return the element formerly at Position p.
    """
    original = self._validate(p)
    old_value = original._element       # temporarily store old element
    original._element = e               # replace with new element
    return old_value                    # return the old element value
```

### doubly_linked_base.py

```python
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

class _DoublyLinkedBase:
  """A base class providing a doubly linked list representation."""

  #-------------------------- nested _Node class --------------------------
  # nested _Node class
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = '_element', '_prev', '_next'            # streamline memory

    def __init__(self, element, prev, next):            # initialize node's fields
      self._element = element                           # user's element
      self._prev = prev                                 # previous node reference
      self._next = next                                 # next node reference

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty list."""
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer                  # trailer is after header
    self._trailer._prev = self._header                  # header is before trailer
    self._size = 0                                      # number of elements

  #-------------------------- public accessors --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0

  #-------------------------- nonpublic utilities --------------------------

  def _insert_between(self, e, predecessor, successor):
    """Add element e between two existing nodes and return new node."""
    newest = self._Node(e, predecessor, successor)      # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element                             # record deleted element
    node._prev = node._next = node._element = None      # deprecate node
    return element                                      # return deleted element
```

### linked_queue.py

```python
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

from ..exceptions import Empty

class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next

  #------------------------------- queue methods -------------------------------
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0                          # number of queue elements

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
      raise Empty('Queue is empty')
    return self._head._element              # front aligned with head of list

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                     # special case as queue is empty
      self._tail = None                     # removed head had been the tail
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None)            # node will be new tail node
    if self.is_empty():
      self._head = newest                   # special case: previously empty
    else:
      self._tail._next = newest
    self._tail = newest                     # update reference to tail node
    self._size += 1
```

```python
# exceptions.py

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass
```

### singly_linked_list.py

```python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            return None
        return self.head.element

    def last(self):
        if self.is_empty():
            return None
        return self.tail.element

    def add_first(self, e):
        newest = Node(e, next_node=self.head)
        self.head = newest
        if self.is_empty():
            self.tail = self.head
        self.size += 1

    def add_last(self, e):
        newest = Node(e)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next_node = newest
        self.tail = newest
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        answer = self.head.element
        self.head = self.head.next_node
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return answer

    def __eq__(self, other):
        if not isinstance(other, SinglyLinkedList) or self.size != len(other):
            return False

        node1, node2 = self.head, other.head
        while node1 is not None:
            if node1.element != node2.element:
                return False
            node1, node2 = node1.next_node, node2.next_node

        return True

    def __str__(self):
        result = []
        node = self.head
        while node is not None:
            result.append(str(node.element))
            node = node.next_node
        return "(" + ", ".join(result) + ")"


if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.add_first("MSP")
    list1.add_last("ATL")
    list1.add_last("BOS")
    list1.remove_first()
    print(list1)
```
