def to_str(value, depth):
    if isinstance(value, dict):
        lines = ['{']
        for key, val in value.items():
            lines.append(f"{' ' * (depth * 4 + 4)}{key}: {to_str(val, depth + 1)}")
        lines.append(' ' * (depth * 4) + '}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)


def format_stylish(diff, depth=1):
    lines = ['{']
    line_indent = ' ' * (depth * 4 - 2)
    close_indent = ' ' * (depth * 4 - 4)
    for node in diff:
        key = node['key']
        node_type = node['type']
        if node_type == 'changed':
            lines.append(f'{line_indent}- {key}: {to_str(node["old_value"], depth)}')
            lines.append(f'{line_indent}+ {key}: {to_str(node["new_value"], depth)}')
        elif node_type == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(f'{line_indent}  {key}: {children}')
        else:
            sign = {'added': '+', 'removed': '-'}.get(node_type, ' ')
            lines.append(f'{line_indent}{sign} {key}: {to_str(node["value"], depth)}')
    lines.append(close_indent + '}')
    return '\n'.join(lines)
