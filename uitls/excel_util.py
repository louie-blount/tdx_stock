import os
import csv
from datetime import datetime

# 获取当前日期
today = datetime.today().strftime('%Y%m%d')

# 生成以当天日期结尾的文件名
output_path = f"micro_strategy_output_{today}.csv"

print(output_path)





def save_stocks_to_excel(stocks, output_path="micro_strategy_output.csv"):
    """
    将股票列表输出为 CSV 文件。

    Args:
        stocks (list): Stock 对象的列表。
        output_path (str): 输出文件路径。
    """
    if not stocks:
        raise ValueError("股票列表为空！无法生成 Excel 文件。")

    # 写入 CSV 文件
    with open(output_path, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["代码", "名称", "细分行业", "当前价格", "市盈率(TTM)", "净资产收益率(%)", "股息率(%)", "涨跌位", "beta系数", "流通市值", "总市值"])
        for stock in stocks:
            writer.writerow([
                stock.code, 
                stock.name, 
                stock.sector, 
                stock.current_price,
                stock.pe_ttm, 
                stock.net_profit_margin_percent, 
                stock.dividend_yield_percent,
                stock.rise_fall_percentage, 
                stock.beta_coefficient, 
                stock.circulating_market_value_z, 
                stock.total_market_value_billion
            ])

    print(f"选股结果已输出至 {os.path.abspath(output_path)}")
