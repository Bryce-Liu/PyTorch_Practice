# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 19:15
# @Author  : Bryce Liu
# @FileName: pandas_plot.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========Series
data = pd.Series(np.random.randn(1000),
                 index=np.arange(1000))
data = data.cumsum()  # 数据累加
# print(data.head())
"""
0    0.373907
1    0.222079
2   -1.021797
3   -2.877201
4   -2.521036
dtype: float64
"""
# data.plot()
# plt.show()

# ==========DataFrame
data = pd.DataFrame(np.random.randn(1000, 4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
data = data.cumsum()
# print(data.head())
"""
          A         B         C         D
0  2.065516  0.780487  0.414750  0.876275
1  0.564663  0.304826  0.706830  0.059724
2  1.897543  1.339585 -1.025774  0.191925
3  2.117503  1.885135 -0.593751  0.461214
4  1.921466  1.049373 -0.783439  0.653394
"""
# data.plot()
# plt.show()

# ===========.scatter()
ax = data.plot.scatter(x="A",y="B",color="DarkBlue",label="Class 1")
data.plot.scatter(x="C",y="D",color="DarkGreen",label="Class 2", ax=ax)
plt.show()
