from database.process_file import ProcessFile
from core.process_data import ProcessDict, ProcessRange


def load_and_transform_data(path_file_data):
    raw_data = ProcessFile.read_csv_file(path_file_data)

    data = []
    for row in raw_data:
        ProcessDict.transform_value_to_range(row)
        data.append(row)

    return data


def main():
    path_file_data = 'data/data.txt'
    path_file_out_data = 'data/out_data.txt'
    number_records = 12
    fieldnames = ['Вид работы']

    data = load_and_transform_data(path_file_data)

    out_data = []
    for _ in range(number_records):
        random_data = ProcessDict.get_random_dict(data)
        out_inner_data = []
        for row in random_data:
            department = row['Отдел']
            range_value: range = row['Значение']
            random_num = ProcessRange.get_random_value_from_range(range_value)

            out_string = f'{department} ({random_num})'
            out_inner_data.append(out_string)

        result_string = (f'Помощь в выполнение рентгенографических исследований: {";".join(out_inner_data)}.'
                         f' Формулирование заключений совместно с врачом-рентгенологом.')
        out_data.append({'Вид работы': result_string})

    ProcessFile.write_csv_file(path_file_out_data, out_data, fieldnames)


if __name__ == '__main__':
    main()
