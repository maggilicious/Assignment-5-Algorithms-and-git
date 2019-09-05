
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
                                            
max_int = 0                                 # assign a max input
                                            
while num_int > 0:                          # run while the input is not negative
    if max_int < num_int:                   # check if input is larger than max
        max_int = num_int                   # if input is larger than max int is input
    num_int = int(input("Input a number: "))# prompt for new input
                                            
print("The maximum is", max_int)    # Do not change this line
