# Palindrome

# getting the input for the word
word = raw_input("Please enter your word: ")

# reverse the input word
rev_word = reversed(word)

# if the word and the word reversed is the same then print they are palindromes
if list(word) == list(rev_word):
  print "This is a palindrome!"

# if the words are not palindromes then print this
else:
  print "This is not a palindrome!"