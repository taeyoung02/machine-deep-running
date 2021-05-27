#!/usr/bin/env python
# coding: utf-8

# In[192]:

from sklearn.preprocessing import StandardScaler, RobustScaler
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import confusion_matrix


from sklearn.metrics import roc_auc_score

from keras import backend as K
from sklearn.metrics import classification_report

from keras import models, layers
from keras import optimizers
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import regularizers
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import RandomOverSampler

from sklearn.metrics import roc_curve






''' #############################데이터 불러오기############################ '''


train = pd.read_csv('C:\\Users\\com\\Downloads\\data\\X_train.csv')
test = pd.read_csv('C:\\Users\\com\\Downloads\\data\\X_test.csv')
y_train = pd.read_csv('C:\\Users\\com\\Downloads\\data\\y_train.csv')
y_test =  pd.read_csv('C:\\Users\\com\\Downloads\\data\\y_test.csv')

val = pd.read_csv('C:\\Users\\com\\Downloads\\data\\validation.csv')


''' #############################데이터 분석 ##############################'''


'''
val = val.iloc[:,1:]


y_train


y_train=y_train.iloc[:,1:]
y_test = y_test.iloc[:,1:]


y_test


train["mark"] = 2
val["mark"] = 1
test["mark"]=0


train = train.iloc[:,1:]
test = test.iloc[:,1:]



train["class"] = y_train
test["class"] = y_test



data = pd.concat([train, test, val], axis=0, ignore_index=True)



'''
#val도 필요하다면 
y_train=y_train.iloc[:,1:]
y_test = y_test.iloc[:,1:]

train["mark"] = 1
test["mark"]=0

train = train.iloc[:,1:]
test = test.iloc[:,1:]
val = val.iloc[:,1:]

train["class"] = y_train
test["class"] = y_test


data = pd.concat([train, test], axis=0, ignore_index=True)

# 여기까지 위에거 덮어쓰시고 아래도 추가해주시면 됩니다. 아래에도 두부분을 수정해줄 필요있음. 표시해놨어요

data.iloc[:,2]



data.describe()



fig, ax = plt.subplots(1, 2, figsize=(18,4))

amount_val = data['Amount'].values
time_val = data['Time'].values

sns.distplot(amount_val, ax=ax[0], color='r')
ax[0].set_title('Distribution of Transaction Amount', fontsize=14)
ax[0].set_xlim([min(amount_val), max(amount_val)])

sns.distplot(time_val, ax=ax[1], color='b')
ax[1].set_title('Distribution of Transaction Time', fontsize=14)
ax[1].set_xlim([min(time_val), max(time_val)])



plt.show()


# In[211]:



data['scaled_amount'] = RobustScaler().fit_transform(data['Amount'].values.reshape(-1,1))
data['scaled_time'] = RobustScaler().fit_transform(data['Time'].values.reshape(-1,1))
data.drop(['Time','Amount'], axis=1, inplace=True)
'''

# In[212]:


fig, ax = plt.subplots(1, 2, figsize=(18,4))

amount_val = data['scaled_amount'].values
time_val = data['scaled_time'].values

sns.distplot(amount_val, ax=ax[0], color='r')
ax[0].set_title('Distribution of Transaction Amount', fontsize=14)
ax[0].set_xlim([min(amount_val), max(amount_val)])

sns.distplot(time_val, ax=ax[1], color='b')
ax[1].set_title('Distribution of Transaction Time', fontsize=14)
ax[1].set_xlim([min(time_val), max(time_val)])

'''

plt.boxplot(data['scaled_amount'],sym="bo")  

unique, counts = np.unique(y_train, return_counts =True)
class_dic = dict(zip(unique, counts))

x =np.arange(2)
plt.bar(x,counts)
plt.xticks(x, unique)
plt.show()






# In[215]:


corr = data.corr(method='pearson')


# In[216]:


