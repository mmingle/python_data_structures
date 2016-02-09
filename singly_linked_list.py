
class Node:

	def __init__(self, data, next=None):
		self.data=data
		self.next=next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, next):
		self.next = next



class LinkedList:
	def __init__(self, head=None):
		self.head=head

	def insert(self, data):
		node = Node(data)
		node.set_next(self.head)
		self.head = node
	

	def print_list(self):
		current = self.head
		while current:
			print current.get_data()
			current = current.get_next()

	def size(self):
	    current = self.head
	    count = 0
	    while current:
	        count += 1
	        current = current.get_next()
	    return count

	def delete(self, data):
	    current = self.head
	    previous = None
	    found = False
	    while current and found is False:
	        if current.get_data() == data:
	            found = True
	        else:
	            previous = current
	            current = current.get_next()
	    if current is None:
	        raise LookupError("Data not in list")
	    if previous is None:
	        self.head = current.get_next()
	    else:
	        previous.set_next(current.get_next())

	def search(self, data):
	    current = self.head
	    found = False
	    while current and found is False:
	        if current.get_data() == data:
	            found = True
	        else:
	            current = current.get_next()
	    if current is None:
	        raise LookupError("Data Not in list")
	    return current