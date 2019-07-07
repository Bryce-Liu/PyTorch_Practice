# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 17:51
# @Author  : Bryce Liu
# @FileName: pandas_merge.py

import pandas as pd
import numpy as np

# ==========单标签合并=========
left = pd.DataFrame({"key": ["K0", "K1", "K2", "K3"],
                     "A": ["A0", "A1", "A2", "A3"],
                     "B": ["B0", "B1", "B2", "B3"]})
right = pd.DataFrame({"key": ["K0", "K1", "K2", "K3"],
                      "C": ["C0", "C1", "C2", "C3"],
                      "D": ["D0", "D1", "D2", "D3"]})
# print(left)
"""
  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3
"""
# print(right)
"""
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
"""

# ==========merge
result = pd.merge(left, right, on="key")  # 基于某个标签进行合并
# print(result)
"""
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K1  A1  B1  C1  D1
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
"""

# ==========多标签合并=========
left = pd.DataFrame({"key1": ["K0", "K0", "K1", "K2"],
                     "key2": ["K0", "K1", "K0", "K1"],
                     "A": ["A0", "A1", "A2", "A3"],
                     "B": ["B0", "B1", "B2", "B3"]})
right = pd.DataFrame({"key1": ["K0", "K1", "K1", "K2"],
                      "key2": ["K0", "K0", "K0", "K0"],
                      "C": ["C0", "C1", "C2", "C3"],
                      "D": ["D0", "D1", "D2", "D3"]})
# print(left)
"""
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3
"""
# print(right)
"""
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
"""

# default
# 多标签合并默认需要多个标签完全相同的行才能合并
result = pd.merge(left, right, on=["key1", "key2"])
# print(result)
"""
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K1   K0  A2  B2  C1  D1
2   K1   K0  A2  B2  C2  D2
"""

# outer
# 全部合并，没有数据的部分使用NaN填充
result = pd.merge(left, right, on=["key1", "key2"], how="outer")
# print(result)
"""
  key1 key2    A    B    C    D
0   K0   K0   A0   B0   C0   D0
1   K0   K1   A1   B1  NaN  NaN
2   K1   K0   A2   B2   C1   D1
3   K1   K0   A2   B2   C2   D2
4   K2   K1   A3   B3  NaN  NaN
5   K2   K0  NaN  NaN   C3   D3
"""

# 指定基准
# 此处以right作为标准merge
result = pd.merge(left, right, on=["key1", "key2"], how="right")
# print(result)
"""
  key1 key2    A    B   C   D
0   K0   K0   A0   B0  C0  D0
1   K1   K0   A2   B2  C1  D1
2   K1   K0   A2   B2  C2  D2
3   K2   K0  NaN  NaN  C3  D3
"""

# ==========显示合并信息=========
df1 = pd.DataFrame({"column": [0, 1], "left": ["a", "b"]})
df2 = pd.DataFrame({"column": [1, 2, 2], "right": [2, 2, 2]})
# print(df1)
"""
   column left
0       0    a
1       1    b
"""
# print(df2)
"""
   column  right
0       1      2
1       2      2
2       2      2
"""

result = pd.merge(df1, df2, on=["column"], how="outer", indicator=True)
# print(result)
"""
   column left  right      _merge
0       0    a    NaN   left_only
1       1    b    2.0        both
2       2  NaN    2.0  right_only
3       2  NaN    2.0  right_only
"""

# 指定indicator名称
result = pd.merge(df1, df2, on=["column"], how="outer", indicator="indicator_column")
# print(result)
"""
   column left  right indicator_column
0       0    a    NaN        left_only
1       1    b    2.0             both
2       2  NaN    2.0       right_only
3       2  NaN    2.0       right_only
"""