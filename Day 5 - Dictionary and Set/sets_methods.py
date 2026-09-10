s= {32,65,98,65,32, 32, 32,"aman"} # This is a set with some duplicate elements.

print(s) # print the set and its type

print(len(s)) # print the length of the set

s.add(100) # add a new element to the set
print(s) # print the set after adding a new element

s.remove(32) # remove a specific element from the set
print(s) # print the set after removing an element

s.discard(1) # remove a specific element from the set, if it is not present do nothing
print(s) # print the set after discarding an element

s.pop() # remove and return an arbitrary element from the set
print(s) # print the set after popping an element

s.difference_update({98}) # remove all the elements of another set from the set
print(s) # print the set after updating it

s.clear() # remove all the elements from the set
print("jai shree ram") # print the empty set after clearing it


s1 = {3,4,5,1,67,89,90}
s2 = {9,1,2,3,4,5,85,65}
print(s1.union(s2)) # print the union of two sets
print(s1.intersection(s2)) # print the common values of two sets
print(s1.difference(s2)) # print the difference of two sets