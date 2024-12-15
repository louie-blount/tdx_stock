import os
import csv
from strats.strategy import Strategy
from stock_reader.lday_reader import calculate_rise_fall_percentage

class MicroStrategy(Strategy):
    """
    微盘股选股策略实现。
    """



    def execute(self, stocks):
        """
        按照微盘股策略筛选股票。

        策略：
        1. 初步筛选：总市值小于 50 亿。
        2. 市盈率(TTM)排名前25%。
        3. 净资产收益率排名前25%。
        4. 股息率排名前50%。
        5. 涨跌位小于27。

        Args:
            stocks (list): Stock 对象的列表。

        Returns:
            list: 符合条件的股票列表。
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

        # 排序
        pe_sorted = sorted(filtered_stocks, key=lambda x: self.safe_float(x.pe_ttm))
        roe_sorted = sorted(filtered_stocks, key=lambda x: self.safe_float(x.net_profit_margin_percent), reverse=True)
        div_yield_sorted = sorted(filtered_stocks, key=lambda x: self.safe_float(x.dividend_yield_percent), reverse=True)

        # 获取前50%股票的代码
        pe_top25 = {stock.code for stock in pe_sorted[:len(pe_sorted) // 4]}
        roe_top25 = {stock.code for stock in roe_sorted[:len(roe_sorted) // 4]}
        div_yield_top50 = {stock.code for stock in div_yield_sorted[:len(div_yield_sorted) // 2]}

        # 同时满足条件的股票
        selected_stocks = [
            stock for stock in filtered_stocks
            if stock.code in pe_top25 and stock.code in roe_top25 and stock.code in div_yield_top50
        ]

        return selected_stocks
