#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0

#function to check the Pythagorean triplet condition is defined
def check_pyth(a, b, c):
	return (a**2) + (b**2) == (c**2)

SUM = 1000 #unique triplet where sum of a,b and c is 1000

#loop to find the unique pair
for i in range(1, SUM):
	for j in range(i+1, SUM):
		c = SUM - (i + j)
		if(check_pyth(i, j, c)): #calls the check_pyth function and runs the if condition
			if i + j + c == SUM: #checks whether i,j and c adds up to 1000
				solution = i * j * c #saving the product of i,j and c in solution
				break #the loop breaks once the condition is satisfied

# Check for the correct answer.
print("#5 : Pythagorean Triplet ::", "Correct." if solution == 31875000 else ("Wrong: " + str(solution)))
