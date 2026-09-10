# 1 - Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = {
    "namaste": "Hello",
    "dhanyabad": "Thank you",
    "kripya": "Please",
    "aap": "You",
    "mein": "I"
}
word = input("Enter a Hindi word to look up its English translation: ")
print(words.get(word, "Translation not found")) # print the English translation of the Hindi word, if not found print "Translation not found"