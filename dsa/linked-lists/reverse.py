from node import Node

def reverse(head):
  rev = Node(head.value)
  current = head.next

  while current is not None:
    rev = Node(current.value, rev)
    current = current.next

  return rev


lst = Node(0)
current = lst

for i in range(1, 6):
  current.next = Node(i)
  current = current.next

current = lst

while current is not None:
  print(current.value)
  current = current.next

rev = reverse(lst)
current = rev

while current is not None:
  print(current.value)
  current = current.next
