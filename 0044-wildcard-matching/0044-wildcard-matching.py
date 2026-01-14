class Solution(object):
    def isMatch(self, s, p):
        s_ptr, p_ptr = 0, 0
        star_ptr, s_match = -1, 0

        while s_ptr < len(s):
            if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_ptr = p_ptr
                s_match = s_ptr
                p_ptr += 1
            elif star_ptr != -1:
                p_ptr = star_ptr + 1
                s_match += 1
                s_ptr = s_match
            else:
                return False
        
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
        
        return p_ptr == len(p)