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
