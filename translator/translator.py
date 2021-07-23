'''The main file of old-orthography translator project

Programm gets the path to the folder with files in pre-revolutionary Russian orthography
and creates there a new folder filled with their translated copies.
'''

import re
import os
from os import path
import excep_dict


def tokenization(line_of_tokens):
    '''Performs tokenization of line from original file'''
    lst_tokenlines = []
    lst_tokens = []
    # Separating tokens by all non-literal symbols
    lst_tokenlines.append(re.split(r'[^A-Z-a-z-а-я-А-Я-Ѣ-ѣ-І-і-Ѳ-ѳ-Ѵ-ѵ]', line_of_tokens.strip()))
    # Creating flat list
    for line in lst_tokenlines:
        for word in line:
            lst_tokens.append(word)
            # Eliminating blanks
            lst_tokens = [x for x in lst_tokens if x != '']
    return lst_tokens


def check_for_exception (dict, output_string, tokens):
    '''Checks if there any exception, comparing dictionary content with tokenized line

    Args:
        dict (list): exception dictionary
        output_string (str): current line in 'r' file
        tokens (list): list of line's tokens

    Returns:
        checked output string

    '''
    dictionary = dict
    # Checking for exceptions
    for line in dictionary:
        for word in tokens:
            if word in line:
                output_string = execute_exceptions(output_string, word)
    return output_string


def execute_exceptions(new_output_string, word):
    '''Removes the found exception with the word from dictionary'''
    new_output_string = re.sub(replace(word), word, new_output_string)
    return new_output_string


def replace(data):
    '''Applies regular expressions to a string '''
    import rules_dict
    # Loading REGEX
    rules = rules_dict.get_rules()
    # Processing changes
    for key, val in rules.items():
        data = re.sub(key, val, data)
    return data


def get_files():
    '''Finds wanted folder'''
    print("please, type the path to your folder")
    path = input()
    # Changing directory due to user's path
    os.chdir(path)
    # Getting names of files
    list_of_files = os.listdir(path)
    # Creating a new folder to translated files
    if not os.path.exists(path + r'/translated_files'):
        os.mkdir('translated_files')
    return list_of_files


def main():
    '''Translator core function

    Receives dictionary from 'excep_dict' function, then reads all files in given path
    by line, changes that line due to REGEX in 'replace' function, compares tokens from
    'tokenization' function with the dictionary content, corrects if it is needed and
    wrights derived lines in a new folder.
    '''
    dict = excep_dict.get_dictionary()
    for current_file in get_files():
        # Checking file extension
        if current_file.split('.')[-1] == 'txt':
            # Assignment of output name
            output_file_name = current_file.split('.')[0] + '_translated.txt'
            input_file = open(current_file, encoding="utf-8")
            # Creating translated copy of the file in generated folder
            output_file = open('translated_files' + '\\' + output_file_name, 'w', encoding="utf-8")                                            												                               
            result = []
            # Line for tokenization
            input_line = str										                                
            for line in input_file:
                input_line = line
                # REGEX implementation 
                line = replace(line)
                # Checking for possible matches with exception dictionary
                line = check_for_exception(dict, line, tokenization(input_line))
                result.append(line)
                output_file.write(line)
            input_file.close()
            output_file.close()
    return ''.join(result)


main()
