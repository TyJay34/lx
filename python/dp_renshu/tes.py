#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_mldata
from chainer import cuda, Variable, FunctionSet, optimizers
import chainer.functions  as F
import sys, time, math

plt.style.use('ggplot')

# 手書き数字データを描画する関数
def draw_digit(data):
    size = 28
    plt.figure(figsize=(2.5, 3))

    X, Y = np.meshgrid(range(size),range(size))
    Z = data.reshape(size,size)   # convert from vector to 28x28 matrix
    Z = Z[::-1,:]             # flip vertical
    plt.xlim(0,27)
    plt.ylim(0,27)
    plt.pcolor(X, Y, Z)
    plt.gray()
    plt.tick_params(labelbottom="off")
    plt.tick_params(labelleft="off")

    plt.show()



# Neural net architecture
def forward(x_data, y_data, train=True):
    x, t = Variable(x_data), Variable(y_data)
    y = F.dropout(F.relu(model.l1(x)),  train=train)
    x_hat  = F.dropout(model.l2(y),  train=train)
    # 誤差関数として二乗誤差関数を用いる
    return F.mean_squared_error(x_hat, t)

# 確率的勾配降下法で学習させる際の１回分のバッチサイズ
batchsize = 100

# 学習の繰り返し回数
n_epoch   = 30

# 中間層の数
n_units   = 400


# MNISTの手書き数字データのダウンロード
# #HOME/scikit_learn_data/mldata/mnist-original.mat にキャッシュされる
print 'fetch MNIST dataset'
mnist = fetch_mldata('MNIST original')

# mnist.data : 70,000件の784次元ベクトルデータ
mnist.data   = mnist.data.astype(np.float32)
mnist.data  /= 255     # 0-1のデータに変換

# mnist.target : 正解データ（教師データ）
mnist.target = mnist.target.astype(np.int32)

# 学習用データを N個、検証用データを残りの個数と設定
N = 60000
y_train, y_test = np.split(mnist.data.copy(),   [N])
N_test = y_test.shape[0]


x_train, x_test = np.split(mnist.data,   [N])

# AutoEncoderのモデルの設定
# 入力 784次元、出力 784次元, 2層
model = FunctionSet(l1=F.Linear(784, n_units),
                    l2=F.Linear(n_units, 784))


# Setup optimizer
optimizer = optimizers.Adam()
optimizer.setup(model.collect_parameters())


l1_W = []
l2_W = []

l1_b = []
l2_b = []

train_loss = []
test_loss = []
test_mean_loss = []

prev_loss = -1
loss_std = 0

loss_rate = []

# Learning loop
for epoch in xrange(1, n_epoch+1):
    print 'epoch', epoch
    start_time = time.clock()

    # training
    perm = np.random.permutation(N)
    sum_loss = 0
    for i in xrange(0, N, batchsize):
        x_batch = x_train[perm[i:i+batchsize]]
        y_batch = y_train[perm[i:i+batchsize]]

        optimizer.zero_grads()
        loss = forward(x_batch, y_batch)
        loss.backward()
        optimizer.update()

        train_loss.append(loss.data)
        sum_loss     += float(cuda.to_cpu(loss.data)) * batchsize

    print '\ttrain mean loss={} '.format(sum_loss / N)

    # evaluation
    sum_loss     = 0
    for i in xrange(0, N_test, batchsize):
        x_batch = x_test[i:i+batchsize]
        y_batch = y_test[i:i+batchsize]
        loss = forward(x_batch, y_batch, train=False)

        test_loss.append(loss.data)
        sum_loss     += float(cuda.to_cpu(loss.data)) * batchsize

    loss_val = sum_loss / N_test

    print '\ttest  mean loss={}'.format(loss_val)
    if epoch == 1:
        loss_std = loss_val
        loss_rate.append(100)
    else:
        print '\tratio :%.3f'%(loss_val/loss_std * 100)
        loss_rate.append(loss_val/loss_std * 100)

    if prev_loss >= 0:
        diff = loss_val - prev_loss
        ratio = diff/prev_loss * 100
        print '\timpr rate:%.3f'%(-ratio)

    prev_loss = sum_loss / N_test
    test_mean_loss.append(loss_val)

    l1_W.append(model.l1.W)
    l2_W.append(model.l2.W)
    end_time = time.clock()
    print "\ttime = %.3f" %(end_time-start_time)


draw_digit(mnist.data[5])
draw_digit(mnist.data[12345])
draw_digit(mnist.data[33456])
