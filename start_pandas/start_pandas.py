# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 11:39
# @Author  : Bryce Liu
# @FileName: start_pandas.py

import pandas as pd
import numpy as np

# =========序列
s = pd.Series([1, 3, 4, np.nan, 44, 1])
print(s)
"""
0     1.0
1     3.0
2     4.0
3     NaN
4    44.0
5     1.0
dtype: float64
"""

# ==========日期序列
dates = pd.date_range('20190101', periods=6)
print(dates)
"""
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-05', '2019-01-06'],
              dtype='datetime64[ns]', freq='D')
"""

# ===========默认行列
df_default = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df_default)  # 以数字命名行列标题
"""
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
"""

# ==========定义行列的名称
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=["a", "b", "c", "d"])
print(df)
"""
                   a         b         c         d
2019-01-01  1.058925 -0.556034  0.281601  1.131573
2019-01-02  1.352189  1.516104  0.438753 -0.294522
2019-01-03  0.498826 -0.117144  1.184877  1.190517
2019-01-04  0.804679  0.685127  0.357882 -0.407962
2019-01-05  0.381283  0.503775 -0.427989  0.537228
2019-01-06 -0.676476  1.851026 -0.126164  0.275436
"""

# ==========字典定义DataFrame
df_dict = pd.DataFrame({"A": 1.,
                        "B": pd.Timestamp("20190101"),
                        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                        "D": np.array([3] * 4, dtype='int32'),
                        "E": pd.Categorical(["test", "train", "test", "train"]),
                        "F": "foo"})
print(df_dict)
"""
     A          B    C  D      E    F
0  1.0 2019-01-01  1.0  3   test  foo
1  1.0 2019-01-01  1.0  3  train  foo
2  1.0 2019-01-01  1.0  3   test  foo
3  1.0 2019-01-01  1.0  3  train  foo
"""

# ===========打印数据格式
print(df_dict.dtypes)
"""
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
"""

# ===========打印数据行号
print(df_dict.index)
# Int64Index([0, 1, 2, 3], dtype='int64')

# ===========打印列号
print(df_dict.columns)
# Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')

# ===========只打印数据
print(df_dict.values)
"""
[[1.0 Timestamp('2019-01-01 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2019-01-01 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2019-01-01 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2019-01-01 00:00:00') 1.0 3 'train' 'foo']]
"""

# ============描述dataframe
print(df_dict.describe())
"""
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
"""

# ============数据转制
print(df_dict.T)
"""
                     0  ...                    3
A                    1  ...                    1
B  2019-01-01 00:00:00  ...  2019-01-01 00:00:00
C                    1  ...                    1
D                    3  ...                    3
E                 test  ...                train
F                  foo  ...                  foo
"""

# ============数据排序
print(df_dict.sort_index(axis=1, ascending=False))  # axis=1按列排序
"""
[6 rows x 4 columns]
     F      E  D    C          B    A
0  foo   test  3  1.0 2019-01-01  1.0
1  foo  train  3  1.0 2019-01-01  1.0
2  foo   test  3  1.0 2019-01-01  1.0
3  foo  train  3  1.0 2019-01-01  1.0
"""
print(df_dict.sort_index(axis=0, ascending=False))  # axis=0按行排序
"""
     A          B    C  D      E    F
3  1.0 2019-01-01  1.0  3  train  foo
2  1.0 2019-01-01  1.0  3   test  foo
1  1.0 2019-01-01  1.0  3  train  foo
0  1.0 2019-01-01  1.0  3   test  foo
"""
print(df_dict.sort_values(by="E"))  # 数据按E列排序
"""
     A          B    C  D      E    F
0  1.0 2019-01-01  1.0  3   test  foo
2  1.0 2019-01-01  1.0  3   test  foo
1  1.0 2019-01-01  1.0  3  train  foo
3  1.0 2019-01-01  1.0  3  train  foo
"""