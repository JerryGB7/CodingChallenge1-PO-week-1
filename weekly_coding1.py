# Problem Statement
# Write a program that accepts sets of three numbers and prints the second-maximum number among the three.

# Input

	
# First line contains the number of triples, N.
	
# The next N lines which follow each have three space separated integers.

# Output
# For each of the N triples, output one new line which contains the second-maximum integer among the three.

def second_max(numlist = list):
    maxnum = max(numlist)
    minnum = min(numlist)
    numlist.remove(maxnum)
    numlist.remove(minnum)
    return numlist[0]

output_nums = []
n = int(input())
for i in range(0, n):
    userlist = list(int(num) for num in input().strip().split())[:n]
    output_nums.append(second_max(userlist))

for i in output_nums:
    print(i)