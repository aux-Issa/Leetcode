# https://leetcode.com/problems/unique-email-addresses/submissions/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_dic = {"local":[], "domain":[]}
        for email in emails:
            emails_list = email.split('@')
            # localの.を削除し，+以降を除去
            emails_dic['local'].append(emails_list[0].replace('.', '').split('+')[0])
            emails_dic['domain'].append(emails_list[1])

        i = 0
        ans = []
        for l in emails_dic["local"]:
            ans.append(l + '@' + emails_dic["domain"][i])
            i += 1
        # 集合型にして重複を削除
        ans = set(ans)
        # リスト型に戻す
        ans = list(ans)
        print(ans)
        return len(ans)