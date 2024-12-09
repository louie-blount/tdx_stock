import os
import csv
from strats.strategy import Strategy
from stock_reader.lday_reader import calculate_rise_fall_percentage



class MicroStrategy(Strategy):
    """
    微盘股选股策略实现。
    """

    @staticmethod
    def extract_market_value(value_str):
        """
        从形如 '45.67亿' 的字符串中提取数字部分并转换为浮点数。

        Args:
            value_str (str): 包含数值和单位的字符串，如 '45.67亿'。

        Returns:
            float: 提取的数值。
        """
        try:
            # 移除末尾的 "亿" 并转换为浮点数
            return float(value_str.rstrip("亿"))
        except ValueError:
            return 0.0

    @staticmethod
    def safe_float(value, default= float('inf')):
        """
        将字符串转换为浮点数，若无法转换则返回默认值。

        Args:
            value (str): 待转换的字符串。
            default (float): 无法转换时的默认值。

        Returns:
            float: 转换后的浮点数或默认值。
        """
        try:
            return float(value)
        except ValueError:
            return default

    def execute(self, stocks, output_path="micro_strategy_output.csv"):
        """
        按照微盘股策略选股。

        策略：
        1. 初步筛选：总市值小于 50 亿。
        2. 市盈率(TTM)排名前50%。
        3. 净资产收益率排名前50%。
        4. 股息率排名前50%。
        5. 涨跌位小于27。

        Args:
            stocks (list): Stock 对象的列表。
            output_path (str): 输出文件路径。
        """
        if not stocks:
            raise ValueError("股票列表为空！无法执行策略。")

        # 转换市值字段并筛选总市值小于 50 亿的股票
        filtered_stocks = [
            stock for stock in stocks
            if self.extract_market_value(stock.total_market_value_billion) < 50
        ]
        
        
        
        
        # 筛选涨跌位小于 27 的股票，同时更新每个股票的 `rise_fall_percentage` 属性
        for stock in filtered_stocks:
            stock.rise_fall_percentage = calculate_rise_fall_percentage(stock)
            stock.net_profit_margin_percent = stock.net_profit_margin_percent.replace("㈢", "")

        filtered_stocks = [s for s in filtered_stocks if s.rise_fall_percentage < 27]



        # 排序并获取排名前50%的股票
        pe_sorted = sorted(filtered_stocks, key=lambda x: self.safe_float(x.pe_ttm))
        roe_sorted = sorted(filtered_stocks, key=lambda x: self.safe_float(x.net_profit_margin_percent), reverse=True)
        div_yield_sorted = sorted(filtered_stocks, key=lambda x: self.safe_float(x.dividend_yield_percent), reverse=True)




        # 获取前50%股票的代码
        pe_top50 = {stock.code for stock in pe_sorted[:len(pe_sorted) // 2]}
        roe_top50 = {stock.code for stock in roe_sorted[:len(roe_sorted) // 2]}
        div_yield_top50 = {stock.code for stock in div_yield_sorted[:len(div_yield_sorted) // 2]}

        # 同时满足条件的股票
        selected_stocks = [
            stock for stock in filtered_stocks
            if stock.code in pe_top50 and stock.code in roe_top50 and stock.code in div_yield_top50
        ]

        # 写入 CSV 文件
        with open(output_path, mode="w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["代码", "名称", "当前价格", "市盈率(TTM)", "净资产收益率(%)", "股息率(%)", "涨跌位", "流通市值", "总市值"])
            for stock in selected_stocks:
                writer.writerow([
                    stock.code, stock.name, stock.current_price,
                    stock.pe_ttm, stock.net_profit_margin_percent, stock.dividend_yield_percent,
                    stock.rise_fall_percentage, stock.circulating_market_value_z, stock.total_market_value_billion
                ])

        print(f"选股结果已输出至 {os.path.abspath(output_path)}")
