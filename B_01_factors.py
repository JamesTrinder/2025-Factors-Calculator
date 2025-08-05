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


# Gets factors, returns a sorted list
def get_factors(factors):
    # x**(0.5) is the square root of x

    # We want to loop until we get to the square root of to_factor
    # stop is the square root of the factor.
    # Basically instead of going from one to the number,
    # we go from 1 to 'stop' (which is the square root
    # of the number we are trying to factorise)

    stop = int(factors ** 0.5)

    factors_list = []

    for item in range(1, stop + 1):

        # if modulo is zero, then the number is a factor
        if factors % item == 0:

            # find second factor by dividing 'to factor' by the first factor
            factor_2 = int(factors / item)

            # Add first factor to list
            factors_list.append(item)

            # check second factor is not in list and add it
            if factor_2 not in factors_list:
                factors_list.append(factor_2)

    # output
    factors_list.sort()
    return factors_list

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
        all_factors = get_factors(to_factor)

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
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("Thank you for using the factors calculator")