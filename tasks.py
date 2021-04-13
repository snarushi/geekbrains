#TASK 1

def divide(dividend, divider):
    print(f"Dividend is {dividend}, divider is {divider}")
    if(divider == 0):
        print(("No way!"))
    else:
        print(f"{dividend} / {divider} = {float(int(dividend) / int(divider))}")

#divide(30, 5)

#TASK 2
def credentials(name, surname, DOB, city, email, phone):
    print(f"{name.title()} {surname.title()} born {DOB} in {city}. Contacts: {email}, {phone}")

#credentials(name="Slava", surname="Narushi", DOB="1999", city="Saint-P", email="yyy@ya.ru", phone="7777777")

#TASK 3
def my_func(a, b, c):
    list = [a, b, c]
    list.sort()
    return list[-1] + list[-2]

#print(my_func(4, 1, 10))

#TASK 4
#First solution
def power(x, y):
    return x ** y

#Second solution
def powerloop(x, y):
    power = 1
    if y > 0:
        while y > 0:
            power = power * x
            y -= 1
        return power
    else:
        y = -y
        while y > 0:
            power = power * x
            y -= 1
        return 1 / power

#print(powerloop(3, -3))

#TASK 5
def sum():
    sum = 0
    while True:
        numbers = input("Enter the numbers... End up with 'q' to terminate program")
        if numbers[-1] == 'q':
            break
        numbers = numbers.split()
        for n in numbers:
            sum += int(n)
        print(sum)
    return sum

#TASK 6
def capital(word):
    return word.title()

def Capitals(string):
   result = ""
   words = string.split()
   for word in words:
       word = capital(word)
       result += word + " "
   return result

print(Capitals("wqdfqc fiehwo oiuewoi diuey87h2iu foi2eh"))