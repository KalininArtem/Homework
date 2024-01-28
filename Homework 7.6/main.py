import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

example_contact = {
    'lastname': None,
    'firstname': None,
    'surname': None,
    'organization': None,
    'position': None,
    'phone': None,
    'email': None,
}
headers = contacts_list.pop(0)
new_list = [headers]


def get_format_phone_number(phone_number):
    pattern = re.compile(
        r'[\+]?[78][(\s]?[(]?(\d{3})[)\s-]?[\s]?(\d{3})[-]?(\d{2})[-]?(\d{2})[\s]?[(]?(доб.)?[\s]?(\d{4})?[)]?')

    format_string = r'+7(\1)\2-\3-\4 \5\6'

    formatted_number = pattern.sub(format_string, phone_number)

    return formatted_number
def get_full_name(list_of_data):
    return (" ".join(list_of_data[: 2])).strip()


for index, old_contact in enumerate(contacts_list):

    exist = False

    organization = old_contact[3]
    position = old_contact[4]
    phone = old_contact[5]
    if phone:
        phone = get_format_phone_number(phone)
    email = old_contact[6]

    full_name_contact = get_full_name(old_contact)

    split_full_name = full_name_contact.split(' ')
    if len(split_full_name) == 2:
        lastname, firstname = split_full_name
        surname = None
    elif len(split_full_name) == 3:
        lastname, firstname, surname = split_full_name
    else:
        print('error')
        break


    for new_contact in new_list:
        full_name_new_contact = get_full_name(new_contact)
        if full_name_new_contact.startswith(full_name_contact):
            exist = True

            if lastname:
                new_contact[0] = lastname
            if firstname:
                new_contact[1] = firstname
            if surname:
                new_contact[2] = surname
            if organization:
                new_contact[3] = organization
            if position:
                new_contact[4] = position
            if phone:
                new_contact[5] = phone
            if email:
                new_contact[6] = email
    if not exist:
        new_list.append(
            [
                lastname,
                firstname,
                surname,
                organization,
                position,
                phone,
                email

            ]
        )

with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_list)
