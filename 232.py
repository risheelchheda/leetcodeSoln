def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = []   # initialize front stack
        self.back = []    # initialize back stack

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.back.append(x)    # add element to back stack

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()            # move elements from back stack to front stack
        return self.front.pop() # remove and return the first element from front stack

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.front:     # if front stack is empty
            while self.back:   # move all elements from back stack to front stack
                self.front.append(self.back.pop())
        return self.front[-1]  # return the last element in front stack (i.e., the first element in queue)

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.front and not self.back  # queue is empty if both stacks are empty