abs(corr["class"]).sort_values(ascending=False)


# In[217]:


def outliers(y): 
    f, axes = plt.subplots(ncols=1, figsize=(15,8))
    
    sns.boxplot(x="class", y=y, data=data, ax=axes)
    axes.set_title(y)


# In[218]:

outliers("V22") 
outliers("V17")
outliers("V14")
outliers("V12")
outliers("V10")
outliers("V16")
outliers("V3")
outliers("V7")
outliers("V11")
outliers("V4")
outliers("V18")
outliers("V9")
outliers("V1")
outliers("V5")
outliers("V2")


# In[219]:


outliers("V22") # 상관계수가 낮음. class에 따른 특징이 안나타남



'''#######################데이터 가공 ############################## '''
# In[220]:




# In[221]:


def remove_outliers(y): 
    target = data[data['class']==0][y]
    quan25 = np.percentile(target.values, 25)
    quan75 = np.percentile(target.values, 75)
    
    iqr = quan75-quan25
    iqr = iqr*1.5
    low = quan25 - iqr
    high = quan75 + iqr
    outlier = target[(target<low) | (target>high)].index
    print("outlier 개수 = {}".format(len(outlier)))
    data.drop(outlier, axis=0, inplace=True)
    print(data.shape)
    return


# In[222]:


remove_outliers("V17")


# In[223]:


remove_outliers("V14")
remove_outliers("V12")
remove_outliers("V10")
remove_outliers("V16")
remove_outliers("V3")
remove_outliers("V7")
remove_outliers("V11")
remove_outliers("V4")
remove_outliers("V18")
remove_outliers("V9")
remove_outliers("V1")
remove_outliers("V5")
remove_outliers("V2")




'''
# # 데이터 다시 나누기

# In[224]:


train = data[data["mark"] == 2]
val = data[data["mark"] == 1]
test = data[data["mark"] == 0]

'''
#val도 이상치 제거할경우 위와 바꾸기.
train = data[data["mark"] == 1]
test = data[data["mark"] == 0]



y_train = train["class"]
y_test = test["class"]
y_val =val["class"]


train.drop(['class'], axis=1, inplace=True) # 다시 split함
test.drop(['class'], axis=1, inplace=True)
val.drop(['class'], axis=1, inplace=True)

train.drop(['mark'], axis=1, inplace=True)
test.drop(['mark'], axis=1, inplace=True)
#val.drop(['class'], axis=1, inplace=True)   val도 이상치 제거할경우추가 이게 끝.



X_train=train
X_test=test
X_val=val


# In[232]:


X_train


# In[233]:


X_test

#정규화
def MMnormalize(x_train,x_test):
    max1 = np.max(x_train,axis=0)
    max2 = np.max(x_test,axis=0)
    max = np.append(max1, max2, axis=0)
    max = max.reshape(2,30)
    max = np.max(max,axis=0)
    
    min1 = np.min(x_train,axis=0)
    min2 = np.min(x_test,axis=0)
    min = np.append(min1, min2, axis=0)
    min = min.reshape(2,30)
    min = np.min(min,axis=0)

    nor_train = (x_train - min)/(max - min)
    nor_test = (x_test - min)/(max - min)

    return nor_train , nor_test



X_train , X_test = MMnormalize(train,test)
# val도 정규화?
# garbage , X_val = MMnormalize(train,val)


#oversampling

X_train, y_train = RandomOverSampler(random_state=0).fit_resample(X_train, y_train)
X_train, y_train = SMOTE(random_state=0).fit_resample(X_train, y_train)


'''############################# 모델 구현 #############################'''

'''
# In[235]:


lr = LogisticRegression()


# In[236]:


lr.fit(X_train, y_train)


# In[237]:


predicted = lr.predict(X_test)


# In[238]:


len([i for i in y_test if i==1])


# In[239]:



# In[240]:


cf = confusion_matrix(y_test, predicted)


# In[241]:


cf


# In[287]:

print('Logistic Regression: ', roc_auc_score(y_test, predicted))


# In[290]:





print('Logistic Regression:')
print(classification_report(y_test, predicted))

'''
# In[251]:


