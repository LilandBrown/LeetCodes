class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for i in tokens:
            if i == "-":
                st = s.pop()
                s.append(s.pop() - st)
            elif i == "+":
                st = s.pop()
                s.append(s.pop() + st)
            elif i == "/":
                s1 = s.pop()
                s2 = s.pop()
                s.append(math.trunc(s2 / s1) )
            elif i == "*":
                s.append(s.pop() * s.pop())
            else:
                s.append(int(i))
        return s[0]