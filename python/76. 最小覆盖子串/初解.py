# -*- coding:utf-8 -*-
from collections import defaultdict


class Solution:
    @staticmethod
    def minWindow(s, t):
        if len(s) < len(t):
            return ''
        left = right = 0
        cc = ''

        while True:
            while not include_check(t, s[left:right]):
                if right < len(s):
                    right += 1
                elif len(t) < (right - left):
                    left += 1
                else:
                    break

            while include_check(t, s[left:right]):
                if not cc or len(cc) > len(s[left:right]):
                    cc = s[left:right]
                left += 1

            if len(t) >= (right - left) and right == len(s):
                break

        if cc:
            return cc
        else:
            return ''


def include_check(res, n):
    res = tran_dict(res)
    n = tran_dict(n)

    result = None
    for key in res:
        if (key in n) and (res[key] <= n[key]):
            result = True
        else:
            return False
    return result


def tran_dict(n):
    n_dict = defaultdict(int)
    for i in n:
        n_dict[i] += 1
    return n_dict


if __name__ == '__main__':
    # a = "ADOBECODEBANC"
    # b = "ABC"
    a = 'aa'
    b = 'aa'
    print(Solution.minWindow(a, b))
