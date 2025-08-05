for item in range(1, 200):
    num_lollies = 12
    num_students = item

while True:
    num_lollies = int(input("How many lollies? "))
    num_students = int(input("How many students? "))

    division = num_lollies / num_students
    per_student = num_lollies // num_students
    lollies_left = num_lollies % num_students

    print("Division: ", division)
    print("Lollies left per student: ", per_student)
    print("Lollies left: ", lollies_left)

    if lollies_left == 0:
        print(f"{num_students} is a factor of 12!")

    print(f"Each student gets {per_student} and we have {lollies_left} left over")