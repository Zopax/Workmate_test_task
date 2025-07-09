import pytest
from csv_processor.services.csv_processor import CSVProcessor

def test_load_data_success(processor):
    assert len(processor.data) == 3
    assert processor.data[0]["name"] == "Product1"

def test_load_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        CSVProcessor("nonexistent.csv")
        
def test_load_data_empty_file(empty_csv):
    with pytest.raises(ValueError):
        CSVProcessor(empty_csv)

def test_parse_condition_invalid(processor):
    with pytest.raises(ValueError, match="Условие должно быть непустой строкой"):
        processor._parse_condition(None)
    with pytest.raises(ValueError, match="Условие должно быть непустой строкой"):
        processor._parse_condition("")
    with pytest.raises(ValueError, match="Отсутствует значение для сравнения"):
        processor._parse_condition("price=")
    with pytest.raises(ValueError, match="Отсутствует название колонки"):
        processor._parse_condition("=100")
    with pytest.raises(ValueError, match="Колонка 'invalid' не найдена"):
        processor._parse_condition("invalid>100")
        
def test_parse_condition_valid(processor):
    assert processor._parse_condition("price>100") == ("price", ">", "100")
    assert processor._parse_condition("rating<=4.5") == ("rating", "<=", "4.5")
    assert processor._parse_condition("name=iPhone") == ("name", "=", "iPhone")
    assert processor._parse_condition(" price  >=  100 ") == ("price", ">=", "100")      

def test_filter_numeric(processor):
    result = processor.filter("price>150")
    assert len(result) == 2
    assert all(float(item["price"]) > 150 for item in result)

def test_filter_string(processor):
    result = processor.filter("name=Product1")
    assert len(result) == 1
    assert result[0]["name"] == "Product1"

def test_filter_invalid_column(processor):
    with pytest.raises(ValueError, match="Колонка 'invalid' не найдена"):
        processor.filter("invalid>100")
    
    with pytest.raises(ValueError, match="Колонка 'invalid' не найдена"):
        processor.filter("invalid>100")

def test_filter_invalid_operator(processor):
    with pytest.raises(ValueError, match="Неподдерживаемый оператор"):
        processor.filter("price?100")

def test_aggregate_avg(processor):
    func, value = processor.aggregate("price=avg")
    assert func == "AVG"
    assert value == 200.0

def test_aggregate_min(processor):
    func, value = processor.aggregate("price=min")
    assert func == "MIN"
    assert value == 100.0

def test_aggregate_max(processor):
    func, value = processor.aggregate("price=max")
    assert func == "MAX"
    assert value == 300.0

def test_aggregate_invalid_column(processor):
    with pytest.raises(ValueError, match="Колонка invalid не существует"):
        processor.aggregate("invalid=avg")

def test_aggregate_invalid_func(processor):
    with pytest.raises(ValueError, match="Неподдерживаемая агрегатная функция"):
        processor.aggregate("price=invalid")

def test_print_table(capsys, processor):
    processor.print_table(processor.data)
    captured = capsys.readouterr()
    assert "Product1" in captured.out
    assert "100" in captured.out

def test_print_aggregation(capsys, processor):
    processor.print_table(("TEST", 123))
    captured = capsys.readouterr()
    assert "TEST" in captured.out
    assert "123" in captured.out