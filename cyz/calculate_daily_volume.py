import numpy as np

def calculate_daily_volume(freight_rate_per_volume):
    # parameter a, b are determined by function fitting of matlab
    a = 88.4
    b = -0.009267
    freight_rate_per_volume = np.array(freight_rate_per_volume)
    daily_volume = a * np.exp(b * freight_rate_per_volume)
    return daily_volume

if __name__ == "__main__":
    # example : 输入可以是列表或单个数据
    res = calculate_daily_volume([34,32,-11])
    print(res)