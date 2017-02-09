#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO
import pydotplus
iris = load_iris()

print iris.data
print iris.target

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
pred = clf.predict(iris.data)
print pred

print float(sum(pred == iris.target)) / float(len(iris.target))

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

graph.write_pdf("./output/graph.pdf")
