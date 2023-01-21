import csv
import re

with open ('phonebook.csv', encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    

def correct_name(rows):
    for employee in rows:
        result = ' '.join(employee[0:3]).split(' ')[0:3] + employee[3:7]
        return result
        

def delete_duplicates(correct_name_list):
    without_dupli = []
    for comp in contacts_list:
        for employee in correct_name_list:
            if comp[0:2] == employee[0:2]:
                list_employee = comp
                comp = list_employee[0:2]
                for i in range(2, 7):
                    if list_employee[i] == '':
                        comp.append(employee[i])
                    else:
                        comp.append(list_employee[i])
        if comp not in without_dupli:
            without_dupli.append(comp)
    return without_dupli


def new_phone(rows, regular, new):
    phone = []
    pattern = re.compile(regular)
    phone = [[pattern.sub(new, string) for string in strings]for strings in rows]
    return phone


correct_name_list = correct_name(contacts_list)
without_dupli = delete_duplicates(correct_name_list)
regular = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})'
correct_list = new_phone(without_dupli, regular, r'+7(\2)\3-\4-\5')
regular_2 = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s]*[(доб.\s]*(\d+)[)]*'
correct_phonebook = new_phone(correct_list, regular_2, r'+7(\2)\3-\4-\5 доб.\6')


with open("correct_phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(correct_phonebook)