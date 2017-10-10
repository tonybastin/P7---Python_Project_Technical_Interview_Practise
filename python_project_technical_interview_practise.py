''' Question 1 Given two strings s and t, determine whether some anagram of t 
    is a substring of s. For example: if s = "udacity" and t = "ad", then the 
    function returns True. Your function definition should look like: 
    question1(s, t) and return a boolean True or False.
'''
def question1(s,t):
    count_t = 0
    for i in t:
        if i in s:
            count_t += 1
            
    if count_t == len(t):
        return True
    return False   