import pytest
import csv
import os
from csv_processor.services.csv_processor import CSVProcessor

@pytest.fixture
def sample_csv(tmp_path):
    csv_path = os.path.join(tmp_path, "products.csv")
    data = [
        {"name": "Product1", "price": "100", "rating": "4.5"},
        {"name": "Product2", "price": "200", "rating": "4.0"},
        {"name": "Product3", "price": "300", "rating": "3.5"}
    ]
    
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price", "rating"])
        writer.writeheader()
        writer.writerows(data)
    
    return csv_path

@pytest.fixture
def empty_csv(tmp_path):
    csv_path = os.path.join(tmp_path, "empty.csv")
    with open(csv_path, 'w', newline='') as f:
        pass
    return csv_path

@pytest.fixture
def processor(sample_csv):
    return CSVProcessor(sample_csv)