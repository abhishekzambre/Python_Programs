class ListNode:
	def __init__(self, data=0, next_node=None):
		self.data = data
		self.next_node = next_node

	def print_list(self):
		temp = self
		while(temp):
			print(str(temp.data), end=" ")
			temp = temp.next_node
		print()

	def insert_after(node, new_node):
		new_node.next_node = node.next_node
		node.next_node = new_node

	def search(self, data):
	    current = self
	    found = False
	    while current and found is False:
	        if current.data == data:
	            found = True
	        else:
	            current = current.next_node
	    if current is None:
	        raise ValueError("Data not in list")
	    return current

def addTwoNumbers(l1, l2):
	print("List A: ", end="")
	l1.print_list()
	print("List B: ", end="")
	l2.print_list()
	pass

l1 = ListNode(2)
n1 = ListNode(4)
l1.insert_after(n1)
n2 = ListNode(3)
n1.insert_after(n2)

l2 = ListNode(5)
n3 = ListNode(6)
l2.insert_after(n3)
n4 = ListNode(4)
n3.insert_after(n4)
n5 = ListNode(8)
n4.insert_after(n5)

addTwoNumbers(l1, l2)