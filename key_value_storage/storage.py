import os
import tempfile
import argparse
import json
from collections import OrderedDict

# каталог для хранения временных файлов
print(tempfile.gettempdir())
# абсолютный путь к временному файлу
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

#чтение данных из командной строки
parser = argparse.ArgumentParser(description='find_key')
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()
name = args.key
surname = args.value

try:
    with open(storage_path, "r") as file_name:
        dictionary = OrderedDict(json.load(file_name))
except:
    with open(storage_path, "w") as file_name:
        dictionary = OrderedDict()
        dictionary[name] = [surname]
        json.dump(dictionary, file_name)
        exit()

if (name is not None) and (surname is not None):
    if name in dictionary.keys():
        names = list()
        names = dictionary[name]
        names.append(surname)
        dictionary[name] = names
        with open(storage_path, "w") as file_name:
            json.dump(dictionary, file_name)
    else:
        dictionary[name] = [surname]
        with open(storage_path, "w") as file_name:
            json.dump(dictionary, file_name)

if (name is not None) and (surname is None):
    if name in dictionary.keys():
        print(', '.join(dictionary[name]))
    else:
        print(dictionary.get(name, None))


