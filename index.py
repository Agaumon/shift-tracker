import os, time, decimal

os.system("clear")

employee_name = input("Employee: ")

total_hours = 0
# hours_worked = float(input("Hours: "))

hourly_wage = float(input("Hourly wage: "))

time.sleep(1)
os.system('clear')

def get_shift_hours():
    shifts_worked = int(input("How many shifts did you work? "))
    shifts = []
    for shift in range(shifts_worked):
        print(f'Shift {shift + 1}')
        hours_worked = int(input("Hours worked: "))
        shifts.append(hours_worked)
    total_hours = sum(shifts)
    if total_hours <= 40:
        regular_hours = total_hours
    else:
        regular_hours = 40
    return regular_hours, shifts, total_hours

time.sleep(1)
os.system("clear")

def calculate_pay(total_hours, regular_hours):
    # gross_pay = hours_worked * hourly_wage
    gross_pay = total_hours * hourly_wage
    gross_pay = round(gross_pay, 2)

    regular_pay = regular_hours * hourly_wage

    # if hours_worked > 40:
    #     overtime = hours_worked - 40
    #     overtime_pay = overtime * (hourly_wage * 1.5)
    #     gross_pay = gross_pay + overtime_pay

    if total_hours > 40:
        overtime = total_hours - 40
        overtime_pay = overtime * (hourly_wage * 1.5)
        gross_pay = gross_pay + overtime_pay
    else:
        overtime = 0

def display_summary():
    print("----- Weekly Summary -----")
    print()

    for number, hours in enumerate(shifts):
        print(f'Shift {number + 1}: {hours} hours')
    print()

    print(f'Total hours: {total_hours}')

    print(f'Regular hours: {regular_hours}')
    print(f'Overtime hours: {overtime}')
    print()

    # print(f'Employee: {employee_name}')
    # print(f'Hourly wage: ${hourly_wage:,.2f}')

    print(f'Regular pay: ${regular_pay:,.2f}')
    if overtime > 0:
        print(f'Overtime pay: ${overtime_pay:,.2f}')
    print(f'Gross pay: ${gross_pay:,.2f}')