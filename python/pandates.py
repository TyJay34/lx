#!/usr/bin/env python
# -*- coding: utf-8 -*-

# グラフ化に必要なものの準備
import matplotlib
import matplotlib.pyplot as plt

# データの扱いに必要なライブラリ
import pandas as pd
import numpy as np


fontprop = matplotlib.font_manager.FontProperties(fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",size = 17)

#plt.style.use('ggplot')
#font = {'family' : 'meiryo'}
#matplotlib.rc('font', **font)

# dfの準備
df = pd.DataFrame([2,1.368,3.32,1.44,2.12,5.62,1.57,1.44,1.4])

df.plot(kind='bar',color='grey')
#plt.legend(prop = fontprop, loc = 'upper left')
#plt.legend('')
plt.xticks([0,1,2,3,4,5,6,7,8],['1-1','1-2','1-3','2-1','2-2','2-3','3-1','3-2','3-3'],rotation=0,size = 18)
plt.yticks(size = 18)

#plt.grid(which='major',color='black',linestyle='-')
plt.ylabel(u'$O$-GlcNAc修飾残基の数',fontproperties=fontprop )
plt.legend([],frameon=False)

#plt.show()
plt.savefig("/media/link2/file/TJ/graphasdf.png", dpi=600, transparent=True)

#ax = df.plot.bar(y=[u'個数'], alpha=0.6, figsize=(12,3), stacked=False, cmap='autumn')
#plt.title(u'積み上げ型の棒グラフ',fontdict = {"fontproperties" : fontprop}, size=16)
#fig = ax.get_figure()
#plt.show
#fig.savefig("example.png", dpi=600)
