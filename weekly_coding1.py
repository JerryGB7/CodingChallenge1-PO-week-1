# Problem Statement
# Write a program that accepts sets of three numbers and prints the second-maximum number among the three.

# Input

	
# First line contains the number of triples, N.
	
# The next N lines which follow each have three space separated integers.

# Output
# For each of the N triples, output one new line which contains the second-maximum integer among the three.

def second_max(num1 = int, num2 = int, num3 = int):
    numlist = [num1, num2, num3]
    maxnum = max(numlist)
    minnum = min(numlist)
    numlist.remove(maxnum)
    numlist.remove(minnum)
    return numlist[0]

#print(second_max(100, 999, 500))