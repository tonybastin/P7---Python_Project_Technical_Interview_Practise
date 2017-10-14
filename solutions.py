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
def helper_palindrome(word):
    # This function checks if a given word is palindrome
    count = len(word) - 1
    for i in word:
        if i.lower() != word[count].lower():
            return ""
        count -=1
    return word 

def question2(a):
    palindrome = ""
    
    # is 'a' is either "" or None return "Enter a valid input"
    if a == "" or a == None or a == " ":
        return "Please enter a valid string"
    
    # splits the given sting into substings
    for i in range(len(a)):        
        for j in range(i+1,len(a)+1):
            substring = a[i:j]
            if helper_palindrome(substring) and substring != " ":
                if len(substring) > len(palindrome):
                    palindrome = substring
                
    # Incase a palindrome is identified with first and last positions as " ", 
    # it willbe removed
    if palindrome[0] == " ":
        palindrome = palindrome[1:-1]
        
    return palindrome


print ("\nPrinting results for question 2 :\n")
print (question2(" ")) 
# should print "Please enter a valid string"
print (question2("TTTTMMM")) 
# should print "TTTT"
print (question2("ATSVBACADCBBCDA")) 
# should print "ADCBBCDA"
print(question2("Anna is taking the kayak to the river")) 
# should print "kayak"


'''
Question 3
Given an undirected graph G, find the minimum spanning tree within G. A minimum 
spanning tree connects all vertices in a graph with the smallest possible total
weight of edges. Your function should take in and return an adjacency list 
structured like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
'''

from heapq import *
 
def prim( nodes, edges ):
    conn = {key:[] for key in nodes} 
    for n1,n2,c in edges:
        conn[ n1 ].append( (c, n1, n2) )
 
    mst = []
    used = set( nodes[ 0 ] )
    usable_edges = conn[ nodes[0] ][:]
    heapify( usable_edges )
    
    # Implementing prim's alogoritham to find the MST
    while usable_edges:
        cost, n1, n2 = heappop( usable_edges )
        if n2 not in used:
            used.add( n2 )
            mst.append( ( n1, n2, cost ) )
 
            for e in conn[ n2 ]:
                if e[ 2 ] not in used:
                    heappush( usable_edges, e )
    
    # Coverting the MST back into the format requied by the question     
    fmst = {key:[] for key in nodes}    
    for n1,n2,c in mst:
        fmst[ n1 ].append( (n2, c) )
        fmst[ n2 ].append( (n1, c) )
        
    return (fmst)

def question3(s1):
    
    # Find the nodes in the graph
    nodes = [key for key in s1]
    
    # Find all the edge combination (undirected) in the graph
    edges = []      
    for key, values in s1.items():        
        for value in values:
            edges.append(( key, value[0], value[1]))    
    
    # Pass the nodes and edges to prim() to find the MST
    return ( prim( nodes, edges ))


print ("\nPrinting results for question 3 :\n")
s1 = {'A': [('B', 2)],
      'B': [('A', 2), ('C', 5)],
      'C': [('B', 5)]}

s2 = {'A': [('B', 7), ('D', 5) ],
      'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
      'C': [('B', 8), ('E', 5)],
      'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
      'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
      'F': [('D', 6), ('E', 8), ('F',11)],
      'G': [('E', 9), ('F', 11)]}

s3 = {'A': [('B', 5), ('D', 4)],
      'B': [('A', 7), ('C', 2), ('D', 3)],
      'C': [('B', 2), ('D', 1)],
      'D': [('A', 4), ('B', 3), ('C', 1)]}
print (question3(s1)) 
# should print {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
print (question3(s2)) 
# should print {'A': [('D', 5), ('B', 7)], 'B': [('A', 7), ('E', 7)], 
# 'C': [('E', 5)], 'D': [('A', 5), ('F', 6)], 
# 'E': [('B', 7), ('C', 5), ('G', 9)], 'F': [('D', 6)], 'G': [('E', 9)]}
print (question3(s3)) 
# should print {'A': [('D', 4)], 'B': [('C', 2)], 'C': [('D', 1), ('B', 2)], 
# 'D': [('A', 4), ('C', 1)]}

'''
Question 4
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node 
from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but 
if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can 
assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should 
look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the 
integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 
are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
'''

def parent(T, n):
	#return parent of n if it exists, otherwise return -1
    numrows = len(T)
    for i in range(numrows):
        if T[i][n] == 1:
            return i
    return -1

def question4(T, r, n1, n2):
    n1_parents = []
    while n1 != r:        
        n1 = parent(T, n1)
        n1_parents.append(n1)
    if len(n1_parents) == 0:
        return -1
    while n2 != r:
        n2 = parent(T, n2)
        if n2 in n1_parents:
            return n2
    return -1


print ("\nPrinting results for question 4 :\n")
print (question4([[0,1,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [1,0,0,0,1],
                  [0,0,0,0,0]],
                 3,
                 1,
                 4))
# should print 3

print (question4([[0,0,0,0,0],
                  [1,0,0,1,0],
                  [0,1,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]],
                 2,
                 0,
                 3))
# should print 1

print (question4([[0,0,0,0,0,0],
                  [1,0,0,1,0,0],
                  [0,1,0,0,1,0],
                  [0,0,0,0,0,0],
                  [0,0,0,0,0,1],
                  [0,0,0,0,0,0]],
                 2,
                 0,
                 5))
# should print 2
