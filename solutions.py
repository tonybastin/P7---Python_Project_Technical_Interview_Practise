''' Question 1 Given two strings s and t, determine whether some anagram of t 
    is a substring of s. For example: if s = "udacity" and t = "ad", then the 
    function returns True. Your function definition should look like: 
    question1(s, t) and return a boolean True or False.
'''

def question1(s,t):
    # convert 's' and 't' to lower case
    s = s.lower()
    t = t.lower()
    
    # check if length of 's' is lower than 't'
    if len(s) < len(t):
        return False
    
    # split 's' into substrings having length of 't'
    substrings = []
    for i in range(len(s)-len(t)+1):        
        substrings.append(s[i:i+len(t)])
    
    # for each substring check whether all letters in 't' 
    # excist in 's' and return 'True' if found   
    for substring in substrings:
        count_substring = 0
        for i in t:
            if i in substring:
                count_substring += 1                    
        if count_substring == len(t):
            return True
    return False        


print ("\nPrinting results for question 1 :\n")
print (question1("Udacity", "ud")) 
# should print True
print (question1("udacity", "ciy")) 
# should print False
print (question1("ty", "udacity"))  
# should print False
print (question1("", "")) 
# should print True 
  
'''Question 2
    Given a string a, find the longest palindromic substring contained in a. 
    Your function definition should look like question2(a), and return a 
    string.
'''
