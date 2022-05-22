# Задание №2

import yaml

TEST = {
    "φ": ['hello world', 'привет мир', '֍ ֍ ֍ ֍ ֍'],
    "©§¥": 19,
    "¾½¼": {
        (1, 2): 'первый',
        5: 'пять',
        'восемь': '8'
    },
}

FILE_NAME = 'file.yaml'
print(TEST)


def save_yaml(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def load_yaml(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        f_to_dict = yaml.load(f, Loader=yaml.FullLoader)
    return f_to_dict


save_yaml(TEST, FILE_NAME)
result_load = load_yaml(FILE_NAME)
print(TEST)
print(result_load)

print(result_load == TEST)
