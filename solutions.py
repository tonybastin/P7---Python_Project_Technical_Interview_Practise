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
    
    # for each substring of 's' check whether all  
    # letters in 't' excist and return 'True' if found
    for i in range(len(s)-len(t)+1):
        count_substring = 0
        for j in t:
            if j in s[i:i+len(t)]:
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

# Implementing prim's alogoritham to find the MST
def prim( nodes, edges ):
    mst = []
    # 1) Initialize the tree with a single vertex
    used = set( nodes[ 0 ] )
    usable_edges = edges[ nodes[0] ][:]
    heapify( usable_edges )
    
    # 2) Grow the tree by one edge: of the edges that 
    #    connect the tree to vertices not yet in the tree, 
    #    find the minimum-weight edge, and transfer it to the tree.
    # 3) Repeat step 2 (until all vertices are in the tree)
    while usable_edges:
        cost, n1, n2 = heappop( usable_edges )
        if n2 not in used:
            used.add( n2 )
            mst.append( ( n1, n2, cost ) )
 
            for e in edges[ n2 ]:
                if e[ 2 ] not in used:
                    heappush( usable_edges, e )
    
    # Coverting the MST back into the format requied by the question     
    fmst = {key:[] for key in nodes}    
    for n1,n2,cost in mst:
        fmst[ n1 ].append( (n2, cost) )
        fmst[ n2 ].append( (n1, cost) )
        
    return (fmst)

def question3(s1):
    
    # Find the nodes in the graph
    nodes = [key for key in s1]
    
    # Converting all the edge combination (undirected) into required format
    edges = { key:[] for key in nodes}      
    for key, values in s1.items():        
        for value in values:
            edges[key].append((value[1],  key, value[0] ))    
        
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
print (question3(s1),"\n") 
# should print {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
print (question3(s2),"\n") 
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

'''
Question 5
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, 
the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll 
is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below 
to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while counter <= position and current:
            if counter == position:
                return current
            counter += 1
            current = current.next
        return None
    
    def get_length(self):
        counter = 0 
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter
    
def question5(ll, m):
    position = ll.get_length() - m + 1
    #print (position)
    return ll.get_position(position).value     


print ("\nPrinting results for question 5 :\n")
# Test cases
# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

print (question5(ll, 4))
# Should print 1
print (question5(ll, 3))
# Should print 2
print (question5(ll, 1))
# Should print 4