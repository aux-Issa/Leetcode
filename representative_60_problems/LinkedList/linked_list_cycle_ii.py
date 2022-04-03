# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # headがNoneの場合
        if not head:
            return
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # slowを最初のindexに戻し，fastとslowの移動速度を統一する
                # 再び重なった時のslowのindexが答え
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow
        return
            
        
        