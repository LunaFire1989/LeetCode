class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		head, curr, carry = None, None, 0
		while l1 != None or l2 != None:
			if l1 == None:
				val = l2.val + carry
				l2 = l2.next
			elif l2 == None:
				val = l1.val + carry
				l1 = l1.next
			else:
				val = l1.val + l2.val + carry
				l1, l2 = l1.next, l2.next
			digit, carry = val % 10, val /10	
			tmp = ListNode(digit)
			if head == None:
				head, curr = tmp, tmp
			else:
				curr.next = tmp
				curr = curr.next
		if carry != 0:
			tmp = ListNode(carry)
			curr.next = tmp
		return head

def initList(nums):
	head = None
	for x in list(reversed(nums)):
		tmp = ListNode(x)
		tmp.next = head
		head = tmp	
	return head

def printList(head):
	while head != None:
		print head.val
		head = head.next

l1 = initList([2, 4, 3])
l2 = initList([5, 6, 4])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
printList(result)