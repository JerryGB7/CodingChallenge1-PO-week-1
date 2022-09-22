# Problem statement
# Given an alphanumeric string made up of digits and lower case Latin characters only, find the sum of all the digit characters in the string.

# Input

# The first line of the input contains an integer T denoting the number of test cases. Then T test cases follow.	
# Each test case is described with a single line containing a string S, the alphanumeric string.

# Output
	
# For each test case, output a single line containing the sum of all the digit characters in that string.
# Constraints	
# 1 ≤ T ≤ 1000
# 1 ≤ |S| ≤ 1000, where |S| is the length of the string S.

def alphanumeric_string(userinput = str):
    sum_of_num = 0
    for i in userinput:
        if i.isdigit():
            sum_of_num += int(i)

    return sum_of_num

#print(alphanumeric_string("ab12315da"))