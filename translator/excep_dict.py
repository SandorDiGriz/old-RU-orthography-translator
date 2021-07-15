def get_dictionary():
    lst_dict = []
    with open (r'dictionary.txt', encoding='utf-8') as file:
        for line in file:
            lst_dict.append(line.rstrip())
    return lst_dict
