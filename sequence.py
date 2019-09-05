n = int(input("Enter the length of the sequence: ")) # Do not change this line
# problem description
# generate the first n numbers in the following sequence 1,2,3,6,11,20,37,....

# the pattern is adding the last three numbers to the current number in the sequence
# we establish the first three numbers 1, 2 and 3 which will also work as our last three numbers

num1 = 1
num2 = 2
num3 = 3
for i in range(1,n+1):

