#!/usr/bin/env python
# @Time    : 2019/1/16 7:03
# @Author  : LiuWei
# @Site    : 
# @File    : numUniqueEmails.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# 929. 独特的电子邮件地址


class Solution:
    """
    首先对本地名称和域名进行分割
    本地名称先消掉字符“.”，再去掉+号后面的字符
    处理后的本地名称加上域名组合，使用集合进行存储
    集合具有去重功能，直接返回集合大小即可
    """
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emailSet = set()
        for email in emails:
            splits = str(email).split("@")
            localName = splits[0]
            domainName = splits[1]

            localName = localName.replace(".", "")
            plusIndex = localName.find("+")
            localName = localName[:plusIndex]

            emailSet.add(localName + "@" + domainName)
        return len(emailSet)


if __name__ == "__main__":
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    solution = Solution()
    print(solution.numUniqueEmails(emails))