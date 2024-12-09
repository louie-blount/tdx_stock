import os
import struct

def read_tdx_day_file(file_path):
    """
    读取通达信 `.day` 格式的历史日线数据文件。

    Args:
        file_path (str): `.day` 文件路径。

    Returns:
        list[dict]: 包含每一天的日期、开盘价、最高价、最低价、收盘价、成交量的字典列表。
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")

    data = []
    with open(file_path, "rb") as file:
        while chunk := file.read(32):  # 每 32 字节为一条记录
            # 按格式解码二进制数据
            date, open_price, high_price, low_price, close_price, amount, volume, _ = struct.unpack("<iiiiifii", chunk)
            data.append({
                "date": date,
                "open": open_price / 100.0,
                "high": high_price / 100.0,
                "low": low_price / 100.0,
                "close": close_price / 100.0,
                "volume": volume,
                "amount": amount / 10.0
            })
    return data





def calculate_rise_fall_percentage(stock, data_dir_sh="D:\\Stocks\\new_tdx\\vipdoc\\sh\\lday", data_dir_sz="D:\\Stocks\\new_tdx\\vipdoc\\sz\\lday"):
    """
    根据通达信历史日线数据计算涨跌位百分比。

    Args:
        stock (Stock): Stock 对象，包含股票代码和当前价格。
        data_dir_sh (str): 上证历史数据目录。
        data_dir_sz (str): 深证历史数据目录。

    Returns:
        float: 涨跌位百分比。
    """
    # 判断股票市场
    if stock.code.startswith("6"):  # 上证股票
        file_path = os.path.join(data_dir_sh, f"sh{stock.code}.day")
    elif stock.code.startswith(("0", "3")):  # 深证股票
        file_path = os.path.join(data_dir_sz, f"sz{stock.code}.day")
    else:
        raise ValueError(f"无法确定市场，股票代码: {stock.code}")

    # 读取日线数据
    try:
        data = read_tdx_day_file(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"未找到历史数据文件: {file_path}")

    # 提取最近 999 个交易日的数据
    recent_data = data[-999:] if len(data) >= 999 else data

    if not recent_data:
        raise ValueError(f"无历史数据可用: {stock.code}")

    # 计算最高价和最低价
    highest_price = max(day["high"] for day in recent_data)
    lowest_price = min(day["low"] for day in recent_data)

    # 检查价格范围
    if highest_price == lowest_price:
        raise ValueError(f"最高价与最低价相同，无法计算涨跌位: {stock.code}")

    # 确保 current_price 是浮点数
    current_price = float(stock.current_price)
    
    # 计算涨跌位百分比
    rise_fall_percentage = (current_price - lowest_price) / (highest_price - lowest_price) * 100
    print(f"股票 {stock.name} {stock.code} 过去999个交易日最高价: {highest_price} 最低价: {lowest_price} 现价：{current_price} 涨跌位：{rise_fall_percentage}%")  # 打印
    
    return rise_fall_percentage






def judge_lday_file_exists(stock, data_dir_sh="D:\\Stocks\\new_tdx\\vipdoc\\sh\\lday", data_dir_sz="D:\\Stocks\\new_tdx\\vipdoc\\sz\\lday"):
    """
    判断通达信历史日线数据是否存在

    Args:
        stock (Stock): Stock 对象，包含股票代码和当前价格。
        data_dir_sh (str): 上证历史数据目录。
        data_dir_sz (str): 深证历史数据目录。

    Returns:
        bool: 是否存在
    """
    # 判断股票市场
    if stock.code.startswith("6"):  # 上证股票
        file_path = os.path.join(data_dir_sh, f"sh{stock.code}.day")
    elif stock.code.startswith(("0", "3")):  # 深证股票
        file_path = os.path.join(data_dir_sz, f"sz{stock.code}.day")
    else:
        raise ValueError(f"无法确定市场，股票代码: {stock.code}")


    return os.path.exists(file_path)