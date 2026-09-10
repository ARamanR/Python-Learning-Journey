''' 2. Write a program to fill in a letter template given below with name and date.
letter =
Dear <|Name|>,
You are selected!
<|Date|>

'''

letter = '''Dear <|NAME|>,
Hare Krishna
Date: <|DATE|>'''

print(letter.replace("<|NAME|>", "Aman").replace("<|DATE|>", "20/06/2026"))