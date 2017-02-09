#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
#import sklearn
from nb1 import NaiveBayes1

data = np.genfromtxt('/media/link/file/TJ/neuro/all5_hai.tsv', dtype=int)

X = data[:, 1:]
y = data[:, 1]

clr = NaiveBayes1()
clr.fit(X[200:],y[200:])

predict_y = clr.predict(X[:200 :])
sk = 0
hzr = 0
for i in xrange(200):
    print i , y[i] , predict_y[i]
    if y[i] == predict_y[i]:
        sk += 1
    else:
        hzr += 1
print float(sk) / float(sk + hzr)
