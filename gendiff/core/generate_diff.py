from gendiff.core.diff_builder import build_diff
from gendiff.core.parser import parse
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish

FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json,
}


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    diff = build_diff(data1, data2)
    if format_name not in FORMATTERS:
        raise ValueError(f'Unsupported format name: {format_name}')
    return FORMATTERS[format_name](diff)
