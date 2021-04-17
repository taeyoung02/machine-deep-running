import numpy as np


def knn(train, test, train_y, test_y, k, y_name, weighted=False):
    final = []
    result2 = []
    for i in test:
        result1 = []
        for j in train:
            result1.append(np.sqrt(np.sum(np.power((i - j), 2))))
        result2.append(result1)
    # 거리 구함

    if weighted == False: # 가중치 적용 X인 경우
        for i in range(len(result2)):
            result2[i] = np.argsort(result2[i])  # 정렬후 원래 인덱스 반환
            result2[i] = result2[i][:k]
            # 가까운 k개만 저장

            V = [0] * (int(max(train_y)) + 1) # 빈도를 저장할 배열

            for j in result2[i]:
                V[int(train_y[j])] += 1  # 레이블 카운트
            final.append(V.index(max(V)))  # 가장 많이 나온 레이블 저장


    else:  # 가중치 적용
        for i in range(len(result2)):
            result3 = sorted(result2[i][:k])
            W = [0] * k  # 가중치 저장
            for a in range(k):
                d = result3[a]
                W[a] = 1 / (1 + np.power(d, 2)) # 가중치 계산
            result2[i] = np.argsort(result2[i])  # 정렬후 원래 인덱스 반환
            result2[i] = result2[i][:k]

            V = [0] * (int(max(train_y)) + 1)

            n = 0
            for j in result2[i]:
                V[int(train_y[j])] += W[n]  # 가중치만큼 합산
                n += 1
            final.append(V.index(max(V)))

    # k개중에 가장 투표를 많이받은것 고름

    for i in range(len(test)):
        print("Test Data Index: {}    Computed Class: {},    True class: {}"
              .format(i, y_name[int(final[i])], y_name[int(test_y[i])]))
        print('')

