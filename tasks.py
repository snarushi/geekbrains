#TASK1

def inputlines():
    with open("lines.txt", 'a') as file_obj:
        while True:
            line = input('Enter the new line \n')
            if line != '':
                file_obj.write(line + '\n')
            else:
                break
    print("Exited edit mode")

#inputlines()

#TASK2
def count_words_and_lines():
    line_number = 0
    lines = []
    with open('countlines', 'r') as file_obj:
        for line in file_obj:
            line_number += 1
            lines.append((line_number, len(line.split())))
    print(f"Total {line_number} lines in the file")
    for el in lines:
        print(f"{el[0]} line contains {el[1]} words")

#count_words_and_lines()

#TASK3
def salaries():
    total_people = 0
    salary_total = 0
    print("Employees with less 20k salary are:")
    with open('salaries', 'r') as file_obj:
        for line in file_obj:
            total_people += 1
            line_obj = line.split()
            salary_total += float(line_obj[1])
            if float(line_obj[1]) < 20000:
                print(line_obj[0])
        print(f"Average salary is {salary_total / total_people}")

#salaries()

#TASK4
def numerals():
    dictionary = {"One": "Первый", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    with open('numbers', 'r') as file_obj:
        for line in file_obj:
            with open('rus_numbers.txt', 'a') as new_file_obj:
                for english in list(dictionary.keys()):
                    if line.count(english) > 0:
                        line = line.replace(english, dictionary[english])
                        new_file_obj.write(line)

numerals()

#TASK5
import random
def nsum():
    amount = int(input("Enter the amount of numbers \n"))
    maximum = int(input("Enter the maximum number \n"))
    with open('numbers.txt', 'w+') as file_obj:
        for _ in range(1, amount + 1):
            print(random.randint(0, maximum), file=file_obj, end=' ')
        file_obj.seek(0)
        nline = file_obj.readline()
        print(sum(map(int, nline.split())))

#nsum()

#TASK6
def lessons():
    lessons_dict = {}
    with open('lessons.txt', 'r') as file_obj:
        for line in file_obj:
            total_lesson_hours = 0
            lessons_line_list = line.split()
            lesson_title = lessons_line_list[0].replace(':', '')
            for el in lessons_line_list[1:]:
                temp = el.split('(')
                if temp[0] != '-':
                    total_lesson_hours += int(temp[0])
            lessons_dict[lesson_title] = total_lesson_hours
    print(lessons_dict)

#lessons()

# #TASK7
import json
def profits():
    data = [{}, {}]
    total_profits = 0
    profitable = 0
    with open('companies.txt', 'r') as file_obj:
        lines_list = [el.replace('\n', '') for el in file_obj.readlines()]
        for line in lines_list:
            temp_list = line.split()
            pnl = int(temp_list[2]) - int(temp_list[3])
            if pnl > 0:
                total_profits += pnl
                profitable += 1
            data[0][temp_list[0]] = pnl
    data[1]['average_profit'] = total_profits / profitable
    with open("result.json", "w") as write_f:
        json.dump(data, write_f)


#profits()