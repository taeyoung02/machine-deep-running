
#!/usr/bin/env python
# coding: utf-8

# In[20]:


from knn import knn


# In[1]:


import sys, os
sys.path.append(os.pardir)


# In[2]:


import numpy as np
from dataset.mnist import load_mnist


# In[3]:


from PIL import Image


# In[4]:


(x_train, t_train), (x_test, t_test) =     load_mnist(flatten=True, normalize=False)
# training data, test data
# flatten: 이미지를 1차원 배열로 읽음
# normalize: 0~1 실수로. 그렇지 않으면 0~255 
image = x_train[0]
label = t_train[0]
# 첫번째 데이터
print(label)
print(image.shape)


# In[38]:


x_train


# In[39]:


t_train


# In[35]:


x_train = x_train.astype(int)


# In[36]:


t_train = t_train.astype(int)


# In[37]:


t_test = t_test.astype(int)
x_test = x_test.astype(int)


# In[7]:


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()
# image를 unsigned int로
image = image.reshape(28,28)
# 1차원 —> 2차원 (28x28)
print(image.shape)
img_show(image)


# In[40]:


len(x_train), x_train.shape


# In[41]:


len(t_train)


# In[80]:


size = 100
test_x,test_y=[],[]

sample = np.random.randint(0, t_test.shape[0], size)
for i in sample:
    test_x.append(x_test[i])
    test_y.append(t_test[i])


# In[81]:


len(test_x[0])


# In[211]:


import numpy as np






label_name = ['0','1','2','3','4','5','6','7','8','9']


# In[135]:


import time


# In[138]:


start = time.time()
knn(x_train,t_train,label_name,test_x,test_y, 3)
end = time.time()


# In[139]:


print(end-start)


# In[136]:


start = time.time()
knn(x_train,t_train,label_name,test_x,test_y, 5)
end = time.time()


# In[137]:


print(end-start)


# In[140]:


start = time.time()
knn(x_train,t_train,label_name,test_x,test_y, 10)
end = time.time()


# In[141]:


print(end-start)


# # PCA 주성분 분석

# In[88]:


from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt


# In[119]:


len(x_train), len(test_x)


# In[170]:


data = np.concatenate((x_train, test_x), axis=0) # 훈련에 사용할 feature 연결


# In[151]:


pca = PCA(random_state=1107)
X_p = pca.fit_transform(data)

import pandas as pd
v_ratio = pd.Series(np.cumsum(pca.explained_variance_ratio_)) # 누적 분산을 나타냄


# In[157]:


v_ratio


# In[156]:


# 분산량이 90%에 해당하는 지점이 86번째 주성분값
count=0
for i in v_ratio:
    if i > 0.9:
        print(count)
        break
    count+=1


# In[171]:


#StandardScaler() = 데이터를 조정하여 평균을0, 분산을 1로만들음

# Create pipeline: pipeline
pca=PCA(n_components=87)# 87개의 차원만 보기

# 연속된 변환을 순서대로 처리할 수 있도록 도와주는 pipeline
pipeline = make_pipeline(StandardScaler(),pca)
print(pipeline)
# Fit the pipeline to 'samples'


# In[172]:


pipeline.fit(data) # pipeline 적용


features = [i for i in range(87)]
plt.bar(features, pca.explained_variance_)#분산(정보량) 분석
plt.xlabel('PCA feature')
plt.ylabel('variance')
plt.xticks(range(pca.n_components_))#xticks 눈금 조정. 여기서 정수0~9까지가 눈금
plt.show()


# In[186]:


data = StandardScaler().fit_transform(data)
pca = PCA(n_components=87) # 주성분을 10개로 결정

principalComponents = pca.fit_transform(data) #주성분을 10개로 맞춤
principalDf = pd.DataFrame(data=principalComponents, columns =                            ["principle component" + str(i) for i in range(87)])


# In[187]:


principalDf.head()


# In[188]:


pca.explained_variance_ratio_  # 각 주성분이 가진 분산


# In[189]:


x_train2 = principalDf[:len(x_train)] # 다시 데이터 분할
x_test2 = principalDf[len(x_train):]


# In[190]:


x_train2


# In[191]:


x_test2


# In[193]:


x_train2.values


# In[214]:


start = time.time()
knn(x_train2.values,t_train,label_name,x_test2.values,test_y, 3)
end = time.time()


# In[215]:


print(end-start)


# In[216]:


start = time.time()
knn(x_train2.values,t_train,label_name,x_test2.values,test_y, 5)
end = time.time()


# In[217]:


print(end-start)


# In[218]:


start = time.time()
knn(x_train2.values,t_train,label_name,x_test2.values,test_y, 10)
end = time.time()


# In[219]:


print(end-start)




