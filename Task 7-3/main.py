import os


def reading_files() -> dict:
    """ Считывает все .txt файлы из каталога 'sorted' и объединяет в форматированный словарь.

        Для корректной работы каталог 'sorted' должен находиться в текущем каталоге.

        Структура возвращаемого словаря:

        {'Название_файла_1': ['Строка 1 файла 1', 'Строка 2 файла 1', ...],
         'Название_файла_2': ['Строка 1 файла 2', 'Строка 2 файла 2', ...],
         ...}
    """
    combined_data = {}
    dir_sorted = os.path.join(os.getcwd(), 'sorted')
    txt_files_name = filter(lambda x: x.endswith('.txt'), os.listdir(dir_sorted))
    for file_name in txt_files_name:
        path = os.path.join(dir_sorted, file_name)
        with open(path, encoding='utf-8') as file:
            for line_file in file:
                if file_name in combined_data.keys():
                    combined_data[file_name] += [line_file]
                else:
                    combined_data[file_name] = [line_file]
    return combined_data


def creating_resul_file(combined_data: dict) -> str:
    """ Сортирует входящий форматированный словарь по возрастанию количества строк в значениях словаря,
        а затем записывает его в результирующий файл 'resul_file.txt'
        c дополнительной служебной информацией на 2-х строках:
        имя изначального файла и количество строк в нем.

        combined_data - входящий форматированный словарь. Может быть сформирован функцией 'reading_files()'

        Возвращает сообщение о формировании файла 'resul_file.txt'
    """
    result_data = dict(sorted(combined_data.items(), key=lambda x: x[1], reverse=True))
    with open('resul_file.txt', 'w', encoding='utf-8') as resul_file:
        for file_name in result_data:
            resul_file.write(f'{file_name}\n')
            resul_file.write(f'{str(len(result_data[file_name]))}\n')
            for line in result_data[file_name]:
                resul_file.write(line)
                if '\n' not in line:
                    resul_file.write('\n')  # Для одинакового формата вывода файлов
            resul_file.write('\n')        # Добавил перенос строки между выводом разных изначальных файлов
    return 'Объединенный и отсортированный файл "resul_file.txt" сформирован в текущем каталоге!'


print(creating_resul_file(reading_files()))
