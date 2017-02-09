#!/usr/bin/env python
# -*- coding: utf-8 -*-
# グラフ化に必要なものの準備
import matplotlib
import matplotlib.pyplot as plt

# データの扱いに必要なライブラリ
import pandas as pd
import numpy as np


a = pd.read_csv('/media/link/file/TJ/tabtest.tsv',delimiter='\t')
df  = a.iloc[:,:]

print df
