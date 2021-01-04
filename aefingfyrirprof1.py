def get_student():
    name, grade_1, grade_2, grade_3 = None, None, None, None        

    name = input("Student name: ")
    grade_1 = float(input("Input grade number 1: "))
    grade_2 = float(input("Input grade number 2: "))
    grade_3 = float(input("Input grade number 3: "))

    average = (grade_1 + grade_2 + grade_3) / 3

    return name, grade_1, grade_2, grade_3, average

def add_grades(student_dict, name, grade_1, grade_2, grade_3, average):
    if name not in student_dict:
        student_dict[name] = grade_1, grade_2, grade_3, average

def print_student_list(student_dict):
        sorted_list = sorted(student_dict)
        current_value = 0
        max_value = 0
        print("Student list:")
        for name in sorted_list:
            current_value = (student_dict[name][3])
            if current_value > max_value:
                    max_value = current_value
                    current_student = name
            
            print("{}: [{}, {}, {}]".format(name, student_dict[name][0], student_dict[name][1], student_dict[name][2]))
        print("Student with highest average grade:\n{} has an average grade of {:.2f}".format(current_student, max_value))

def main():
    student_dict = {}
    name = ''

    if name is not None:
        for i in range(0,4):
            name, grade_1, grade_2, grade_3, average = get_student()
            add_grades(student_dict, name, grade_1, grade_2, grade_3, average)
        print_student_list(student_dict)

main()
