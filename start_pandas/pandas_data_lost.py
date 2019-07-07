# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 15:57
# @Author  : Bryce Liu
# @FileName: pandas_data_lost.py

import pandas as pd
import numpy as np

dates = pd.date_range('20190701', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=["A", "B", "C", "D"])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)
"""
             A     B     C   D
2019-07-01   0   NaN   2.0   3
2019-07-02   4   5.0   NaN   7
2019-07-03   8   9.0  10.0  11
2019-07-04  12  13.0  14.0  15
2019-07-05  16  17.0  18.0  19
2019-07-06  20  21.0  22.0  23
"""

# ========丢掉含有NaN的行/列
print(df.dropna(axis=0, how="any"))
# how=["any","all"]
# all表示当所有data都等于NaN时才丢弃本列/行
"""
             A     B     C   D
2019-07-03   8   9.0  10.0  11
2019-07-04  12  13.0  14.0  15
2019-07-05  16  17.0  18.0  19
2019-07-06  20  21.0  22.0  23
"""
print(df.dropna(axis=1, how="any"))
"""
             A   D
2019-07-01   0   3
2019-07-02   4   7
2019-07-03   8  11
2019-07-04  12  15
2019-07-05  16  19
2019-07-06  20  23
"""

# ========补充NaN位置的数据
print(df.fillna(value="hh"))
"""
             A   B   C   D
2019-07-01   0  hh   2   3
2019-07-02   4   5  hh   7
2019-07-03   8   9  10  11
2019-07-04  12  13  14  15
2019-07-05  16  17  18  19
2019-07-06  20  21  22  23
"""

# =========检查数据的确实与否
print(df.isnull())
"""
                A      B      C      D
2019-07-01  False   True  False  False
2019-07-02  False  False   True  False
2019-07-03  False  False  False  False
2019-07-04  False  False  False  False
2019-07-05  False  False  False  False
2019-07-06  False  False  False  False
"""
print(np.any(df.isnull()) == True)  # 如果数据中有NaN则返回True
# True
