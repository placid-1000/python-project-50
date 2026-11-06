# Вычислитель отличий (Python)

[![hexlet-check](https://github.com/placid-1000/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/placid-1000/python-project-50/actions)

В этом проекте отрабатывается работа с коллекциями. Изучаются способы построения и обхода деревьев. Вы познакомитесь с разными форматами данных (JSON, YAML), научитесь их парсить и формировать. Начнете писать тесты (pytest) и освоите разработку через них. Познакомитесь с непрерывной интеграцией (CI) и элементами экстремального программирования (XP)

Учебный проект Хекслета: https://ru.hexlet.io/programs/python
Как это должно работать: https://asciinema.org/a/Pe6QypnLEmFWssNAjCOJN1iii

## Стек

- Python

## Установка

```bash
git clone https://github.com/placid-1000/python-project-50.git
cd python-project-50
make install
```


## Использование

Демонстрация работы утилиты:

[![asciinema](https://asciinema.org/a/L6I04CGi7YqBFaQ2.svg)](https://asciinema.org/a/L6I04CGi7YqBFaQ2)

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
