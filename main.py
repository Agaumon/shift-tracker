import os, time, decimal

# Clear Display
def clear():
    time.sleep(1)
    os.system('clear')

# Ask name of employee and hourly wage
employee_name = input("Employee: ")
hourly_wage = float(input("Hourly wage: "))

clear()

def get_shift():
    # Create empty list
    shifts = []
    # Ask for number of shifts worked
    shifts_worked = int(input("How many shifts did you work? "))

    # Print shifts worked along with hours worked
    for shift in range(shifts_worked):
        print(f'Shift {shift + 1}')
        hours_worked = int(input("Hours worked: "))
        shifts.append(hours_worked)
    return shifts, hours_worked

def get_hours(shifts):
    # Calculate total hours worked
    total_hours = sum(shifts)

    # Calculate overtime hours
    if total_hours > 40:
        overtime = total_hours - 40
    else:
        overtime = 0

    # Calculate regular hours worked
    if total_hours <= 40:
        regular_hours = total_hours
    else:
        regular_hours = 40
    return regular_hours, total_hours, overtime

clear()

def calculate_pay(regular_hours, total_hours, overtime):
    # Calculate regular pay
    regular_pay = regular_hours * hourly_wage

    # Calculate overtime pay
    overtime_pay = overtime * (hourly_wage * 1.5)

    # Calculate gross pay
    gross_pay = (total_hours * hourly_wage) + overtime_pay

def display_summary(shifts, total_hours, regular_hours, overtime, regular_pay, overtime_pay, gross_pay):
    print("----- Weekly Summary -----")
    print()

    # Display shift number and hours for each shift
    for number, hours in enumerate(shifts):
        print(f'Shift {number + 1}: {hours} hours')
    print()

    # Display hours
    print(f'Total hours: {total_hours}')

    print(f'Regular hours: {regular_hours}')
    print(f'Overtime hours: {overtime}')
    print()

    # Display pay
    print(f'Regular pay: ${regular_pay:,.2f}')
    if overtime > 0:
        print(f'Overtime pay: ${overtime_pay:,.2f}')
    print(f'Gross pay: ${gross_pay:,.2f}')

get_shift(shifts)
get_hours()
calculate_pay()
display_summary()