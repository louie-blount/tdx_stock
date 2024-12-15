from abc import ABC, abstractmethod

class Strategy(ABC):
    """
    策略抽象基类。
    """
    @abstractmethod
    def execute(self, stocks):
        """
        执行选股策略。

        Args:
            stocks (list): Stock 对象的列表。
        """
        pass


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
    def safe_float(value, default=float('inf')):
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