def recall(y_target, y_pred):
    # clip(t, clip_value_min, clip_value_max) : clip_value_min~clip_value_max 이외 가장자리를 깎아 낸다
    # round : 반올림한다
    y_target_yn = K.round(K.clip(y_target, 0, 1)) # 실제값을 0(Negative) 또는 1(Positive)로 설정한다
    y_pred_yn = K.round(K.clip(y_pred, 0, 1)) # 예측값을 0(Negative) 또는 1(Positive)로 설정한다

    # True Positive는 실제 값과 예측 값이 모두 1(Positive)인 경우이다
    count_true_positive = K.sum(y_target_yn * y_pred_yn) 

    # (True Positive + False Negative) = 실제 값이 1(Positive) 전체
    count_true_positive_false_negative = K.sum(y_target_yn)

    # Recall =  (True Positive) / (True Positive + False Negative)
    # K.epsilon()는 'divide by zero error' 예방차원에서 작은 수를 더한다
    recall = count_true_positive / (count_true_positive_false_negative + K.epsilon())

    # return a single tensor value
    return recall


# In[252]:




# In[279]:


model = models.Sequential()
model.add(layers.Dense(30, activation = 'relu', input_shape = (30,)))
model.add(layers.Dense(30, activation = 'relu'))
model.add(layers.Dense(30, activation = 'relu'))
model.add(layers.Dense(1, activation='sigmoid'))


# In[280]:


model.compile(optimizer='rmsprop',
             loss='binary_crossentropy',
             metrics=['accuracy', recall])


# In[281]:


x_train = np.asarray(X_train).astype('float32').reshape((-1,30))
x_val = np.asarray(X_val).astype('float32').reshape((-1,30))
y_train = np.asarray(y_train).astype('float32').reshape((-1,1))
y_val = np.asarray(y_val).astype('float32').reshape((-1,1))


# In[282]:


y_train.shape


# In[308]:





# In[350]:


es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=15)


# In[351]:


history = model.fit(x_train,
                   y_train,
                   epochs=100,
                   batch_size=len(y_train)//10,
                    callbacks=[es],
                   validation_data = (x_val, y_val))


# In[352]:





history_dict = history.history
loss = history_dict['loss']
val_loss = history_dict['val_loss']



epochs = range(1, len(loss) + 1)



plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('loss')
plt.legend()



plt.show()


# In[353]:





history_dict = history.history
loss = history_dict['recall']
val_loss = history_dict['val_recall']



epochs = range(1, len(loss) + 1)



plt.plot(epochs, loss, 'bo', label='Training recall')
plt.plot(epochs, val_loss, 'b', label='Validation recall')
plt.title('Training and validation recall')
plt.xlabel('Epochs')
plt.ylabel('recall')
plt.legend()



plt.show()


# In[354]:



# In[355]:


model2 = models.Sequential()
model2.add(layers.Dense(30, kernel_regularizer=regularizers.l2(0.001), activation = 'relu', input_shape = (30,)))
model2.add(layers.Dense(30, kernel_regularizer=regularizers.l2(0.001), activation = 'relu'))
model2.add(layers.Dense(30, kernel_regularizer=regularizers.l2(0.001), activation = 'relu'))
model2.add(layers.Dense(1, activation='sigmoid'))


# In[356]:


model2.compile(optimizer='rmsprop',
             loss='binary_crossentropy',
             metrics=['accuracy', recall])


# In[357]:


history2 = model2.fit(x_train,
                   y_train,
                   epochs=100,
                   batch_size=len(y_train)//10,
                      callbacks=[es],
                   validation_data = (x_val, y_val))


# In[358]:




