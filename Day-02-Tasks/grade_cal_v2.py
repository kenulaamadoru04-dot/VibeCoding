def get_marks():
    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))
    return mark1, mark2, mark3


def calculate_average(mark1, mark2, mark3):
    return (mark1 + mark2 + mark3) / 3


def get_grade(average):
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "Fail"


def display_result(name, average, grade):
    print("------------------------------")
    print(f"Name :{name}")
    print(f"Average: {round(average, 2)}")
    print("Grade  : {grade}")
    print("------------------------------")


def main():
    while True:
        name = input("Enter student's name (or type Exit to quit): ")

        if name.lower() == "exit":
            print("Program ended.")
            break

        mark1, mark2, mark3 = get_marks()
        average = calculate_average(mark1, mark2, mark3)
        grade = get_grade(average)

        display_result(name, average, grade)


# Run the program
main()
