# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 14:57
# @Author  : Bryce Liu
# @FileName: choose_data.py

import pandas as pd
import numpy as np

dates = pd.date_range('20190701', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=["A", "B", "C", "D"])
# print(df)
"""
             A   B   C   D
2019-07-01   0   1   2   3
2019-07-02   4   5   6   7
2019-07-03   8   9  10  11
2019-07-04  12  13  14  15
2019-07-05  16  17  18  19
2019-07-06  20  21  22  23
"""
# print(type(df["A"].values))
# for i in df["A"].values:
#     print(i)
print(df.iloc[0])
# df.iloc[3,0]=8
# print(df)
# print(df[df["A"]==8].sort_values(by=["B"],ascending=False))

# ========选择一列
# print(df["A"])
# print(df.A)  # 两种方法结果一致
"""
2019-07-01     0
2019-07-02     4
2019-07-03     8
2019-07-04    12
2019-07-05    16
2019-07-06    20
Freq: D, Name: A, dtype: int64
"""

# ========列的切片
# print(df[0:2])
"""
            A  B  C  D
2019-07-01  0  1  2  3
2019-07-02  4  5  6  7
"""
# print(df['20190705':"20190706"])
"""
             A   B   C   D
2019-07-05  16  17  18  19
2019-07-06  20  21  22  23
"""

# ========以标签选择
# print(df.loc['20190703'])
"""
A     8
B     9
C    10
D    11
Name: 2019-07-03 00:00:00, dtype: int64
"""
# print(df.loc[:, ["A", "B"]])  # 二维选择
"""
             A   B
2019-07-01   0   1
2019-07-02   4   5
2019-07-03   8   9
2019-07-04  12  13
2019-07-05  16  17
2019-07-06  20  21
"""
# print(df.loc["20190704", ["A", "B"]])  # 二维选择
"""
A    12
B    13
Name: 2019-07-04 00:00:00, dtype: int64
"""

# =========以index选择
# print(df.iloc[3, 1])
# 13
# print(df.iloc[3:5, 1:3])
"""
             B   C
2019-07-04  13  14
2019-07-05  17  18
"""

# ==========值比较的筛选
# print(df[df.A>8])
"""
             A   B   C   D
2019-07-04  12  13  14  15
2019-07-05  16  17  18  19
2019-07-06  20  21  22  23
"""