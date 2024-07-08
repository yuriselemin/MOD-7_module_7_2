


# Домашнее задание по теме "Позиционирование в файле".



def custom_write(file_name, strings):
    f = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    for i, string in enumerate(strings):
        f.write(f'\n{string}')
        start_position = f.tell()
        strings_positions[(i + 1, start_position)] = string
    f.close()
    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


