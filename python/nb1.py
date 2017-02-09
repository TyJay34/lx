#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import sklearn

class NaiveBayes1(object):
    def __init__(self):

        self.pY_ = None
        self.pXgY_ = None

    def fit(self, X, y):
        #fit model
        n_samples = X.shape[0]
        n_features = X.shape[1]
        n_classes = 2
        n_fvalues = 2

        #事例数と暮らすラベルの数が違うとえら
        if n_samples != len(y):
            raise ValueError('Mismatched number of samples. ^^; ')

        #クラスラベルがｙである事例数
        nY = np.zeros(n_classes, dtype = int)
        for i in xrange(n_samples):
            nY[y[i]] += 1

        #モデルパラメータself.pY_ の計算
        self.pY_ = np.empty(n_classes, dtype=float)
        for i in xrange(n_classes):
            self.pY_[i] = nY[i] / float(n_samples)

        #特徴の分布のパラメータn
        nXY = np.zeros((n_features, n_fvalues, n_classes), dtype=int)
        for i in xrange(n_samples):
            for j in xrange(n_features):
                nXY[j, X[i,j], y[i]] += 1

        #モデルパラメータself.pXgY_の計算
        self.pXgY_ = np.empty((n_features, n_fvalues, n_classes), dtype=float)
        for j in xrange(n_features):
            for xi in xrange(n_fvalues):
                for yi in xrange(n_classes):
                    self.pXgY_[j,xi,yi] = nXY[j, xi, yi] / float(nY[yi])


    def predict(self, X):
        #predict class
        n_samples = X.shape[0]
        n_features = X.shape[1]

        y = np.empty(n_samples, dtype=int)

        for i, xi in enumerate(X):
            logpXY = np.log(self.pY_) + \
            np.sum(np.log(self.pXgY_[np.arange(n_features), xi, :]),
                   axis=0)

            y[i] = np.argmax(logpXY)

        return y
