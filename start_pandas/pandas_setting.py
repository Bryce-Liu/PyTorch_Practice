# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 15:43
# @Author  : Bryce Liu
# @FileName: pandas_setting.py

import pandas as pd
import numpy as np

dates = pd.date_range('20190701', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=["A", "B", "C", "D"])
print(df)
"""
             A   B   C   D
2019-07-01   0   1   2   3
2019-07-02   4   5   6   7
2019-07-03   8   9  10  11
2019-07-04  12  13  14  15
2019-07-05  16  17  18  19
2019-07-06  20  21  22  23
"""

# =========iloc修改数据
df.iloc[2, 2] = 1111
print(df)
"""
             A   B     C   D
2019-07-01   0   1     2   3
2019-07-02   4   5     6   7
2019-07-03   8   9  1111  11
2019-07-04  12  13    14  15
2019-07-05  16  17    18  19
2019-07-06  20  21    22  23
"""

# =========loc修改数据
df.loc["20190704", "B"] = 2222
print(df)
"""
             A     B     C   D
2019-07-01   0     1     2   3
2019-07-02   4     5     6   7
2019-07-03   8     9  1111  11
2019-07-04  12  2222    14  15
2019-07-05  16    17    18  19
2019-07-06  20    21    22  23
"""

# =========值比较的筛选与修改
print(df.A > 4)
"""
2019-07-01    False
2019-07-02    False
2019-07-03     True
2019-07-04     True
2019-07-05     True
2019-07-06     True
Freq: D, Name: A, dtype: bool
"""
print(df.A[df.A > 4])  # 可以实现部分修改数据
"""
2019-07-03     8
2019-07-04    12
2019-07-05    16
2019-07-06    20
Freq: D, Name: A, dtype: int64
"""
df[df.A > 4] = "hhh"
print(df)
"""
              A    B    C    D
2019-07-01    0    1    2    3
2019-07-02    4    5    6    7
2019-07-03  hhh  hhh  hhh  hhh
2019-07-04  hhh  hhh  hhh  hhh
2019-07-05  hhh  hhh  hhh  hhh
2019-07-06  hhh  hhh  hhh  hhh
"""

# ==========数据新增
df["F"] = np.nan  # 新增空数据
print(df)
"""
              A    B    C    D   F
2019-07-01    0    1    2    3 NaN
2019-07-02    4    5    6    7 NaN
2019-07-03  hhh  hhh  hhh  hhh NaN
2019-07-04  hhh  hhh  hhh  hhh NaN
2019-07-05  hhh  hhh  hhh  hhh NaN
2019-07-06  hhh  hhh  hhh  hhh NaN
"""

df["E"] = pd.Series([1, 2, 3, 4, 5, 6], index=dates)  # 添加指定数据
print(df)
"""
              A    B    C    D   F  E
2019-07-01    0    1    2    3 NaN  1
2019-07-02    4    5    6    7 NaN  2
2019-07-03  hhh  hhh  hhh  hhh NaN  3
2019-07-04  hhh  hhh  hhh  hhh NaN  4
2019-07-05  hhh  hhh  hhh  hhh NaN  5
2019-07-06  hhh  hhh  hhh  hhh NaN  6
"""
