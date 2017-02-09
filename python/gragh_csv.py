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
fp = FontProperties(fname=fontfile, size=28)


df_sample = pd.read_csv('/media/link/file/TJ/jhG/kinbCP.tsv',delimiter='\t')

# dfの準備
df = df_sample.iloc[:, 1:6]
print df
#print df
colorlist=["0","0.2","0.4","0.6","1"]
df.plot(kind='bar', stacked=True,color=colorlist)
plt.legend(bbox_to_anchor=(1.25, 0.6))
plt.subplots_adjust(right=0.7)
plt.xticks([0,1,2],[u'クラス１',u'クラス２',u'クラス３'],fontproperties=fp,rotation=0)
#plt.xticks([0,1,2],['a','b','c'],fontproperties=fp)
plt.ylim(ymax=100)
plt.ylabel(u'（％）',fontproperties=fp)
plt.tick_params(labelsize=24)
#plt.show()
#fig = plt.figure()
plt.savefig("/media/link/file/TJ/jhG/graphSB.png",dpi=5000, transparent=True)
