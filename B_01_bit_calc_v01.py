# Generates Headings (eg: ---- Heading ----) 1 usage from dis import Instruction
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instruction go here.
- instruction 1
- instructions 2
- etc 
    ''')


# asks users for file type (integer / image / text / xxx)  1 usage
def get_filetype():

    while True:
        response = input("File_type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ["integer", "int"]:
            return "integer"

        # check for an image...
        elif response in ['image', 'p', 'img']:
            return "image"
        # check for a text...
        elif response in ['text', 't', 'txt']:
                return "text"

        # if the response is invalid output an error
        else:
            print("please enter a valid file type")



# Ask user for width and loop until they
# enter a number that is more than zero 3 usages
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


# calculates how many bits are needed to represent an integer
def image_calc():
  # get the image dimensions
  width = int_check("width: ", 1)
  height = int_check("height: ", 1)

  # calculate the number of pixels and multiply by 24 to get the number of bits
  num_pixels = width * height
  num_bits = num_pixels * 24

  # set up answer and return it
  answer = (f"Number of pixels:  {width} * {height} = {num_pixels }"
            f"\nNumber of bits: {num_pixels  } * 24 = {num_bits}")

  return answer


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
    answer = f"{integer} in binary is {binary}. we need {num_bits} bit to represent it."

    return answer

# calculates number of bits needed to represent text in ascii 1 usage
def calc_text_bits():

    # get text from user
    response = input("Enter some text: ")

    # calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # set up answer and return it
    answer = (f"{response} has {num_chars} characters. "
              f"\nwe need {num_chars} * 8 bits to represent it"
              f"\nwhich is {num_bits} bits")
    return answer


# Main routine goes here

# Display instructions if requested
want_instructions = input("please <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()
    if file_type == "xxx":
        break
    # if user chose 'i', ask if they want an image / integer
    if file_type == 'i':

        want_image = input("press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)



