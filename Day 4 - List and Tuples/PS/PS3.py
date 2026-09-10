# 3. Check that a tuple type cannot be changed in python.
a = (1, 2, 3,)
print("Original tuple:", a)
try:
    a[0] = 10
except TypeError as e:
    print("Error:", e)
print("Tuple after attempted change:", a)