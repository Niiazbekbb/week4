def calculate_grade(score):
    if 0 <= score <= 100:
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    else:
        return None

while True:
    try:
        score_input = input("Enter Score: ")
        score = int(score_input)
        grade = calculate_grade(score)
        if grade is not None:
            print("Grade is", grade)
        else:
            print("Error, please enter a numeric input between 0 and 100")
    except ValueError:
        print("Error, please enter a numeric input between 0 and 100")
