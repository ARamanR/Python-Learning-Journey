devotee = ["aryan", "nitin", "Krishna", "Anmol", "Danny", False, 1, 5.2]
print(devotee)

devotee.append("Abhishek") # This will add "Abhishek" to the end of the list
print(devotee)

devotee.remove(False) # This will remove the value False from the list
print(devotee)

devotee.clear() # This will remove all the elements from the list, making it empty
print(devotee)

Mala = [16, 14, 10, 21, 1, 5, 7, 11, 9, 3, 15, 8, 12, 20, 19, 18, 17, 13, 4, 2, 6]
Mala.sort() # This will sort the list in ascending order
print(Mala)

Mala.sort(reverse=True) # This will sort the list in descending order
print(Mala)

Mala.insert(0, 32) # This will insert the value 32 at index 0
print(Mala)

# 