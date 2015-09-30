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
