import matplotlib.pyplot as plt
import numpy as np
# 解决中文显示问题

total_times = 10000

# 记录骰子的结果
roll1_arr = np.random.randint(1, 7, size=total_times)
roll2_arr = np.random.randint(1, 7, size=total_times)
result_arr = roll1_arr + roll2_arr
