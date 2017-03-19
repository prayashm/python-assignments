import re

# Take the paragraph as input
print("Enter paragraph:\n")
paragraph = input()
words = re.findall(r"[\w']+", paragraph)

# Count of words
word_count = len(words)

# Count of letters/characters
char_count = len(paragraph)

# Count of unique words (case insensitive)
lowercase_words = [word.lower() for word in words]
unique_word_count = len(set(lowercase_words))

# Words which begin with Uppercase
uppercase_word_count = sum([1 for word in words if word[0].isupper()])

# Count of punctuations
punctuations_count = len(re.findall(r"[^\w'\s]", paragraph))

# Count of words that are numbers
numbers_count = len(re.findall(r"[\d]+", paragraph))

print("\nText has")
print("{} Words".format(word_count))
print("{} Characters".format(char_count))
print("{} Unique Words (case-insensitive)".format(unique_word_count))
print("{} Words starting with uppercase".format(uppercase_word_count))
print("{} Punctuations".format(punctuations_count))
print("{} Numbers".format(numbers_count))
