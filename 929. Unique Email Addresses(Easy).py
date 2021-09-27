from typing import List


class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:

        def _split_email(word):
            lt = word.split("+")
            return lt[0].replace(".", "")

        for idx, email in enumerate(emails):
            _email = email.split("@")
            _email[0] = _split_email(_email[0])
            emails[idx] = '@'.join(_email)
        return len(set(emails))



    # def numUniqueEmails(self, emails: List[str]) -> int:
    #     for idx, val in enumerate(emails):
    #         temp = ""
    #         flag = 0
    #         for ch in val:
    #             if ch == "@":
    #                 flag = 2
    #                 temp += ch
    #             elif flag == 2 and ch == ".":
    #                 temp += ch
    #             elif ch == "+":
    #                 flag = 1
    #             elif ch == "." or flag == 1:
    #                 continue
    #             else:
    #                 temp += ch
    #
    #         emails[idx] = temp
    #     return len(set(emails))
    #



if __name__ == '__main__':
    print(Solution().numUniqueEmails(emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
