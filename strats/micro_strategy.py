import os
import csv
from strats.strategy import Strategy
from stock_reader.lday_reader import calculate_rise_fall_percentage
from collections import defaultdict

class MicroStrategy(Strategy):
    """
    微盘股选股策略实现。
    """
    
    def classify_and_filter_stocks(self, stocks):
        # 按行业分类
        sector_dict = defaultdict(list)
        for stock in stocks:
            sector_dict[stock.sector].append(stock)
        
        # 按市值筛选每个行业中市值最小的20只股票
        result = {}
        for sector, stock_list in sector_dict.items():
            # 按市值升序排序
            
            # 筛选涨跌位小于27的股票，并更新每个股票的 `rise_fall_percentage` 属性
            for stock in stock_list:
                stock.rise_fall_percentage = calculate_rise_fall_percentage(stock)
                stock.net_profit_margin_percent = stock.net_profit_margin_percent.replace("㈢", "")
            # 筛选涨跌位小于27的股票, 市值小于50亿
            filtered_stocks = [s for s in stock_list if s.rise_fall_percentage < 27 and self.extract_market_value(s.total_market_value_billion) < 40]

                        # 排序
            pe_sorted = sorted(filtered_stocks, key=lambda x: self.safe_float(x.pe_ttm))
            roe_sorted = sorted(filtered_stocks, key=lambda x: self.safe_float(x.net_profit_margin_percent), reverse=True)
            div_yield_sorted = sorted(filtered_stocks, key=lambda x: self.safe_float(x.dividend_yield_percent), reverse=True)

            # 获取前50%股票的代码
            pe_top25 = {stock.code for stock in pe_sorted[:len(pe_sorted) // 4]}
            roe_top25 = {stock.code for stock in roe_sorted[:len(roe_sorted) // 4]}
            div_yield_top50 = {stock.code for stock in div_yield_sorted[:len(div_yield_sorted) // 2]}
            
            # 同时满足条件的股票
            sector_selected_stocks = [
                stock for stock in filtered_stocks
                if stock.code in pe_top25 and stock.code in roe_top25 and stock.code 
            ]
            
            
            
            sorted_stocks = sorted(sector_selected_stocks, key=lambda x: x.total_market_value_billion)
            # 筛选最小的3只股票
            result[sector] = sorted_stocks[:3]
        
        return result





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
        
        
        sector_dict = self.classify_and_filter_stocks(stocks)
        
        
        selected_stocks = []
        
        # 筛选涨跌位小于 27 的股票，同时更新每个股票的 `rise_fall_percentage` 属性
        # 按行业对每个行业的股票列表单独筛选，并合并结果
        for sector, stocks in sector_dict.items():

            # 合并结果
            selected_stocks.extend(stocks)

        return selected_stocks
