#!/usr/bin/env python
# -*- coding: utf-8 -*-

# グラフ化に必要なものの準備
import matplotlib
import matplotlib.pyplot as plt

# データの扱いに必要なライブラリ
import numpy as np

fp = matplotlib.font_manager.FontProperties(fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",size = 17)

a = np.genfromtxt('/media/link/file/TJ/jhG/retio.tsv', dtype=float)
left = [1,2,3]
a1 = a[0,:]
a2 = a[1,:]
label = u'クラス１',u'クラス２',u'クラス３'
print a1,a2
plt.bar(left,a1,color="red",align="center")
plt.bar(left,a2,bottom=a1,color="blue",align="center",tick_label=label, fontprop=fp)

plt.show()
