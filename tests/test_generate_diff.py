import json
from pathlib import Path

from gendiff import generate_diff

TEST_DATA_DIR = Path(__file__).parent / 'test_data'


def test_generate_diff_flat_json():
    path1 = TEST_DATA_DIR / 'file1.json'
    path2 = TEST_DATA_DIR / 'file2.json'
    expected = (TEST_DATA_DIR / 'expected_flat_diff.txt').read_text()
    assert generate_diff(str(path1), str(path2)) == expected.rstrip('\n')


def test_generate_diff_same_files():
    path = TEST_DATA_DIR / 'file1.json'
    actual = generate_diff(str(path), str(path))
    assert '- ' not in actual
    assert '+ ' not in actual

def test_main(capsys, monkeypatch):
    path1 = TEST_DATA_DIR / 'file1.json'
    path2 = TEST_DATA_DIR / 'file2.json'
    expected = (TEST_DATA_DIR / 'expected_flat_diff.txt').read_text()

    monkeypatch.setattr('sys.argv', ['gendiff', str(path1), str(path2)])
    from gendiff.scripts.gendiff import main
    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == expected.strip()

def test_generate_diff_flat_yaml():
    path1 = TEST_DATA_DIR / 'file1.yml'
    path2 = TEST_DATA_DIR / 'file2.yml'
    expected = (TEST_DATA_DIR / 'expected_flat_diff.txt').read_text()
    assert generate_diff(str(path1), str(path2)) == expected.rstrip('\n')


def test_yaml_and_json_give_same_diff():
    expected = (TEST_DATA_DIR / 'expected_flat_diff.txt').read_text()
    assert generate_diff(
        str(TEST_DATA_DIR / 'file1.json'),
        str(TEST_DATA_DIR / 'file2.json'),
    ) == expected.rstrip('\n')
    assert generate_diff(
        str(TEST_DATA_DIR / 'file1.yml'),
        str(TEST_DATA_DIR / 'file2.yml'),
    ) == expected.rstrip('\n')

def test_generate_diff_nested_json():
    path1 = TEST_DATA_DIR / 'nested_file1.json'
    path2 = TEST_DATA_DIR / 'nested_file2.json'
    expected = (TEST_DATA_DIR / 'expected_stylish.txt').read_text()
    assert generate_diff(str(path1), str(path2)) == expected.rstrip('\n')


def test_generate_diff_nested_yaml():
    path1 = TEST_DATA_DIR / 'nested_file1.yml'
    path2 = TEST_DATA_DIR / 'nested_file2.yml'
    expected = (TEST_DATA_DIR / 'expected_stylish.txt').read_text()
    assert generate_diff(str(path1), str(path2)) == expected.rstrip('\n')


def test_nested_json_and_yaml_give_same_diff():
    diff_json = generate_diff(
        str(TEST_DATA_DIR / 'nested_file1.json'),
        str(TEST_DATA_DIR / 'nested_file2.json'),
    )
    diff_yaml = generate_diff(
        str(TEST_DATA_DIR / 'nested_file1.yml'),
        str(TEST_DATA_DIR / 'nested_file2.yml'),
    )
    assert diff_json == diff_yaml

def test_generate_diff_plain_json():
    path1 = TEST_DATA_DIR / 'nested_file1.json'
    path2 = TEST_DATA_DIR / 'nested_file2.json'
    expected = (TEST_DATA_DIR / 'expected_plain.txt').read_text()
    assert generate_diff(str(path1), str(path2), 'plain') == expected.rstrip('\n')


def test_generate_diff_plain_yaml():
    path1 = TEST_DATA_DIR / 'nested_file1.yml'
    path2 = TEST_DATA_DIR / 'nested_file2.yml'
    expected = (TEST_DATA_DIR / 'expected_plain.txt').read_text()
    assert generate_diff(str(path1), str(path2), 'plain') == expected.rstrip('\n')


def test_generate_diff_json():
    path1 = TEST_DATA_DIR / 'nested_file1.json'
    path2 = TEST_DATA_DIR / 'nested_file2.json'
    diff = json.loads(generate_diff(str(path1), str(path2), 'json'))
    keys = [node['key'] for node in diff]
    assert keys == ['common', 'group1', 'group2', 'group3']
    common_types = {node['key']: node['type'] for node in diff[0]['children']}
    assert common_types == {
        'follow': 'added',
        'setting1': 'unchanged',
        'setting2': 'removed',
        'setting3': 'changed',
        'setting4': 'added',
        'setting5': 'added',
        'setting6': 'nested',
    }


def test_json_format_same_for_json_and_yaml():
    diff_json = json.loads(generate_diff(
        str(TEST_DATA_DIR / 'nested_file1.json'),
        str(TEST_DATA_DIR / 'nested_file2.json'),
        'json',
    ))
    diff_yaml = json.loads(generate_diff(
        str(TEST_DATA_DIR / 'nested_file1.yml'),
        str(TEST_DATA_DIR / 'nested_file2.yml'),
        'json',
    ))
    assert diff_json == diff_yaml
