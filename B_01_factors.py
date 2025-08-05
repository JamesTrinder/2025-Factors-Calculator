# Generates heading (eg ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''\nTo use this program simply enter an integer between
1 and 200. The program will show the factors of your
chosen integer.

It will also tell you if your chosen number...
- is a prime number (ie: it has two factors)
- is a perfect square

To exit the program, please type 'xxx'.\n

    ''')


# Ask user for an integer between 1 and 200
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

# Works out factors, returns sorted list
def factor(var_to_factor):
    var_to_factor = []

    while True:
        for item in range(1, 200):
            all_factor =

            remainder = to_factor % all_factor

            for item in range(0, 5):

                # generate a random number
                factors = num_check(1, 10)

                if factors not in var_to_factor:
                    var_to_factor.append(factors)

            if remainder == 0:
                print(f"{all_factor} is a factor of {to_factor} !")

            var_to_factor.sort()
            return

# Main routine goes here

statement_generator("Factor finder like a cool guy :0", "-")

# Display instructions if requested
want_instructions = input("Press <enter> to see the instructions "
                              "or any key to continue ")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    # ask user for a number to be factorized
    to_factor = num_check("\nEnter an integer (or xxx to quit): ")

    if to_factor == "xxx":
        break

    # get factors for integers that are 2 or more
    elif to_factor != 1:
        all_factors = factor(to_factor)

    # Set up a comment for unity
    else: all_factors = ""
    comment = "One is UNITY! It has only one factor. Itself :)"

    # comments for squares / primes

    # Prime numbers have only two factors
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"

    # check if the list has an odd number of factors
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    # Set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special"

    # output factors and comment
    print(factor)
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("Thank you for using the factors calculator")