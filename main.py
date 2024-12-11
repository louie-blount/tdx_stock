from stock_reader.utils import read_stock_data
from stock_reader.lday_reader import calculate_rise_fall_percentage
from stock_reader.lday_reader import judge_lday_file_exists
from strats.strategy import Strategy
from strats.micro_strategy import MicroStrategy

def main():
    """
    主程序入口
    """
    # 替换为你的实际文件路径
    file_path = r"D:\Code\Python\program\tdx_stock\data\全部Ａ股20241209.txt"

    # 读取股票数据 [stocks 中存储的是当日所有主板股票行情]
    stocks = read_stock_data(file_path)
    # 先過濾出有日綫的數據
    stocks = [s for s in stocks if judge_lday_file_exists(s)]

    # 打印前3条记录
    print("股票数据样例：")
    for stock in stocks[:3]:
        print(vars(stock))  # 打印对象属性
        rise_fall_percentage = calculate_rise_fall_percentage(stock)
        print(f"涨跌百分位: {rise_fall_percentage}")  # 涨跌百分位
        
        
        # 创建并执行策略
    strategy = MicroStrategy()
    strategy.execute(stocks)
    

if __name__ == "__main__":
    main()
