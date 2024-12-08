class Stock:
    """
    股票对象类，包含A股股票数据的所有字段
    """
    def __init__(self, code, name, change_percent, current_price, price_change, bid_price, ask_price,
                 total_volume, current_volume, speed_percent, turnover_percent, open_price, highest_price,
                 lowest_price, previous_close, pe_dynamic, total_amount, volume_ratio, sector, region,
                 amplitude_percent, average_price, inner_volume, outer_volume, inner_outer_ratio, premium_percent,
                 bid_volume, ask_volume, unmatched_volume, bid_ratio_percent, volume_growth_rate_percent,
                 short_turnover_percent, two_minute_amount, main_net_amount, main_net_ratio_percent,
                 previous_turnover, opening_amount, opening_rush_ratio_percent, opening_prev_ratio_percent,
                 opening_prev_sealing_ratio_percent, opening_turnover, limit_up_bid, bidding_volume_ratio,
                 sealing_ratio, sealing_amount, circulating_shares_billion, circulating_market_value_billion,
                 total_market_value_billion, strength_percent, activity_level, continuous_rise_days,
                 previous_rise_percent, three_day_rise_percent, five_day_rise_percent, ten_day_rise_percent,
                 twenty_day_rise_percent, sixty_day_rise_percent, one_year_rise_percent, month_to_date_percent,
                 year_to_date_percent, yearly_limit_up_days, circulating_shares_z, turnover_z, circulating_market_value_z,
                 market_value_increase, pe_ttm, pe_static, beta_coefficient, distance_from_5_day_line_percent,
                 recent_indicators, short_term_form, medium_term_form, long_term_form, opening_percent, highest_percent,
                 lowest_percent, average_rise_percent, rebound_wave_percent, attack_wave_percent, financial_update,
                 listing_date, total_shares_billion, a_b_shares_billion, h_shares_billion, total_assets_billion,
                 net_assets_billion, minority_equity_billion, asset_liability_ratio_percent, current_assets_billion,
                 fixed_assets_billion, intangible_assets_billion, current_liabilities_billion, cash_assets_billion,
                 inventory_billion, receivables_billion, contract_liabilities_billion, capital_reserve_billion,
                 operating_revenue_billion, operating_cost_billion, operating_profit_billion, investment_income_billion,
                 total_profit_billion, net_profit_after_tax_billion, net_profit_billion, net_profit_excluding_non_billion,
                 undistributed_profit_billion, operating_cash_flow_billion, total_cash_flow_billion, shareholders_count,
                 per_capita_holdings, per_capita_market_value, profit_growth_rate_percent, revenue_growth_rate_percent,
                 pb_ratio, ps_ratio, sales_ratio, dividend_yield_percent, earnings_per_share, net_asset_per_share,
                 capital_reserve_per_share, undistributed_per_share, cash_flow_per_share, equity_ratio_percent,
                 net_profit_margin_percent, gross_margin_percent, operating_margin_percent, net_margin_percent,
                 r_d_expense_billion, employee_count, transaction_code, self_select_date, self_select_price,
                 self_select_return_percent):
        """
        初始化函数，接收所有字段的值
        """
        self.code = code  # 代码
        self.name = name  # 名称
        self.change_percent = change_percent  # 涨幅%
        self.current_price = current_price  # 现价
        self.price_change = price_change  # 涨跌
        self.bid_price = bid_price  # 买价
        self.ask_price = ask_price  # 卖价
        self.total_volume = total_volume  # 总量
        self.current_volume = current_volume  # 现量
        self.speed_percent = speed_percent  # 涨速%
        self.turnover_percent = turnover_percent  # 换手%
        self.open_price = open_price  # 今开
        self.highest_price = highest_price  # 最高
        self.lowest_price = lowest_price  # 最低
        self.previous_close = previous_close  # 昨收
        self.pe_dynamic = pe_dynamic  # 市盈(动)
        self.total_amount = total_amount  # 总金额
        self.volume_ratio = volume_ratio  # 量比
        self.sector = sector  # 细分行业
        self.region = region  # 地区
        self.amplitude_percent = amplitude_percent  # 振幅%
        self.average_price = average_price  # 均价
        self.inner_volume = inner_volume  # 内盘
        self.outer_volume = outer_volume  # 外盘
        self.inner_outer_ratio = inner_outer_ratio  # 内外比
        self.premium_percent = premium_percent  # 溢价%
        self.bid_volume = bid_volume  # 买量
        self.ask_volume = ask_volume  # 卖量
        self.unmatched_volume = unmatched_volume  # 未匹配量
        self.bid_ratio_percent = bid_ratio_percent  # 委比%
        self.volume_growth_rate_percent = volume_growth_rate_percent  # 量涨速%
        self.short_turnover_percent = short_turnover_percent  # 短换手%
        self.two_minute_amount = two_minute_amount  # 2分钟金额
        self.main_net_amount = main_net_amount  # 主力净额
        self.main_net_ratio_percent = main_net_ratio_percent  # 主力净比%
        self.previous_turnover = previous_turnover  # 昨成交额
        self.opening_amount = opening_amount  # 开盘金额
        self.opening_rush_ratio_percent = opening_rush_ratio_percent  # 开盘抢筹%
        self.opening_prev_ratio_percent = opening_prev_ratio_percent  # 开盘昨比%
        self.opening_prev_sealing_ratio_percent = opening_prev_sealing_ratio_percent  # 开盘昨封比%
        self.opening_turnover = opening_turnover  # 开盘换手z
        self.limit_up_bid = limit_up_bid  # 竞价涨停买
        self.bidding_volume_ratio = bidding_volume_ratio  # 竞价量比
        self.sealing_ratio = sealing_ratio  # 封成比
        self.sealing_amount = sealing_amount  # 封单额
        self.circulating_shares_billion = circulating_shares_billion  # 流通股(亿)
        self.circulating_market_value_billion = circulating_market_value_billion  # 流通市值(亿)
        self.total_market_value_billion = total_market_value_billion  # AB股总市值
        self.strength_percent = strength_percent  # 强弱度%
        self.activity_level = activity_level  # 活跃度
        self.continuous_rise_days = continuous_rise_days  # 连涨天
        self.previous_rise_percent = previous_rise_percent  # 昨涨幅%
        self.three_day_rise_percent = three_day_rise_percent  # 3日涨幅%
        self.five_day_rise_percent = five_day_rise_percent  # 5日涨幅%
        self.ten_day_rise_percent = ten_day_rise_percent  # 10日涨幅%
        self.twenty_day_rise_percent = twenty_day_rise_percent  # 20日涨幅%
        self.sixty_day_rise_percent = sixty_day_rise_percent  # 60日涨幅%
        self.one_year_rise_percent = one_year_rise_percent  # 一年涨幅%
        self.month_to_date_percent = month_to_date_percent  # 月初至今%
        self.year_to_date_percent = year_to_date_percent  # 年初至今%
        self.yearly_limit_up_days = yearly_limit_up_days  # 年涨停天
        self.circulating_shares_z = circulating_shares_z  # 流通股本Z
        self.turnover_z = turnover_z  # 换手Z
        self.circulating_market_value_z = circulating_market_value_z  # 流通市值Z
        self.market_value_increase = market_value_increase  # 市值增减
        self.pe_ttm = pe_ttm  # 市盈(TTM)
        self.pe_static = pe_static  # 市盈(静)
        self.beta_coefficient = beta_coefficient  # 贝塔系数
        self.distance_from_5_day_line_percent = distance_from_5_day_line_percent  # 距5日线%
        self.recent_indicators = recent_indicators  # 近日指标提示
        self.short_term_form = short_term_form  # 短期形态
        self.medium_term_form = medium_term_form  # 中期形态
        self.long_term_form = long_term_form  # 长期形态
        self.opening_percent = opening_percent  # 开盘%
        self.highest_percent = highest_percent  # 最高%
        self.lowest_percent = lowest_percent  # 最低%
        self.average_rise_percent = average_rise_percent  # 均涨幅%
        self.rebound_wave_percent = rebound_wave_percent  # 回头波%
        self.attack_wave_percent = attack_wave_percent  # 攻击波%
        self.financial_update = financial_update  # 财务更新
        self.listing_date = listing_date  # 上市日期
        self.total_shares_billion = total_shares_billion  # 总股本(亿)
        self.a_b_shares_billion = a_b_shares_billion  # A/B股(亿)
        self.h_shares_billion = h_shares_billion  # H股(亿)
        self.total_assets_billion = total_assets_billion  # 总资产(亿)
        self.net_assets_billion = net_assets_billion  # 净资产(亿)
        self.minority_equity_billion = minority_equity_billion  # 少数股权(亿)
        self.asset_liability_ratio_percent = asset_liability_ratio_percent  # 资产负债率%
        self.current_assets_billion = current_assets_billion  # 流动资产(亿)
        self.fixed_assets_billion = fixed_assets_billion  # 固定资产(亿)
        self.intangible_assets_billion = intangible_assets_billion  # 无形资产(亿)
        self.current_liabilities_billion = current_liabilities_billion  # 流动负债(亿)
        self.cash_assets_billion = cash_assets_billion  # 货币资金(亿)
        self.inventory_billion = inventory_billion  # 存货(亿)
        self.receivables_billion = receivables_billion  # 应收账款(亿)
        self.contract_liabilities_billion = contract_liabilities_billion  # 合同负债(亿)
        self.capital_reserve_billion = capital_reserve_billion  # 资本公积金(亿)
        self.operating_revenue_billion = operating_revenue_billion  # 营业收入(亿)
        self.operating_cost_billion = operating_cost_billion  # 营业成本(亿)
        self.operating_profit_billion = operating_profit_billion  # 营业利润(亿)
        self.investment_income_billion = investment_income_billion  # 投资收益(亿)
        self.total_profit_billion = total_profit_billion  # 利润总额(亿)
        self.net_profit_after_tax_billion = net_profit_after_tax_billion  # 税后利润(亿)
        self.net_profit_billion = net_profit_billion  # 净利润(亿)
        self.net_profit_excluding_non_billion = net_profit_excluding_non_billion  # 扣非净利润(亿)
        self.undistributed_profit_billion = undistributed_profit_billion  # 未分利润(亿)
        self.operating_cash_flow_billion = operating_cash_flow_billion  # 经营现金流(亿)
        self.total_cash_flow_billion = total_cash_flow_billion  # 总现金流(亿)
        self.shareholders_count = shareholders_count  # 股东人数
        self.per_capita_holdings = per_capita_holdings  # 人均持股
        self.per_capita_market_value = per_capita_market_value  # 人均市值
        self.profit_growth_rate_percent = profit_growth_rate_percent  # 利润同比%
        self.revenue_growth_rate_percent = revenue_growth_rate_percent  # 收入同比%
        self.pb_ratio = pb_ratio  # 市净率
        self.ps_ratio = ps_ratio  # 市现率
        self.sales_ratio = sales_ratio  # 市销率
        self.dividend_yield_percent = dividend_yield_percent  # 股息率%
        self.earnings_per_share = earnings_per_share  # 每股收益
        self.net_asset_per_share = net_asset_per_share  # 每股净资产
        self.capital_reserve_per_share = capital_reserve_per_share  # 每股公积
        self.undistributed_per_share = undistributed_per_share  # 每股未分
        self.cash_flow_per_share = cash_flow_per_share  # 每股现金流
        self.equity_ratio_percent = equity_ratio_percent  # 权益比率%
        self.net_profit_margin_percent = net_profit_margin_percent  # 净益率%
        self.gross_margin_percent = gross_margin_percent  # 毛利率%
        self.operating_margin_percent = operating_margin_percent  # 营业利润率%
        self.net_margin_percent = net_margin_percent  # 净利润率%
        self.r_d_expense_billion = r_d_expense_billion  # 研发费用(亿)
        self.employee_count = employee_count  # 员工人数
        self.transaction_code = transaction_code  # 交易代码
        self.self_select_date = self_select_date  # 自选日期
        self.self_select_price = self_select_price  # 自选价
        self.self_select_return_percent = self_select_return_percent  # 自选收益%
        
        self.rise_fall_percentage = 200 #自定义字段，涨跌百分位




