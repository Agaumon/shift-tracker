import os, time, decimal

# Clear Display
def clear():
    time.sleep(.5)
    os.system('clear')

clear()

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
    return shifts

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
    worktime = {"regular": regular_hours, "ot": overtime, "total": total_hours}
    return worktime

def calculate_pay(worktime):
    # Calculate regular pay
    regular_pay = worktime["regular"] * hourly_wage

    # Calculate overtime pay
    overtime_pay = worktime["ot"] * (hourly_wage * 1.5)

    # Calculate gross pay
    gross_pay = (worktime["total"] * hourly_wage) + overtime_pay

    pay = {"regular": regular_pay, "otpay": overtime_pay, "gross": gross_pay}
    return pay

def display_summary(shifts, worktime, pay):
    clear()
    print("----- Weekly Summary -----")
    print()

    # Display shift number and hours for each shift
    for number, hours in enumerate(shifts):
        print(f'Shift {number + 1}: {hours} hours')
    print()

    # Display hours
    print(f'Total hours: {worktime["total"]}')

    print(f'Regular hours: {worktime["regular"]}')
    print(f'Overtime hours: {worktime["ot"]}')
    print()

    # Display pay
    print(f'Regular pay: ${pay["regular"]:,.2f}')

    if worktime["ot"] > 0:
        print(f'Overtime pay: ${pay["otpay"]:,.2f}')

    print(f'Gross pay: ${pay["gross"]:,.2f}')

# Call functions with appropriate parameters
shifts = get_shift()
worktime = get_hours(shifts)
pay = calculate_pay(worktime)
display_summary(shifts, worktime, pay)