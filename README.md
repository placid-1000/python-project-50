# Вычислитель отличий (Python)

[![hexlet-check](https://github.com/placid-1000/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/placid-1000/python-project-50/actions/workflows/hexlet-check.yml)

[![CI](https://github.com/placid-1000/python-project-50/actions/workflows/check.yml/badge.svg)](https://github.com/placid-1000/python-project-50/actions/workflows/check.yml)

В этом проекте отрабатывается работа с коллекциями. Изучаются способы построения и обхода деревьев. Вы познакомитесь с разными форматами данных (JSON, YAML), научитесь их парсить и формировать. Начнете писать тесты (pytest) и освоите разработку через них. Познакомитесь с непрерывной интеграцией (CI) и элементами экстремального программирования (XP)

Учебный проект Хекслета: https://ru.hexlet.io/programs/python
Как это должно работать: https://asciinema.org/a/Pe6QypnLEmFWssNAjCOJN1iii

## Стек

- Python
- PyYAML
- pytest, pytest-cov
- ruff

## Установка

```bash
git clone https://github.com/placid-1000/python-project-50.git
cd python-project-50
make install
```

## Использование

Сравнение двух плоских JSON-файлов:

```bash
gendiff file1.json file2.json
```

Пример вывода:

```text
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

Демонстрация работы утилиты:

[![asciinema](https://asciinema.org/a/L6I04CGi7YqBFaQ2.svg)](https://asciinema.org/a/L6I04CGi7YqBFaQ2)

Сравнение двух плоских YAML-файлов:

```bash
gendiff file1.yml file2.yml
```

Демонстрация работы с YAML:

[![asciinema](https://asciinema.org/a/GXK3HAsHj3dPt8hE.svg)](https://asciinema.org/a/GXK3HAsHj3dPt8hE)

Сравнение файлов со вложенными структурами:

```bash
gendiff filepath1.json filepath2.json
```

Демонстрация работы с вложенными структурами:

[![asciinema](https://asciinema.org/a/8zsBEsEzatRm5SOq.svg)](https://asciinema.org/a/8zsBEsEzatRm5SOq)

Сравнение файлов в формате plain:

```bash
gendiff --format plain filepath1.json filepath2.json
```

Пример вывода:

```text
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
```

Демонстрация работы в формате plain:

[![asciinema](https://asciinema.org/a/vW08dc7qz5rJmu4A.svg)](https://asciinema.org/a/vW08dc7qz5rJmu4A)

Как библиотека:

```python
from gendiff import generate_diff

diff = generate_diff('file1.json', 'file2.json')
print(diff)
```

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.
