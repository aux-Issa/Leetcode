# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummyHead = ListNode()
    dummyHead.next = head
    # 順番に見ていくポインター
    ptr = dummyHead
      while ptr.next and ptr.next.next:
        # 隣あうノードの値が重複している場合
        if ptr.next.val ==  ptr.next.next.val:
          # 連続する重複の最後のノードを見つける
          copy = ptr.next
          while copy.val and (copy.val == copy.next.val):
            # 重複が連続する限りcopyを進めることで，どこのノードまで重複が続いているか特定する
            copy = copy.next
            # ポインターを「連続重複ノードたちの最後の右隣」を指すようにする(重複を排除している)
            ptr.next = copy.next
                
            # 重複しない場合はポインターを隣に移す
            else:
              ptr = ptr.next
        # なぜdummyHeadを返すの？
      return dummyHead.next
                