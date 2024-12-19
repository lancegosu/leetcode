# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
  # result = 0
  # current = head
  # while current is not None:
  #   result += current.val
  #   current = current.next

  # return result

  result = 0
  if head == None:
    return result

  result = head.val + sum_list(head.next)
  return result
  pass # todo
