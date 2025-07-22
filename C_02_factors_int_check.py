# Ask a user for width and loop until they
# give an answer that is between 1 and 200
def num_check(question):

    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            #ask the user for a number
            response = int(response)

            #check the number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# Main Routine Goes Here
while True:
    to_factor = num_check("To factor: ")
    print("You chose factor", to_factor)

    if to_factor == "xxx":
        break