import csv
from tabulate import tabulate
import argparse

def open_file(file):
    try:
        with open(file, newline='') as csf:
            next(csf, None)
            spamreader = csv.reader(csf, delimiter=',', quotechar='|')
            spamreader = list(spamreader)
            print(tabulate(spamreader, headers=["name", "brand", "price", "rating"], tablefmt="grid"))
    except:  
        print("Неверно указан файл")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default='products.csv')
    parser.add_argument('--where', type=str, default='rating>4.5')
    parser.add_argument('--aggregate', type=str, default='rating=min')
    args = parser.parse_args()
    open_file(args.file)