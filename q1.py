#!/usr/bin/env python


solution = 0 #if not initialized to 0 then if the code fails to compute then this might return garbage value
multiple = 0 #0 is assigned to the 'multiple' variable
             #'multiple' variable holds the value of the 'nth' positive integer
             #in the list of integers representing the multiples such as 1st, 2nd
             #3rd, 4th...integers

max_multiple = 100000 # 100000 is assigned as the upper limit of the integer 'i'
i=1 # integer i is assigned to value 1

while i < max_multiple: # the condition to be evaluated;
#the while loop executes the condition when 'i' is less than max_multiple(100000 in this case)

#follwing is the if condition for checking divisibility of the integer 'i'
#now the 'i' thats is < max_multiple enters into the loop
#this execution block will continuein in loop until it satisfies the if condition
    if (i % 4 == 0) and (i % 13 == 0) and (i % 14 == 0) and (i % 26 == 0) and (i % 50 == 0):
    # checking divisibility condition
    # 'and' is used after each condition to compute all conditions at once
        multiple += 1 #increment 'multiple' variable by 1

        if multiple == 9:
            solution = i #when this 'if' condition is satisfied 'solution' takes the value 'i'
            break #breaks the while loop once multiple == 9
    i += 1 # increment 'i' variable by 1; goes back to the while condition check
    
# checks and prints the correct answer
if multiple == 9:
  print("#1 : 9th Multiple ::", "Correct." if solution == 81900 else ("Wrong: " + str(solution)))
