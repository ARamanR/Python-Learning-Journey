marks = {
    "Aman": 90, 
    "Rahul": 85, 
    "Priya": 92,
    0 : "Pyare"
}

print(marks.keys()) # print all the keys in the dictionary
print(marks.values()) # print all the values in the dictionary
print(marks.items()) # print all the items in the dictionary
print(marks.get("Aman")) # print the value of a specific key
print(marks.get("jai", "Not Found")) # print the value of a specific key, if not found print "Not Found"
print(marks.update({"Aman": 99}) ) # update the value of an existing key and add a new key-value pair
print(marks.setdefault("gannu", 100)) # print the value of a specific key, if not found set it to 100 and return it
print(marks) # print the whole dictionary after setting a new key-value pair

print(marks.pop("Aman")) # remove a specific key and return its value
print(marks) # print the whole dictionary after removing a key

print(marks.popitem()) # remove the last inserted key-value pair and return it  
print(marks) # print the whole dictionary after removing the last inserted key-value pair
marks.clear(); print("jai shree ram") # remove all the key-value pairs from the dictionary and print "jai shree ram"
print(marks) # print the whole dictionary after clearing it