import argparse
from csv_processor.services.csv_processor import CSVProcessor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default='products.csv')
    parser.add_argument('--where', type=str)
    parser.add_argument('--aggregate', type=str)
    args = parser.parse_args()

    try:
        processor = CSVProcessor(args.file)
        
        filtered_data = processor.data
        if args.where:
            try:
                filtered_data = processor.filter(args.where)
                if not filtered_data:
                    print("Нет данных, соответствующих условию фильтрации")
                    return
            except ValueError as e:
                print(f"Ошибка фильтрации: {e}")
                return
        
        if args.aggregate:
            try:
                result = processor.aggregate(args.aggregate, data=filtered_data)
                print("\nРезультат агрегации:")
                processor.print_table(result)
            except ValueError as e:
                print(f"Ошибка агрегации: {e}")
                return
        else:
            print("\nОтфильтрованные данные:")
            processor.print_table(filtered_data)
            
    except Exception as e:
        print(f"Критическая ошибка: {e}")

if __name__ == '__main__':
    main()