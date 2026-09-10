a = (1, 2, 3, 4, 5, 11, False, "Aryan", 5.2,11, "Narad")
print(a)
print(type(a))

no = a.count(11) # This will count the number of occurrences of the value 11 in the tuple
print(no)

i= a.index("Aryan") # This will return the index of the first occurrence of the value "Aryan" in the tuple
print(i)

repeated = a*2 # This will repeat the tuple a two times
print(repeated)