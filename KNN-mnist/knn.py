import numpy as np
import sklearn.metrics as metrics

def knn(train, train_y, y_name, test, test_y, k):
    final = []
    dist = []
    
    for i in test:
        result1 = []
        for j in train:
            result1.append(np.sum(abs(i-j)))
            
        dist.append(result1)
    # 100x60000의 거리 구함

    
    for i in range(len(dist)):
        kindex = np.argsort(dist[i])  # 가까운 거리순으로 정렬후 원래 인덱스 반환
        kindex = kindex[:k]
        # 가까운 k개만 저장
        # 0 < kindex[i] < 60000
        W = [0]*10
        for j in range(k): 
            W[train_y[kindex[j]]] += 1 / (1 + dist[i][kindex[j]])
        # 가까운점의 레이블에 가까운점의 가중치를 합산한것을 저장
        final.append(W.index(max(W)))  # 가장 많이 나온 레이블 저장



    # k개중에 가장 투표를 많이받은것 고름
    computed, real = [],[]
    for i in range(len(test)):
        computed.append(final[i])
        real.append(int(y_name[test_y[i]]))
        print("{} {}"
              .format(final[i], y_name[test_y[i]]))
    print("accuracy = {}".format(metrics.accuracy_score(computed, real)))