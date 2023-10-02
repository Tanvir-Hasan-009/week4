try:
    def computepay(working_hours, wages_rate):
        if working_hours <= 40:
            pay = working_hours * wages_rate
        else:
            pay = (40 * wages_rate) + ((working_hours - 40) * 1.5 * wages_rate)
        return pay

    working_hours = float(input("Enter hours worked: "))
    wages_rate = float(input("Enter hourly rate: "))
    salary = computepay(working_hours, wages_rate)
    print("Salary: ",salary)
except ValueError:
    print("Error: Please enter numeric input.")
