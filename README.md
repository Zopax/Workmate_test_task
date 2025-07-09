# 📊 CSV Data Processor

**Профессиональный инструмент для обработки CSV-файлов** с поддержкой фильтрации, агрегации и визуального вывода таблиц.

---

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## 🌟 Особенности

- 🔍 Фильтрация по значениям (`>`, `<`, `=`, `>=`, `<=`)
- 📈 Агрегации (`avg`, `min`, `max`)
- 🧠 Автоматическое определение типов
- 📂 Поддержка больших CSV-файлов
- 🚫 Понятные сообщения об ошибках

---

## 🛠️ Требования

```bash
Python 3.8+
``` 

---

## ⚡ Установка

```bash
git clone https://github.com/Zopax/Workmate_test_task.git
cd csv-processor
pip install -r requirements.txt
```

---

## 🚀 Примеры использования
# 📄 Просмотр CSV-файла
```bash
python main.py --file products.csv
```
# 🔎 Фильтрация по условию
```bash
python main.py --file products.csv --where "price>1000"
```
# 📊 Агрегация значений
```bash
python main.py --file products.csv --aggregate "price=avg"
```
# 🔗 Комбинированный запрос
```bash
python main.py --file ratings.csv --where "category='Electronics'" --aggregate "rating=max"
```

---

## 🧮 Доступные операторы
| Оператор | Пример           | Описание          |
| -------- | ---------------- | ----------------- |
| `=`      | `"brand=Apple"`  | Точное совпадение |
| `>`      | `"price>500"`    | Больше чем        |
| `<`      | `"rating<4.5"`   | Меньше чем        |
| `>=`     | `"quantity>=10"` | Больше или равно  |
| `<=`     | `"age<=30"`      | Меньше или равно  |

---

## 📈 Примеры агрегаций
| Команда        | Описание             |
| -------------- | -------------------- |
| `price=avg`    | Средняя цена         |
| `quantity=min` | Минимальное кол-во   |
| `rating=max`   | Максимальный рейтинг |

---

## 🗂️ Пример CSV-файла
```scv
id,name,price,quantity,category
1,iPhone 15,999,45,Electronics
2,Notebook,2.5,120,Office
3,Monitor,299,32,Electronics
```

---

## 🧪 Запуск тестов
```bash
pytest --cov=csv_processor --cov-report=html
py -m pytest --cov=csv_processor --cov-report=html tests/ #для Windows
```
---

## Результат работы программы
# Запрос фильтрации 
![image](https://github.com/user-attachments/assets/a2b305fd-c484-4855-ad47-4c8585b4a38f)
# Комбинированный запрос
![image](https://github.com/user-attachments/assets/bc0a0984-07cd-412e-a672-2427bffb788c)
# Запрос агрегации
![image](https://github.com/user-attachments/assets/7086f553-8d93-474c-bb2b-851a1d6feb3b)

---

## Результат тестирования
![image](https://github.com/user-attachments/assets/798e95a3-1d91-4ec3-b0ad-aa2f7ba90503)
[Uploading i<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Coverage report</title>
    <link rel="icon" sizes="32x32" href="favicon_32_cb_58284776.png">
    <link rel="stylesheet" href="style_cb_db813965.css" type="text/css">
    <script src="coverage_html_cb_497bf287.js" defer></script>
</head>
<body class="indexfile">
<header>
    <div class="content">
        <h1>Coverage report:
            <span class="pc_cov">80%</span>
        </h1>
        <aside id="help_panel_wrapper">
            <input id="help_panel_state" type="checkbox">
            <label for="help_panel_state">
                <img id="keyboard_icon" src="keybd_closed_cb_ce680311.png" alt="Show/hide keyboard shortcuts">
            </label>
            <div id="help_panel">
                <p class="legend">Shortcuts on this page</p>
                <div class="keyhelp">
                    <p>
                        <kbd>f</kbd>
                        <kbd>s</kbd>
                        <kbd>m</kbd>
                        <kbd>x</kbd>
                        <kbd>c</kbd>
                        &nbsp; change column sorting
                    </p>
                    <p>
                        <kbd>[</kbd>
                        <kbd>]</kbd>
                        &nbsp; prev/next file
                    </p>
                    <p>
                        <kbd>?</kbd> &nbsp; show/hide this help
                    </p>
                </div>
            </div>
        </aside>
        <form id="filter_container">
            <input id="filter" type="text" value="" placeholder="filter...">
            <div>
                <input id="hide100" type="checkbox" >
                <label for="hide100">hide covered</label>
            </div>
        </form>
        <h2>
                <a class="button current">Files</a>
                <a class="button" href="function_index.html">Functions</a>
                <a class="button" href="class_index.html">Classes</a>
        </h2>
        <p class="text">
            <a class="nav" href="https://coverage.readthedocs.io/en/7.9.2">coverage.py v7.9.2</a>,
            created at 2025-07-09 17:50 +0700
        </p>
    </div>
</header>
<main id="index">
    <table class="index" data-sortable>
        <thead>
            <tr class="tablehead" title="Click to sort">
                <th id="file" class="name left" aria-sort="none" data-shortcut="f">File<span class="arrows"></span></th>
                <th id="statements" aria-sort="none" data-default-sort-order="descending" data-shortcut="s">statements<span class="arrows"></span></th>
                <th id="missing" aria-sort="none" data-default-sort-order="descending" data-shortcut="m">missing<span class="arrows"></span></th>
                <th id="excluded" aria-sort="none" data-default-sort-order="descending" data-shortcut="x">excluded<span class="arrows"></span></th>
                <th id="coverage" class="right" aria-sort="none" data-shortcut="c">coverage<span class="arrows"></span></th>
            </tr>
        </thead>
        <tbody>
            <tr class="region">
                <td class="name left"><a href="z_2f56670673477275___init___py.html">csv_processor\__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_c1a014a964a0f4c5___init___py.html">csv_processor\models\__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_c1a014a964a0f4c5_product_py.html">csv_processor\models\product.py</a></td>
                <td>11</td>
                <td>11</td>
                <td>0</td>
                <td class="right" data-ratio="0 11">0%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_4a2e0ca40180ddb0___init___py.html">csv_processor\services\__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_4a2e0ca40180ddb0_csv_processor_py.html">csv_processor\services\csv_processor.py</a></td>
                <td>102</td>
                <td>12</td>
                <td>0</td>
                <td class="right" data-ratio="90 102">88%</td>
            </tr>
        </tbody>
        <tfoot>
            <tr class="total">
                <td class="name left">Total</td>
                <td>113</td>
                <td>23</td>
                <td>0</td>
                <td class="right" data-ratio="90 113">80%</td>
            </tr>
        </tfoot>
    </table>
    <p id="no_rows">
        No items found using the specified filter.
    </p>
</main>
<footer>
    <div class="content">
        <p>
            <a class="nav" href="https://coverage.readthedocs.io/en/7.9.2">coverage.py v7.9.2</a>,
            created at 2025-07-09 17:50 +0700
        </p>
    </div>
    <aside class="hidden">
        <a id="prevFileLink" class="nav" href="z_4a2e0ca40180ddb0_csv_processor_py.html"></a>
        <a id="nextFileLink" class="nav" href="z_2f56670673477275___init___py.html"></a>
        <button type="button" class="button_prev_file" data-shortcut="["></button>
        <button type="button" class="button_next_file" data-shortcut="]"></button>
        <button type="button" class="button_show_hide_help" data-shortcut="?"></button>
    </aside>
</footer>
</body>
</html>
ndex.html…]()





