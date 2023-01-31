hours_worked = float(input("How many hours have you worked this week?"))
rate_of_pay = float(input("What is your rate of pay?"))

if hours_worked < 40:
    gross_pay = hours_worked * rate_of_pay
else:
    overtime = hours_worked - 40
    overtime_pay = overtime * (rate_of_pay * 1.5)
    gross_pay = 40 * rate_of_pay + overtime_pay

print(f"Your gross pay for the week is {gross_pay}")
