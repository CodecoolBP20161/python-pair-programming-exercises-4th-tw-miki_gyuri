import csv
import sys
from person import Person


def open_csv(file_name):
    with open(file_name, 'r') as phone_number:
        names_n_numbers = [line.split(",") for line in names_n_numbers.readlines()]
        numbers = []
        numbers = numbers.digits
        for element in names_n_numbers:
            for i in element[1]:

        # get phone numbers from list elements
        # remove every non-digit characters
    return names_n_numbers


def get_csv_file_name(argv_list):
    to_return = argv_list[1]  # might need to tell that it's a string
    return to_return


def format_output(person):
    # implent this function
    pass  # delete this


def get_person_by_phone_number(person_list, user_input_phone_number):
    for element in person_list:
        if user_input_phone_number == element[1]:
            return element[0]


def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)

    print(format_output(match_person))

if __name__ == '__main__':
    main()
