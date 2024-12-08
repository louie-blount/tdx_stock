from pytdx.hq import TdxHq_API

# 创建 API 实例
api = TdxHq_API()

try:
    # 连接到行情服务器
    if not api.connect('180.153.18.170', 7709):
        print("服务器连接失败！")
        exit()

    # 获取沪市股票列表
    shanghai_codes = []
    start = 0
    while True:
        data = api.get_security_list(1, start)  # 1 表示沪市
        if not data:  # 如果没有数据，表示已经获取完毕
            break
        shanghai_codes.extend([d['code'] for d in data])
        start += len(data)

    # 获取深市股票列表
    shenzhen_codes = []
    start = 0
    while True:
        data = api.get_security_list(0, start)  # 0 表示深市
        if not data:
            break
        shenzhen_codes.extend([d['code'] for d in data])
        start += len(data)

    # 合并沪深股票代码
    print(f"上海主板 {len(shanghai_codes)} 只股票代码：")
    print(shanghai_codes)
    print(f"深圳主板 {len(shenzhen_codes)} 只股票代码：")
    # print(shenzhen_codes)

except Exception as e:
    print(f"发生错误：{e}")
finally:
    api.disconnect()
