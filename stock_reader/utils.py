from stock import Stock
import csv

def read_stock_data(file_path):
    stocks = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')  # 使用制表符作为分隔符
        header = next(reader)  # 跳过标题行
        for row in reader:
            if len(row) >= 133:  # 确保有足够的字段数
                row = [s.strip() for s in row]
                stock = Stock(*row[:133])  # 截取前 134 个字段，忽略多余的
                stocks.append(stock)
            else:
                print(f"数据缺失行: {row}")  # 打印有问题的行
    return stocks
