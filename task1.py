import sys

def calcSalary():
    path, hours, costPerHour, prize = sys.argv
    salary = float(hours) * float(costPerHour) + float(prize)
    return salary

print(calcSalary())