from knn import knn
import numpy as np

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
# print(iris)
X = iris.data # iris data input
y = iris.target # iris target (label)
y_name = iris.target_names



train_x=np.empty((0,4), float)
train_y=np.empty((0), float)
test_x=np.empty((0,4), float)
test_y=np.empty((0), float)

n=0
for i in range(150):
    n+=1
    if n%15 !=0 or i==0:
        train_x=np.append(train_x, [X[i]], axis=0)
        train_y=np.append(train_y, [y[i]])
    else:
        test_x=np.append(test_x, [X[i]], axis=0)
        test_y=np.append(test_y, [y[i]])



knn(train_x, test_x, train_y, test_y, 3, y_name)

knn(train_x, test_x, train_y, test_y, 5, y_name)

knn(train_x, test_x, train_y, test_y, 10, y_name)

knn(train_x, test_x, train_y, test_y, 3, y_name, 1)

knn(train_x, test_x, train_y, test_y, 5, y_name, 1)

knn(train_x, test_x, train_y, test_y, 10, y_name, 1)




