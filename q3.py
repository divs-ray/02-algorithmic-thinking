#!/usr/bin/env python


solution = 0
number   = 175832868806
# First create a list of prime numbers to 300.
factors=[ ] #list of all factors  of 'number'
for i in range(1,300): #restricing the factor 'i' value between 1-300
    if number %i: continue #checks whether 'i' is a factor of 'number' or not
    else: factors.append(i)

factors.reverse() #reverses the list of all factors
factors.pop() #removes '1' from the list of all factors
#following block checks prime and non-prime condition for all factors of 'number'

nonprime=[ ] #list of non-prime factors
for j in factors: # for 'j' in the list of all factors
    l=[x for x in factors if x !=j] #list of
    for m in l:
        if j%m: continue #
        else:nonprime.append(j)
nprime=set(nonprime)
prime=[h for h in factors if h not in nprime] #list of all prime factors
solution=len(prime) #len counts the number of prime factors

#checks and prints the correct answer
if number == 175832868806:
  print("#3 : Count Prime Factors ::", "Correct." if solution == 6 else ("Wrong: " + str(solution)))
