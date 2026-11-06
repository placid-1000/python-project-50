from gendiff.parser import parse


def stringify(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)


def generate_diff(file_path1, file_path2):
    data1 = parse(file_path1)
    data2 = parse(file_path2)

    keys = sorted(data1.keys() | data2.keys())

    lines = ['{']
    for key in keys:
        in_first = key in data1
        in_second = key in data2

        if not in_second:
            lines.append(f'  - {key}: {stringify(data1[key])}')
        elif not in_first:
            lines.append(f'  + {key}: {stringify(data2[key])}')
        elif data1[key] != data2[key]:
            lines.append(f'  - {key}: {stringify(data1[key])}')
            lines.append(f'  + {key}: {stringify(data2[key])}')
        else:
            lines.append(f'    {key}: {stringify(data1[key])}')

    lines.append('}')
    return '\n'.join(lines)
