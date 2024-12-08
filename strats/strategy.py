from abc import ABC, abstractmethod

class Strategy(ABC):
    """
    策略抽象基类。
    """
    @abstractmethod
    def execute(self, stocks, output_path):
        """
        执行选股策略。

        Args:
            stocks (list): Stock 对象的列表。
            output_path (str): 输出文件路径。
        """
        pass
