# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 16:24
# @Author  : Bryce Liu
# @FileName: import_export.py

import pandas as pd

data = pd.read_csv("students.csv")
# print(data)
"""
   Student ID   name  age  gender
0       10000   Mike   17    male
1       10001   Jack   16    male
2       10002  Marry   16  female
3       10003  Alice   18  female
4       10004   Rose   17  female
5       10005    Bob   18    male
"""
# data.to_pickle("student.pickle")
# print(data.values)
data.to_csv("export_data.csv")