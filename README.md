# Employee Shift Tracker

A Python command-line application that records hours worked across multiple shifts and calculates weekly work-hour totals and estimated gross pay. The project focuses on using functions and data structures to process work-hour information and present a summary.

## Features

- **Shift entry:** Enter the number of shifts worked and the hours for each shift.
- **Weekly hour totals:** Calculate total hours across all recorded shifts.
- **Regular hours:** Separate regular hours from hours worked beyond the 40-hour threshold.
- **Overtime tracking:** Calculate overtime hours using a 40-hour weekly threshold.
- **Pay summary:** Display regular pay, overtime pay, and estimated gross pay based on an hourly wage.
- **Formatted output:** Present the results in a readable weekly summary.

## Technologies

- Python 3
- Functions
- Lists and dictionaries
- Arithmetic operations
- Conditional logic
- Formatted strings

## Getting Started

### Prerequisites

- Python 3 installed on your system.

### Installation

Clone the repository:

```bash
git clone https://github.com/Agaumon/shift-tracker.git
cd shift-tracker
```

### Run the application

The repository includes `main.py` and `index.py`. To run the refactored version:

```bash
python main.py
```

You may need to use `python3 main.py` depending on your system.

## How It Works

The application collects an hourly wage and shift-hour entries from the user. It processes the entries to calculate total hours, regular hours, and overtime hours, then generates a weekly summary of estimated earnings.

## Important Note

This project is an educational calculator and is not intended for official payroll or wage compliance calculations. Verify the overtime-pay calculation before relying on the displayed gross-pay total.

## Future Improvements

- Correct and test overtime-pay calculations.
- Validate hourly wages and shift-hour inputs.
- Support fractional hours and different overtime rules.
- Add weekly history and persistent storage.
- Separate calculation logic from user-interface code.
- Add automated tests for pay calculations.

## Learning Objectives

This project provided practice with Python functions, lists, dictionaries, arithmetic, conditional logic, and transforming user input into a structured summary.

## Author

[Agaumon](https://github.com/Agaumon)
