class Solution:
    # def isValid(s):
    #     open_brackets = s.count("(")
    #     open_curly_brackets = s.count("{")
    #     open_square_brackets = s.count("[")
    #     close_brackets = s.count(")")
    #     close_curly_brackets = s.count("}")
    #     close_square_brackets = s.count("]")
    #     if open_brackets != close_brackets or open_curly_brackets != close_curly_brackets or open_square_brackets != close_square_brackets:
    #         return False
    #     else:
    #         return True
    
    # def isValid2(s):
    #     bracket_amt = s.count("(")
    #     bracket_close_amt = s.count(")")
    #     if bracket_amt == bracket_close_amt:
    #         bracket_indexs = []
    #         for i in range(bracket_amt):
    #             if i == 0:
    #                 bracket_indexs.append(s.index("("))
    #             else:
    #                 bracket_indexs.append(s[bracket_indexs[i-1] + 1:].index("(") + bracket_indexs[i-1] + 1)
    #         print(bracket_amt)
    #         print(bracket_indexs)
    #     else:
    #         print("parenthesis blanced")
    
    def isValid3(s):
        open_brackets = s.count("(")
        close_brackets = s.count(")")
        if open_brackets == close_brackets:
            the_index = s.index("(")
            if s[the_index:].count(")"):
                print("balanced")
            else:
                print("not balance")
        else:
            print("amt not equal")

ans3 = "(what the fuxk beat?? 'you like animu girls?' This dhould me faluse''])"
ans4 = ")("
ans5 = "(0001())"
ans6 = "0(000000(())"

# print(Solution.isValid(ans1))
# print(Solution.isValid(ans3))
# print(Solution.isValid2(ans4))
Solution.isValid3(ans3)
Solution.isValid3(ans4)
Solution.isValid3(ans5)
Solution.isValid3(ans6)