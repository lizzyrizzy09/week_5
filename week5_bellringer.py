# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
text='abracadabra'
print(text[5])
print(text[-2])
print(text[4])



# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
text="abcdefghijklmnopqrstuvwxyz"
substring=text.find("hij")
print(substring)
substring=text[7:10]
print(substring)

substring=text.find("m")
print(substring)
print(text[0:12:2])
print(text[::-1]) 


# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
text="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
substring=text.find("John F. Kennedy")
print(substring)
substring=text[83:98]
print(substring)




# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
text= "Python is fun. Fun is good. Good is subjective."
substring=text.find("subjective")
print(substring)
substring=text[36:-1]
print(substring)

sentence= "Python is fun. Fun is good. Good is subjective."
split_sentence= sentence.split()
print(split_sentence)
new_sentence="fun good subjective"
print(new_sentence)



# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
iteration="iteration" * 7
print(iteration)


# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.