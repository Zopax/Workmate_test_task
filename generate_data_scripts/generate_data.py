import csv
import random
from faker import Faker

def generate_large_csv(filename, num_rows=1000):
    fake = Faker()
    brands = ['apple', 'samsung', 'xiaomi', 'huawei', 'oppo', 'vivo', 'realme', 'oneplus']
    
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'brand', 'price', 'rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for i in range(num_rows):
            brand = random.choice(brands)
            writer.writerow({
                'name': f"{brand} {fake.word()} {random.randint(1, 20)}",
                'brand': brand,
                'price': random.randint(100, 2000),
                'rating': round(random.uniform(3.5, 5.0), 1)
            })

if __name__ == '__main__':
    generate_large_csv('large_file.csv', 1500) 