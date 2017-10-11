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
    
'''Question 2
    Given a string a, find the longest palindromic substring contained in a. 
    Your function definition should look like question2(a), and return a 
    string.
'''

def helper_palindrome(word):
    count = len(word) - 1
    for i in word:
        if i.lower() != word[count].lower():
            return ""
        count -=1
    return word 

def question2(a):
    palindrome = ""
    for i in range(len(a)-1):        
        if len(helper_palindrome(a[i:]))>len(palindrome):
            palindrome = helper_palindrome(a[i:])
        if len(helper_palindrome(a[:i+1]))>len(palindrome):
            palindrome = helper_palindrome(a[:i+1])
        
    return palindrome
    
    