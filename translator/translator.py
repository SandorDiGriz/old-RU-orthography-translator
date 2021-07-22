import re
import os
from os import path
import excep_dict


def main():
    dict = excep_dict.get_dictionary()
    for current_file in get_files():
        if current_file.split('.')[-1] == 'txt':
            output_file_name = current_file.split('.')[0] + '_translated.txt'
            input_file = open(current_file, encoding="utf-8")
            output_file = open('translated_files' + '\\' + output_file_name, 'w', encoding="utf-8")                                            												                               
            result = []
            input_line = str										                                
            for line in input_file:
                input_line = line
                line = replace(line)
                line = check_for_exception(dict, line, tokenisation(input_line))
                result.append(line)
                output_file.write(line)
            input_file.close()
            output_file.close()
    return ''.join(result)


def tokenisation(line_of_tokens):
    lst_tokenlines = []
    lst_tokens = []
    lst_tokenlines.append(re.split(r'[^A-Z-a-z-а-я-А-Я-Ѣ-ѣ-І-і-Ѳ-ѳ-Ѵ-ѵ]', line_of_tokens.strip()))
    for line in lst_tokenlines:
        for word in line:
            lst_tokens.append(word)
            lst_tokens = [x for x in lst_tokens if x != '']
    return lst_tokens


def check_for_exception (dict, output_string, tokens):
    dictionary = dict
    for line in dictionary:
        for word in tokens:
            if word in line:
                output_string = execute_exceptions(output_string, word)
    return output_string


def execute_exceptions(new_output_string, word):
    new_output_string = re.sub(replace(word), word, new_output_string)
    return new_output_string


def replace(data):
    import rules_dict
    rules = rules_dict.get_rules()
    for key, val in rules.items():
        data = re.sub(key, val, data)
    return data


def get_files():
    print("please, type the path to your folder")
    path = input()
    os.chdir(path)
    list_of_files = os.listdir(path)
    if not os.path.exists(path + r'/translated_files'):
        os.mkdir('translated_files')
    return list_of_files


main()
