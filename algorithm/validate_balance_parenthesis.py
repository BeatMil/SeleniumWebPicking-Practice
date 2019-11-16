class Solution:
    def isValid(s):
        open_brackets = s.count("(")
        open_curly_brackets = s.count("{")
        open_square_brackets = s.count("[")
        close_brackets = s.count(")")
        close_curly_brackets = s.count("}")
        close_square_brackets = s.count("]")
        if open_brackets != close_brackets or open_curly_brackets != close_curly_brackets or open_square_brackets != close_square_brackets:
            return False
        else:
            return True

ans1 = "[(((())))]"
ans2 = "((())"
ans3 = "(what the fuxk beat?? 'you suck' This dhould me faluse''])"

print(Solution.isValid(ans1))
print(Solution.isValid(ans3))
