# csv_processor.py
import csv
from tabulate import tabulate

class CSVProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._load_data()
        if not self.data:
            raise ValueError("Файл не содержит данных")

    def _load_data(self):
        try:
            with open(self.file_path, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                if not reader.fieldnames:
                    raise ValueError("Файл не содержит заголовков")
                return [row for row in reader]
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл {self.file_path} не найден") from e
        except csv.Error as e:
            raise csv.Error(f"Ошибка чтения CSV: {e}") from e
        except Exception as e:
            raise ValueError(f"Ошибка загрузки данных: {e}") from e

    def _parse_condition(self, condition):
        if not isinstance(condition, str) or not condition.strip():
            raise ValueError("Условие должно быть непустой строкой")
        
        operators = ["<=", ">=", "=", "<", ">"]
        
        for op in operators:
            if op in condition:
                parts = condition.split(op, 1)
                if len(parts) != 2:
                    continue
                    
                column = parts[0].strip()
                value = parts[1].strip()
                
                if not column:
                    raise ValueError("Отсутствует название колонки")
                if not value:
                    raise ValueError("Отсутствует значение для сравнения")
                if column not in self.data[0]:
                    raise ValueError(f"Колонка '{column}' не найдена")
                    
                return column, op, value
        
        raise ValueError(f"Неподдерживаемый оператор в условии")

    def filter(self, condition):
        try:
            column, operator, value = self._parse_condition(condition)
            filtered = []
            
            for row in self.data:
                row_value = row[column]
                
                if operator in [">", ">=", "<", "<="]:
                    try:
                        row_float = float(row_value)
                        value_float = float(value)
                    except ValueError:
                        continue

                    if operator == ">" and row_float > value_float:
                        filtered.append(row)
                    elif operator == ">=" and row_float >= value_float:
                        filtered.append(row)
                    elif operator == "<" and row_float < value_float:
                        filtered.append(row)
                    elif operator == "<=" and row_float <= value_float:
                        filtered.append(row)
                elif operator == "=" and str(row_value) == str(value):
                    filtered.append(row)
                    
            return filtered
        except ValueError as e:
            raise ValueError(f"Ошибка фильтрации: {str(e)}") from e

    def aggregate(self, condition):
        try:
            if "=" not in condition:
                raise ValueError("Неверный формат агрегации")

            column, func = condition.split("=", 1)
            column = column.strip()
            func = func.strip().lower()
            
            if not column or not func:
                raise ValueError("Пустое значение в условии агрегации")
            if column not in self.data[0]:
                raise ValueError(f"Колонка {column} не существует")
                
            values = []
            for row in self.data:
                try:
                    value = row[column]
                    values.append(float(value))
                except (ValueError, TypeError):
                    raise ValueError(f"Невозможно преобразовать значение '{value}' в число")
                    
            if not values:
                raise ValueError(f"Нет числовых значений в колонке {column}")
                
            if func == "avg":
                return ("AVG", sum(values) / len(values))
            elif func == "min":
                return ("MIN", min(values))
            elif func == "max":
                return ("MAX", max(values))
            else:
                raise ValueError(f"Неподдерживаемая агрегатная функция: {func}")
                
        except ValueError as e:
            raise ValueError(f"Ошибка агрегации: {e}") from e

    @staticmethod
    def print_table(data, title=None):
        if not data:
            print("Нет данных для отображения")
            return
            
        if isinstance(data, list):
            print(tabulate(data, headers="keys", tablefmt="grid"))
        else:
            func, value = data
            print(tabulate([[func, value]], headers=["Aggregation", "Value"], tablefmt="grid"))