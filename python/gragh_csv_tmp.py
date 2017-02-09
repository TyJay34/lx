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


df_sample = pd.read_csv("/media/link/file/TJ/jhG/ogretio.tsv",delimiter='\t',encoding="SHIFT-JIS")

# dfの準備
df = df_sample.iloc[:, 1:6]
xne = df_sample.iloc[:, 0]
print df
print len(xne)
#print df
colorlist=["#000000","#999999"]
df.plot(kind='bar', stacked=True,color=colorlist)
plt.legend(bbox_to_anchor=(0.65, 1.32),fontsize=9,prop=fp)
plt.subplots_adjust(top=0.7,left=0.15)
#plt.xticks([0,1,2],[u'クラス１',u'クラス２',u'クラス３'],fontproperties=fp,rotation=0)
plt.xticks(xrange(0,len(xne)),xne,fontproperties=fp, rotation=0)
plt.ylim(ymax=100)
plt.tick_params(labelsize=24)
plt.ylabel(u'各領域の割合（％）',fontproperties=fp)
#plt.xlabel(u'$Ｏ$－ＧｌｃＮＡｃ修飾が起こる領域',fontproperties=fp)
#plt.subplot(111).yaxis.set_major_formatter('%d %%')
#plt.show()
plt.savefig("/media/link/file/TJ/jhG/OGretio_graph.png",dpi=400, transparent=True)
