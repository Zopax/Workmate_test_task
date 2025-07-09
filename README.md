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
![keybd_closed_cb_ce680311](https://github.com/user-attachments/assets/1e2cedb5-cd9f-4e60-afd6-114e1c847f58)




