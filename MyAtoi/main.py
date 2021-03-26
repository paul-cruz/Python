class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        max_limit = 2**31 - 1
        min_limit = -2**31
        isNegative = False
        s = s.strip()
        if s[0] == "-" or s[0] == "+":
            isNegative = s[0] == "-"
            s = s[1:]
        if s[0].isdigit():
            s = int("".join(list(filter(lambda x: x.isdigit(), s))))
            if isNegative:
                s *= -1
            if s > max_limit:
                return max_limit
            elif s < min_limit:
                return min_limit
            else:
                return s
        else:
            return 0


print(Solution.myAtoi("42"))
print(Solution.myAtoi("   -42"))
print(Solution.myAtoi("4193 with words"))
print(Solution.myAtoi("words and 987"))
print(Solution.myAtoi("-91283472332"))
