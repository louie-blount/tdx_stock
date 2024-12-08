from tdx_reader import read_tdx_all_files
from microcap_strategy import calculate_percentile

def main():
    # 1. 读取本地通达信数据
    tdx_folder = "D:/Stocks/new_tdx/vipdoc/sh/lday/"  # 替换为通达信 .day 文件的文件夹路径
    tdx_data = read_tdx_all_files(tdx_folder)
    print(f"成功读取 {len(tdx_data)} 只股票的通达信数据")

    print(tdx_data)

if __name__ == "__main__":
    main()
