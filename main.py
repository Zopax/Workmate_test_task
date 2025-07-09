import argparse
import sys
from csv_processor.services.csv_processor import CSVProcessor

def main():
    parser = argparse.ArgumentParser(description="Обработчик CSV файлов")
    parser.add_argument('--file', default='products.csv', help="Путь к CSV файлу")
    parser.add_argument('--where', help="Условие фильтрации (например: 'rating>4.5')")
    parser.add_argument('--aggregate', help="Условие агрегации (например: 'price=avg')")
    args = parser.parse_args()

    try:
        processor = CSVProcessor(args.file)
        
        if not args.where and not args.aggregate:
            processor.print_table(processor.data)
            return
            
        result = None
        if args.where:
            result = processor.filter(args.where)
            processor.print_table(result)
        
        if args.aggregate:
            if args.where and result:
                # Агрегация по отфильтрованным данным
                agg_result = processor.aggregate(args.aggregate, data=result)
            else:
                # Агрегация по всем данным
                agg_result = processor.aggregate(args.aggregate)
            processor.print_table(agg_result)
            
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()