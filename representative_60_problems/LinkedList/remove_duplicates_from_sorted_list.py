# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # nodeはval(値)と次のノードを指し示すnext(ポインタ)からなる
    if not head:
      return
    
    copy =  head
    while copy.next:
      if copy.val == copy.next.val:
        copy.next = copy.next.next
      else:
        copy = copy.next
    print(head)
    print(copy)
    return head
                