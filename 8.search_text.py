"""search text from text file"""
user_input = input("Enter String: ")


def searchtext(input_string):
    """function for search a given string"""
    with open("myfile.txt", "r", encoding='utf-8') as text_file:   # opening a text file
        flag = 0                                # setting flag and line_no to 0
        line_no = 0
        for line in text_file:                  # Loop through the file line by line
            line_no += 1
            if input_string in line:             # checking string is present in line or not
                flag = 1
                break
        if flag == 0:                            # checking condition for string found or not
            print('String', input_string, 'Not Found')
        else:
            print('String', input_string, 'Found In Line number: ', line_no)


searchtext(user_input)
