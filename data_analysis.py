#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: hansvng

import pandas as pd
df = pd.read_csv("/Users/hansvng/Desktop/ZJ_20201230_0410.csv",header=0)
result = df.drop_duplicates(subset=['事项名称'],keep=False,inplace=False)
result.to_csv("/Users/hansvng/Desktop/ZJ_20201230_0410去重.csv",index=False)