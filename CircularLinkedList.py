class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  
class CircularLinkedList:
  def __init__(self):
    self.head = None
    self._size = 0

  def append(self, elem):
    new_node = Node(elem)
    if not self.head:
      self.head = new_node
      self.head.next = self.head
    else:
      pointer = self.head
      while (pointer.next != self.head):
        pointer = pointer.next
      pointer.next = new_node
      new_node.next = self.head
    self._size = self._size+1

  def prepend(self, elem):
    new_node = Node(elem)
    pointer = self.head
    new_node.next = self.head
    if not self.head:
      new_node.next = new_node
    else:
      while (pointer.next != self.head):
        pointer = pointer.next
      pointer.next = new_node
    self.head = new_node
    self._size = self._size+1

  def remove(self, elem):
    start_size = self._size
    if self.head == None:
      raise ValueError("empty list")
    elif self.head.data == elem:
      pointer = self.head
      while (pointer.next != self.head):
        pointer = pointer.next
      self.head = self.head.next
      pointer.next = self.head
      self._size = self._size-1
    else:
      prev = self.head
      pointer = self.head.next
      while True:
        if pointer.data == elem:
          self._size = self._size-1
          prev.next = pointer.next
        prev = prev.next
        pointer = pointer.next
        if pointer == self.head:
          break
    if start_size == self._size: 
      raise ValueError(f"{elem} is not in list")

  def findindex(self, elem):
    pointer = self.head
    idx = 0
    if self.head.data == elem:
      return 0
    while True:
      pointer = pointer.next
      idx += 1
      if pointer.data == elem:
        return idx
      if pointer.next == self.head:
        break
    raise ValueError(f"{elem} is not in list")

  def display(self):
    pointer = self.head

    if pointer:
      r = "["
      while (pointer.next != self.head):
        r += str(pointer.data) + ", "
        pointer = pointer.next
      r += str(pointer.data)
      r += "]"
    else:
      r = "[]"
    return r

  def __len__(self):
    return self._size

  def __repr__(self):
    pointer = self.head

    if pointer:
      r = "["
      while (pointer.next != self.head):
        r += str(pointer.data) + ", "
        pointer = pointer.next
      r += str(pointer.data)
      r += "]"
    else:
      r = "[]"
    return r

  def __str__(self):
    return self.__repr__()