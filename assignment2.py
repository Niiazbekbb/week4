def computepay(hours, rate):
    if hours > 40:
        regular_hours_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        total = regular_hours_pay + overtime_pay
    else:
        total = hours * rate
    return total
try:
    hours = float(input("Enter the numbers of hours worked: "))
    rate = float(input("Enter the hourly rate: "))
    if hours < 0 or rate < 0:
        print("Error, please enter non-negative numbers.")
    else:
        salary = computepay(hours, rate)
        print("The total salary is:", salary)
except ValueError:
    print("Error, please enter numeric input.")