history_dict = history2.history
loss = history_dict['loss']
val_loss = history_dict['val_loss']



epochs = range(1, len(loss) + 1)



plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('loss')
plt.legend()



plt.show()


# In[359]:


history_dict = history2.history
loss = history_dict['recall']
val_loss = history_dict['val_recall']



epochs = range(1, len(loss) + 1)



plt.plot(epochs, loss, 'bo', label='Training recall')
plt.plot(epochs, val_loss, 'b', label='Validation recall')
plt.title('Training and validation recall')
plt.xlabel('Epochs')
plt.ylabel('recall')
plt.legend()



plt.show()


# In[364]:


model3= models.Sequential()
model3.add(layers.Dense(30, kernel_regularizer=regularizers.l2(0.001), activation = 'relu', input_shape = (30,)))
model3.add(layers.Dense(30, kernel_regularizer=regularizers.l2(0.001), activation = 'relu'))
model3.add(layers.Dense(30, kernel_regularizer=regularizers.l2(0.001), activation = 'relu'))
model3.add(layers.Dense(1, activation='sigmoid'))


# In[365]:


model3.compile(optimizer='Adam',
             loss='binary_crossentropy',
             metrics=['accuracy', recall])


# In[366]:


history3 = model3.fit(x_train,
                   y_train,
                   epochs=40,
                   batch_size=len(y_train)//10,
                      callbacks=[es],
                   validation_data = (x_val, y_val))


# In[367]:


history_dict = history3.history
loss = history_dict['loss']
val_loss = history_dict['val_loss']



epochs = range(1, len(loss) + 1)



plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('loss')
plt.legend()



plt.show()


# In[368]:


history_dict = history3.history
loss = history_dict['recall']
val_loss = history_dict['val_recall']



epochs = range(1, len(loss) + 1)



plt.plot(epochs, loss, 'bo', label='Training recall')
plt.plot(epochs, val_loss, 'b', label='Validation recall')
plt.title('Training and validation recall')
plt.xlabel('Epochs')
plt.ylabel('recall')
plt.legend()



plt.show()


# In[369]:


predict1=model.predict(X_test)


# In[370]:


roc_auc_score(y_test, predict1)


# In[371]:


predict2= model2.predict(X_test)


# In[372]:


roc_auc_score(y_test, predict2)


# In[373]:


predict3= model3.predict(X_test)


# In[374]:


roc_auc_score(y_test, predict3)


# In[385]:


def labeling(x): # 시그모이드 적용
    X=[]
    for i in x:
        if i<0.5:
            X.append(0)
        else:
            X.append(1)
    return X


# In[388]:


p1 = labeling(predict1)
p2 = labeling(predict2)
p3 = labeling(predict3)


# In[419]:


print(classification_report(y_test, p1))


# In[420]:


print(classification_report(y_test, p2))


# In[421]:


print(classification_report(y_test, p3))


# In[410]:


def plot_roc_curve(test_y, model_probs1,model_probs2, model_probs3,clf_name1, clf_name2, clf_name3):
    # plot naive skill roc curve
    fpr, tpr, _ = roc_curve(test_y, model_probs1)
    plt.plot(fpr, tpr, marker='.', label=clf_name1)
    
    fpr, tpr, _ = roc_curve(test_y, model_probs2)
    plt.plot(fpr, tpr, marker='.', label=clf_name2)
    
    fpr, tpr, _ = roc_curve(test_y, model_probs3)
    plt.plot(fpr, tpr, marker='.', label=clf_name3)
    # axis labels
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    # show the legend
    plt.legend()
    # show the plot
    plt.show()


# In[411]:

# In[413]:


plot_roc_curve(y_test, p1,p2,p3 ,"model1", "model2", "model3")


# In[414]:


confusion_matrix(y_test,p1)


# In[415]:


confusion_matrix(y_test,p2)


# In[416]:


confusion_matrix(y_test,p3)


# In[ ]:




