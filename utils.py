import random
import string
import csv
from student import users


def get_random_alphanumeric_string(letters_count, digits_count):
    sample_str = ''.join((random.choice(string.ascii_lowercase)
                          for i in range(letters_count)))
    sample_str += ''.join((random.choice(string.digits)
                           for i in range(digits_count)))

    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string


def removeChar(string: str):
    return "".join(filter(lambda s: s.isalpha(), list(string)))


def write_file(user_data: list, file_name: str):
    with open(file_name, 'w', newline='', encoding='utf_8_sig') as file:
        writer = csv.writer(file, delimiter=',',
                            escapechar='', quoting=csv.QUOTE_NONE)
        writer.writerow(users[0])
        writer.writerows(user_data)
