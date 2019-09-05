n = int(input("Enter the length of the sequence: ")) # Do not change this line
# problem description
# generate the first n numbers in the following sequence 1,2,3,6,11,20,37,....

# the pattern is adding the last three numbers to the current number in the sequence
# we establish the first three numbers 1, 2 and 3 which will also work as our last three numbers

num1 = 1
num2 = 2
num3 = 3
for i in range(1,n+1):
    if 1 <= i <= 3:                         #to print the first 3 numbers
        print(i)
    else:
        sequence_num = num1 + num2 +num3    # the sequence number is the last three numbers addeed together
        num1 = num2                         # then we update all the numbers by moving them up to their next place in line
        num2 = num3
        num3 = sequence_num                 # such that the last number becomes the last sum of the numbers (sequence_num)
        print(sequence_num)


