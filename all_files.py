def all_files_(file, name_file):
    file_dict = {}
    name = name_file
    read_rows = file.readlines()  # Считываем файл в список
    count_rows = len(read_rows)  # Считаем количество строк в нем
    file_dict[count_rows] = f"{name}\n{str(count_rows)}\n{''.join(read_rows)}"
    return file_dict, count_rows


with open('1.txt', 'r', encoding='utf-8') as f:
    file1 = f
    name1 = '1.txt'
    file_dict1 = all_files_(file1, name1)  # Вызов фунукции


with open('2.txt', 'r', encoding='utf-8') as f2:
    name2 = '2.txt'
    file_dict2 = all_files_(f2, name2)


with open('3.txt', 'r', encoding='utf-8') as f3:
    name3 = '3.txt'
    file_dict3 = all_files_(f3, name3)


with open('4.txt', 'a', encoding='utf-8') as all_files:  # Открываем файл для записи
    all_file_list = [file_dict1[1], file_dict2[1], file_dict3[1]]
    all_file_list.sort()
    all_file_dict = file_dict1[0] | file_dict2[0] | file_dict3[0]
    for i in all_file_list:
        all_files.write(all_file_dict.get(i))
