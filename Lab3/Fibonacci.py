# Fibonacci for 1000

# getting the recursive sequence
def fib(n):
  if n == 0 or n == 1
  return n

else:
  return fib(n-1) + fib(n-2)

# asking the user to input the number
fibnumber = int(raw_input("Please enter your number: "))
print "This is the number you entered: %d" % fibnumber

# displaying the fibonacci number
output = fib(fibnumber)
print "This is the corresponding fibonacci number: %d" % output

# displaying the length of the fibonacci number
length = len(str(output))
print "This is the length of your fibonacci number: %d" % length

# using for loop to print the fibonacci sequence up to the input number
for x in range (0, fibnumber):
  print (fib(x))

  # if the sequence has a number where it is made up of 4 numbers, print this
  if length >= 4:
    print "Your fibonacci is composed of 4 numbers!"

  # print this if the above is not valid
  else:
    print "Your number is not made up of 4 numbers!"
