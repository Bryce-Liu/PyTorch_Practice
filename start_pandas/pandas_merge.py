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

# ==========根据行号index合并=========
left = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"],
                     "B": ["B0", "B1", "B2", "B3"]},
                    index=["K0", "K1", "K2", "K4"])
right = pd.DataFrame({"C": ["C0", "C1", "C2", "C3"],
                      "D": ["D0", "D1", "D2", "D3"]},
                     index=["K0", "K3", "K4", "K5"])
# print(left)
"""
     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
K4  A3  B3
"""
# print(right)
"""
     C   D
K0  C0  D0
K3  C1  D1
K4  C2  D2
K5  C3  D3
"""
# pandas.errors.MergeError: Must pass right_on or right_index=True
result = pd.merge(left, right, left_index=True, right_index=True, how="outer")
# print(result)
"""
      A    B    C    D
K0   A0   B0   C0   D0
K1   A1   B1  NaN  NaN
K2   A2   B2  NaN  NaN
K3  NaN  NaN   C1   D1
K4   A3   B3   C2   D2
K5  NaN  NaN   C3   D3
"""
result = pd.merge(left, right, left_index=True, right_index=True, how="inner")
# print(result)
"""
     A   B   C   D
K0  A0  B0  C0  D0
K4  A3  B3  C2  D2
"""

# ==========处理overlap问题=========
boys = pd.DataFrame({"key": ["k0", "k1", "k2"],
                     "age": [1, 2, 3]})
girls = pd.DataFrame({"key": ["k0", "k0", "k3"],
                      "age": [4, 5, 6]})
# print(boys)
"""
  key  age
0  k0    1
1  k1    2
2  k2    3
"""
# print(girls)
"""
  key  age
0  k0    4
1  k0    5
2  k3    6
"""
result = pd.merge(boys, girls, on="key", suffixes=["_boy","_girl"], how="outer") # 即将相同列名分为两部分
# print(result)
"""
  key  age_boy  age_girl
0  k0      1.0       4.0
1  k0      1.0       5.0
2  k1      2.0       NaN
3  k2      3.0       NaN
4  k3      NaN       6.0
"""