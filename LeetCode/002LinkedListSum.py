class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def print_list(self):
        temp = self
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next
        print()

    def insert_after(node, new_node):
        new_node.next = node.next
        node.next = new_node

    def search(self, data):
        current = self
        found = False
        while current and found is False:
            if current.data == data:
                found = True
            else:
                current = current.next
        if current is None:
            raise ValueError("Data not in list")
        return current


def addTwoNumbers(l1, l2):
    temp1 = l1
    temp2 = l2
    rem = 0
    first = True
    while (temp1 or temp2):
        if (temp1):
            d1 = temp1.data
            temp1 = temp1.next
        else:
            d1 = 0
        if (temp2):
            d2 = temp2.data
            temp2 = temp2.next
        else:
            d2 = 0
        sum_digit = d1 + d2 + rem
        if (sum_digit > 9):
            rem = int(sum_digit / 10)
        else:
            rem = 0
        if first:
            ans_l = ListNode(sum_digit % 10)
            temp3 = ans_l
            first = False
        else:
            new_node = ListNode(sum_digit % 10)
            temp3.insert_after(new_node)
            temp3 = new_node

    if (rem != 0):
        new_node = ListNode(rem)
        temp3.insert_after(new_node)
    ans_l.print_list()

    pass


l1 = ListNode(5)
# n1 = ListNode(4)
# l1.insert_after(n1)
# n2 = ListNode(3)
# n1.insert_after(n2)
l1.print_list()

l2 = ListNode(5)
# n3 = ListNode(6)
# l2.insert_after(n3)
# n4 = ListNode(4)
# n3.insert_after(n4)
# n5 = ListNode(5)
# n4.insert_after(n5)
l2.print_list()

addTwoNumbers(l1, l2)
