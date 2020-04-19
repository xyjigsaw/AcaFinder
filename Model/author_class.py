# Name: author_class
# Author: Reacubeth
# Time: 2020/2/28 14:40
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*


class AuthorItem:
    authorID = None
    authorName = None
    pc = None
    cn = None
    hi = None
    pi = None
    upi = None

    def __init__(self, answer):
        self.authorID = answer['authorID']
        self.authorName = answer['authorName']
        self.pc = answer['pc']
        self.cn = answer['cn']
        self.hi = answer['hi']
        self.pi = answer['pi']
        self.upi = answer['upi']
