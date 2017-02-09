#!/usr/bin/env python
# -*- coding: utf-8 -*-

# グラフ化に必要なものの準備
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# データの扱いに必要なライブラリ
import pandas as pd
import numpy as np
import datetime as dt

#fontfile = '/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf'
fontfile = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
fp = FontProperties(fname=fontfile, size=20)


df_sample = pd.read_csv('/home/infobio/デスクトップ/python/data/tst_pi.csv')

# dfの準備
df = df_sample.iloc[0, :]
label = df_sample.iloc[1, :]
colors=["0","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.8","0.8","0.8"]
print df
plt.pie(df,
        labels=label,
        colors=colors,
        counterclock=False,
        startangle=90,
        labeldistance=1.01,
        wedgeprops={'linewidth': 1, 'edgecolor':"white"},
        textprops={'color': "0.45", 'weight': "bold"},
        autopct="%1.0f%%"
        )
plt.axis('equal')
plt.show()
