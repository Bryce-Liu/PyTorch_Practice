# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 16:41
# @Author  : Bryce Liu
# @FileName: pandas_concatenate.py

import pandas as pd
import numpy as np

df_1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["a", "b", "c", "d"])
df_2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["a", "b", "c", "d"])
df_3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=["a", "b", "c", "d"])

# print(df_1)
# print(df_2)
# print(df_3)
"""
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
     a    b    c    d
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
     a    b    c    d
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
"""

# ========一般合并
# axis=0按行合并，axis=1按列合并
result = pd.concat([df_1, df_2, df_3], axis=0)
print(result)  # 注意这里的行号
"""
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
"""

# 重新编号
result = pd.concat([df_1, df_2, df_3], axis=0, ignore_index=True)
print(result)
"""
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
6  2.0  2.0  2.0  2.0
7  2.0  2.0  2.0  2.0
8  2.0  2.0  2.0  2.0
"""

# =========行号/列号不同的合并
df_4 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["a", "b", "c", "d"], index=[1, 2, 3])
df_5 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["c", "d", "e", "f"], index=[2, 3, 4])

result = pd.concat([df_4, df_5], join="outer", sort=True)  # 直接合并
print(result)
"""
     a    b    c    d    e    f
1  0.0  0.0  0.0  0.0  NaN  NaN
2  0.0  0.0  0.0  0.0  NaN  NaN
3  0.0  0.0  0.0  0.0  NaN  NaN
2  NaN  NaN  1.0  1.0  1.0  1.0
3  NaN  NaN  1.0  1.0  1.0  1.0
4  NaN  NaN  1.0  1.0  1.0  1.0
"""
result = pd.concat([df_4, df_5], join="inner",ignore_index=True)  # inner join 合并获得公共列部分
print(result)
"""
     c    d
0  0.0  0.0
1  0.0  0.0
2  0.0  0.0
3  1.0  1.0
4  1.0  1.0
5  1.0  1.0
"""

# ==========join_axes
result =pd.concat([df_4, df_5], axis=1)  # 横向合并
print(result)
"""
     a    b    c    d    c    d    e    f
1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0
"""

result =pd.concat([df_4, df_5], axis=1, join_axes=[df_4.index])  # 横向合并,以df_4.index为合并基准
print(result)
"""
     a    b    c    d    c    d    e    f
1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
"""

# =========append
df_1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["a", "b", "c", "d"])
df_2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["a", "b", "c", "d"])

result = df_1.append([df_2, df_3], ignore_index=True)
print(result)
"""
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
6  2.0  2.0  2.0  2.0
7  2.0  2.0  2.0  2.0
8  2.0  2.0  2.0  2.0
"""

# append series
s = pd.Series([1,2,3,4], index=["a","b","c","d"])
print(s)
"""
a    1
b    2
c    3
d    4
dtype: int64
"""
result = df_1.append(s, ignore_index=True)
print(result)
"""
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  2.0  3.0  4.0
"""