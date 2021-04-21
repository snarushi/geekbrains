#TASK1
def what_type():
    list = [1, 1.5, 'String', ['list', 'elements']]
    for el in list:
        print(type(el))


#what_type()
#TASK2
def reverse_list():
    list = []
    prompt = ""
    while prompt != "end":
        prompt = input("Enter new list item or type 'end' to finish").lower()
        if prompt != "end":
            list.append(prompt)
    index = 0
    while index < len(list) - 1:
        list[index] = [list[index], list[index + 1]]
        list.remove(list[index + 1])
        index += 1

    for el in list:
        if type(el) != type('str'):
            el.reverse()
        else:
            el = [el]

    print(list)


#reverse_list()

#TASK3
def months():
    calendar = dict(winter=(12, 1, 2), spring=(3, 4, 5), summer=(6, 7, 8), autumn=(9, 10, 11))
    month = int(input("Enter the month number"))
    for season, months in calendar.items():
        if months.count(month) == 1:
            print(f"You entered {season} month")


#months()

#TASK4
def split_string():
    words = input("Enter any string... \n").split()
    for word in enumerate(words):
        print(f"{word[0] + 1} - {word[1]}") if len(word[1]) < 10 else print(f"{word[0] + 1} - {word[1][:10]}")

#split_string()

#TASK5

def rate():
    values = [7, 5, 3, 3, 2]
    new_val = int(input("Enter the new value"))
    for el in values:
        if new_val == el:
            values.insert(values.index(el), new_val)
            break
        elif values.index(el) == len(values) - 1:
            values.append(new_val)
            break
    print(values)

#rate()
