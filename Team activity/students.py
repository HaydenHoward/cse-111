import csv
from lib2to3.pgen2.token import NAME

def main():
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    student_dict = read_dict("students.csv", I_NUMBER_INDEX)
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    i_number = i_number.replace("-","")
    
    if not i_number.isdigit():
        print("Invalid character in i number")
    else:
        if len(i_number) > 9:
            print("i number is too long")
        elif len(i_number) < 9:
            print("i number is too short")
        else:
            if i_number in student_dict:
                value = student_dict[i_number]
                name = value[NAME_INDEX]
                print(name)
            else:
                print("No such student")

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary

if __name__ == "__main__":
    main()