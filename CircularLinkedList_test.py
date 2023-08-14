from CircularLinkedList import CircularLinkedList

def test_append():
  lista = CircularLinkedList()
  for letter in "APPEND":
      lista.append(letter)
  assert lista.display() == "[A, P, P, E, N, D]"

def test_prepend():
  lista = CircularLinkedList()
  for letter in "DNEPERP":
      lista.prepend(letter)
  assert lista.display() == "[P, R, E, P, E, N, D]"

def test_remove():
  lista = CircularLinkedList()
  for n in range(1, 11):
      lista.append(n)
  lista.remove(1)
  lista.remove(5)
  lista.remove(10)
  assert lista.display() == "[2, 3, 4, 6, 7, 8, 9]"

def test_findindex():
  lista = CircularLinkedList()
  for letter in "TEST":
    lista.append(letter)
  assert lista.findindex("S") == 2
  assert lista.findindex("T") == 0

def test_len():
  lista = CircularLinkedList()
  for letter in "TEST":
    lista.append(letter)
  assert len(lista) == 4