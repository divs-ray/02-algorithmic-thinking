#!/usr/bin/env python

solution = 0 #if not initialized to 0 then if the code fails to compute then this might return garbage value
max_fib  = 1e9 # max_fib holds the upper limit(1 billion in this case) of the integer 'i'

a, b = 1, 1 # integers 'a' and 'b' are assigned to value 1

while a < max_fib: # the condition to be evaluated;
#now the 'a'thats is < max_fib enters into the loop

    if a % 17 == 0: #if condition for checking whether 'a' is divisible by 17 or not
    #now the 'a' that returns value zero when divided by 17 moves on to the next execution
        solution += a #sum of Fibonacci numbers those are divisible by 17
                      #starts with 'a' as the Fibonacci number
    a, b = b, a+b #loop creating Fibonacci sequence
    #now this tuple (b,a+b) becomes new (a,b) for the next iteration
    #illustration -> (a,b)=(1,1);(b,a+b)=(1,2) now new (a,b) = (1,2)
    #'a+b' is executed first,before the value is assigned to b

# #checks and prints the correct answer
if max_fib == 1e9:
  print("#2 : Fibonacci ::", "Correct." if solution == 15129388 else ("Wrong: " + str(solution)))
