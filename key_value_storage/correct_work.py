import argparse
import json
import os
import tempfile


def read_data_from_file(storage_path: str):
    """
    Метод для считывания данных из временного файла
    :param storage_path: str - путь к временному файлу
    """
    if not os.path.exists(storage_path):
        print("File is not found")
        return {}
    with open(storage_path, 'r') as f:
        read_data = f.read()
        if read_data:
            return json.loads(read_data)
        return {}

def write_data(storage_path: str, data: str) -> None:
    """
    метод записи данных в файл json
    :param storage_path: str - путь к временному файлу
    :param data: str - вносимые данные
    :return: None
    """
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))

def parse():
    """
    Метод для парсинга вводимых данных из консоли
    """
    parser = argparse.ArgumentParser(description='get_keys')
    parser.add_argument('--key')
    parser.add_argument('--val')
    return parser.parse_args()

def put_data_to_storage(storage_path, key, value):
    """
    метод добавления данныхв хранилище
    """
    data = read_data_from_file(storage_path)
    # каждый ключ будет хранить список значений
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(storage_path, data)

def get_data(storage_path, key):
    data = read_data_from_file(storage_path)
    return data.get(key, [])

def main(storage_path):
    args = parse()

    if args.key and args.val:
        put_data_to_storage(storage_path, args.key, args.val)
    elif args.key:
        print(*get_data(storage_path, args.key), sep=', ')
    else:
        print('The program is called with invalid parameters.')


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)