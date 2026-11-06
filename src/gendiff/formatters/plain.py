def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff, parent=''):
    lines = []
    for node in diff:
        path = f'{parent}{node["key"]}'
        node_type = node['type']
        if node_type == 'nested':
            nested_lines = format_plain(node['children'], path + '.')
            lines.extend(nested_lines.split('\n'))
        elif node_type == 'changed':
            old = to_str(node['old_value'])
            new = to_str(node['new_value'])
            lines.append(
                f"Property '{path}' was updated. From {old} to {new}"
            )
        elif node_type == 'added':
            value = to_str(node['value'])
            lines.append(f"Property '{path}' was added with value: {value}")
        elif node_type == 'removed':
            lines.append(f"Property '{path}' was removed")
    return '\n'.join(lines)
