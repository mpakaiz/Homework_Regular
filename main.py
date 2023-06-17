import re

import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

new_contacts_list = []


def fix_phones():
    pattern = r"(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})((\s?)\(?(доб.)\s?(\d+)\)?)?"
    pattern_phone = re.compile(pattern)
    sub_pattern = r"+7(\2)\3-\4-\5 \8\9"
    for i in contacts_list:
        i[5] = pattern_phone.sub(sub_pattern, i[5])
    return


def move_names():
    pattern_name = r'([А-Я])'
    sub_name = r' \1'
    for i in contacts_list[1:]:
        full_name = i[0] + i[1] + i[2]
        if len((re.sub(pattern_name, sub_name, full_name).split())) == 3:
            i[0] = re.sub(pattern_name, sub_name, full_name).split()[0]
            i[1] = re.sub(pattern_name, sub_name, full_name).split()[1]
            i[2] = re.sub(pattern_name, sub_name, full_name).split()[2]
        elif len((re.sub(pattern_name, sub_name, full_name).split())) == 2:
            i[0] = re.sub(pattern_name, sub_name, full_name).split()[0]
            i[1] = re.sub(pattern_name, sub_name, full_name).split()[1]
            i[2] = ''
        elif len((re.sub(pattern_name, sub_name, full_name).split())) == 1:
            i[0] = re.sub(pattern_name, sub_name, full_name).split()[0]
            i[1] = ''
            i[2] = ''
    return


def merge_contacts_data():

    for i in contacts_list[1:]:
        l_f_name = i[0] + i[1]
        for j in contacts_list:
            new_l_f_name = j[0] + j[1]
            if l_f_name == new_l_f_name:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]
    for a in contacts_list:

        if a[:7] not in new_contacts_list:
            new_contacts_list.append(a)
    return new_contacts_list


if __name__ == "__main__":
    fix_phones()
    move_names()
    merge_contacts_data()
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)
