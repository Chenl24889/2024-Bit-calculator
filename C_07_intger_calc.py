# Ask user for width and loop until they
# enter a number that is more than zero 1 usages
def int_check(question, low):
    error = f"please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            #check that the number is more than zero
            if response >= low:
               return response
            else:
                print(error)

        except ValueError:
            print(error)


# calculates how many bits are needed to represent an integer 1 usage
def integer_calc():
    # Ask rhe user to enter an integer (more than / equal to 0)
    integer = int_check("Integer: ", 0)

    # convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)

    # remove the leading '0b' from the rew binary conversion
    binary = raw_binary[2:]
    num_bits =len(binary)

    # set up answer and return it
    answer = f"{integer} in binary is {binary}. we need {num_bits} to represent it."

    return answer
# Main routine goes here
integer_ans = integer_calc()
print(integer_calc)