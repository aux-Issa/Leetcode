# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      # 返すようのlinkedlistを作成
      root = ListNode()
      ans = root
      # 繰り上がりの値を定義
      carry = 0

      # l1またはl2がnullではないかをチェック
      while l1 or l2:
        # 桁の値を定義
        n = 0
          
        if l1 and l2:   # l1,l2共にtruthyの時
          n = (l1.val + l2.val + carry) % 10
          carry = int((l1.val + l2.val) / 10)
          l1 = l1.next
          l2 = l2.next
        elif l1:   # l2がnone
          n = (l1.val) % 10
          carry = int((l1.val) / 10)
          l1 = l1.next
        elif l2:   # l1がnone
          n = (l2.val) % 10
          carry = int((l2.val) / 10)
          l2 = l2.next
        else:     
          # throw exception
          print('error occurs')

        ans.val = n
        
     # l1とl2が未だnoneで無ければ，新たにnodeを作る
        if l1 or l2:
          ans.next = ListNode()
          ans = ans.next

      # edgecase: whileを抜けた後(つまりl1とl2の要素を全て見終わった後)にまだcarryが残っていれば新しくnodeを作る
      if carry == 1:
        ans.next = ListNode(1)
      return root
            
        
    
    
# edgecase: 以下の場合一つノードを足す必要がある
# 999
# 1
# _____
# 0001