
import csv

def main():
    students_dict = read_file("pupils.csv")
    # display_dictionary(students_dict)
    number_str = prompt_i_number("Please enter an I-Number (xx-xxx-xxxx):")
    search_student_by_i_number(number_str, students_dict)

def read_file(filename: str):
    try:
        with open(filename) as file:
            # initialize reader, students_dict
            reader = csv.reader(file)
            students_dict = dict()

            # loop through file
            next(reader) # skip the first line
            for line in reader:

                # read the other lines of the file into the dictionary
                students_dict[line[0]] = line[1]
            
            return students_dict
    
    except OSError as msg: print(msg)

def display_dictionary(dictionary: dict):
    print("student id  name")
    print("-----------+-------------------")
    for item in dictionary:
        print(f"{item}  ", dictionary[item])

def prompt_i_number(prompt: str):

    while True:
        # prompt
        number_str = input(prompt + " ")

        # remove any '-' characters
        number_str = number_str.replace('-', '')

        # handle undesired input
        if not number_str.isnumeric():
            print("\nInvalid I-Number. (Invalid alphabetic input)\n")
            continue
        elif len(number_str) > 9:
            print("\nInvalid I-Number. (Too many digits)\n")
            continue
        elif len(number_str) < 9:
            print("\nInvalid I-Number. (Not enough digits)\n")
            continue
        
        # else
        break

    # else
    return number_str

def search_student_by_i_number(i_number: str, students: dict):
    try: print(students[i_number])
    except KeyError as msg: print("No such student")
    


""" run program """
if __name__ == "__main__": main()
