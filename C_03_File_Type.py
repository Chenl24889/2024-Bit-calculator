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



# Main routine goes here
while True:
    file_type = get_filetype()

    # if user chose 'i', ask if they want an image / integer
    if file_type == 'i':

        want_image = input("press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You chose {file_type}")

    if file_type == "xxx":
        break

