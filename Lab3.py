# Palindrome

# asking for the input of a word
word = raw_input("Please enter your word: ")
rev_word = reversed(word) # reverse the input word

if list(word) = list(rev_word): # if the reversed word is the same as the word when not reversed
  print("This is a palindrome!") # then it's a palindrome
  
else: # if the above isn't true, then not a palindrome
  print("This is not a palindrome!")