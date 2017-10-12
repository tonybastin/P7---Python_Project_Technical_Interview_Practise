''' Question 1 Given two strings s and t, determine whether some anagram of t 
    is a substring of s. For example: if s = "udacity" and t = "ad", then the 
    function returns True. Your function definition should look like: 
    question1(s, t) and return a boolean True or False.
'''

# Find out if s1 and s2 strings are anagram of each other
def question1(s,t):
    count_t = 0
    for i in t:
        if i in s:
            count_t += 1
            
    if count_t == len(t):
        return True
    return False 

# Main program
def main():
    print (question1("udacity", "ciy"))

if __name__ == '__main__':
    main()  


"""
The test cases for function question1(s,t) is given below

Case 1: question1("udacity", "ad") -> True
string with 2 characters reversed from order in S

Case 2: question1("udacity", "da") -> True
string with 2 characters same as in order in S

Case 3: ("udacity, acity") -> True
string with 6 characters same as in order in S

Case 4: ("udacity", "ciy") -> False
string with 2 characters same as in order in S and 1 character out of order.

Case 5: ("udacity", "xyz") -> False
string with new characters not in string S.

Case 6: ("udacity", "") -> True
empty string.

Case 7: ("ad", "udacity" ) -> False
string t's length is greater than string S.
""" 
  
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
    
    