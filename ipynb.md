```python
import pandas as pd
kt = pd.read_excel('C:/Users/dhrms/Downloads/charge.xlsx', encoding='EUC-KR')
```


```python
#Importing libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# Input data files are available in the "../input/" directory.
import os
import matplotlib.pyplot as plt#visualization
from PIL import  Image
%matplotlib inline
import pandas as pd
import seaborn as sns#visualization
import itertools
import warnings
import io
import plotly.offline as py#visualization
py.init_notebook_mode(connected=True)#visualization
import plotly.graph_objs as go#visualization
import plotly.tools as tls#visualization
import plotly.figure_factory as ff#visualization
import plotly.express as px
```


<script type="text/javascript">
window.PlotlyConfig = {MathJaxConfig: 'local'};
if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}
if (typeof require !== 'undefined') {
require.undef("plotly");
requirejs.config({
    paths: {
        'plotly': ['https://cdn.plot.ly/plotly-latest.min']
    }
});
require(['plotly'], function(Plotly) {
    window._Plotly = Plotly;
});
}
</script>




```python
import matplotlib
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()
# font_location = '/usr/share/fonts/truetype/nanum/NanumGothicOTF.ttf'
font_location = 'C:/Users/dhrms/Downloads/NanumFontSetup_TTF_SQUARE_ROUND/NanumSquareRoundEB.ttf' # For Windows
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

%matplotlib inline

```


```python
kt.isnull().sum()
```




    서비스계약ID               0
    계약자명(가입자명)            0
    서비스번호(TRIM)           0
    개통일(준공일)              0
    해지일                   0
    모상품명                  0
    요금항목명                 0
    청구일자                  0
    금액                    0
    선납금액                  0
    기타요금                  0
    할인금액                  0
    당월금액                  0
    차월증감액                 0
    연체료                   0
    감액료                   0
    청구금액                  0
    전화국명                  0
    dtype: int64




```python
kt.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>서비스계약ID</th>
      <th>계약자명(가입자명)</th>
      <th>서비스번호(TRIM)</th>
      <th>개통일(준공일)</th>
      <th>해지일</th>
      <th>모상품명</th>
      <th>요금항목명</th>
      <th>청구일자</th>
      <th>금액</th>
      <th>선납금액</th>
      <th>기타요금</th>
      <th>할인금액</th>
      <th>당월금액</th>
      <th>차월증감액</th>
      <th>연체료</th>
      <th>감액료</th>
      <th>청구금액</th>
      <th>전화국명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20705470030</td>
      <td>한국식품산업협회 부산지부</td>
      <td>N0050705</td>
      <td>20150629</td>
      <td>99999999</td>
      <td>보안장비</td>
      <td>이전비</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>대연지점</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20391299720</td>
      <td>(주)일양로지스</td>
      <td>N0049707</td>
      <td>20150501</td>
      <td>99999999</td>
      <td>보안장비</td>
      <td>이전비</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>공항국사</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21984609500</td>
      <td>(주)윤성에프앤씨</td>
      <td>N0056905</td>
      <td>20160202</td>
      <td>99999999</td>
      <td>보안장비</td>
      <td>이전비</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>평택지사(CS부)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22508634040</td>
      <td>주식회사 한국체인모터</td>
      <td>N0059200</td>
      <td>20160510</td>
      <td>99999999</td>
      <td>보안장비</td>
      <td>이전비</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>북부천지점</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22628829030</td>
      <td>(주)이노디자인</td>
      <td>N0059692</td>
      <td>20160525</td>
      <td>99999999</td>
      <td>보안장비</td>
      <td>이전비</td>
      <td>20170210</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>강남지사(CS부)</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
kt.columns=kt.columns.str.replace(' ','')
```


```python
kt.columns
```




    Index(['서비스계약ID', '계약자명(가입자명)', '서비스번호(TRIM)', '개통일(준공일)', '해지일', '모상품명',
           '요금항목명', '청구일자', '금액', '선납금액', '기타요금', '할인금액', '당월금액', '차월증감액', '연체료',
           '감액료', '청구금액', '전화국명'],
          dtype='object')




```python
dum=["모상품명","요금항목명"]
```


```python
kt_d= pd.get_dummies(kt[dum])
```


```python
kt["모상품명"].unique()
```




    array(['보안장비', '보안관리', '네트워크관리(표준형)', '네트워크장비', '네트워크관리(고급형)', '무선랜장비',
           'IP-PBX장비', '네트워크장비유지보수', '네트워크관리(기본형)', '그린PC', '서버장비', 'CCTV장비',
           0], dtype=object)




```python
kt.columns
```




    Index(['서비스계약ID', '계약자명(가입자명)', '서비스번호(TRIM)', '개통일(준공일)', '해지일', '모상품명',
           '요금항목명', '청구일자', '금액', '선납금액', '기타요금', '할인금액', '당월금액', '차월증감액', '연체료',
           '감액료', '청구금액', '전화국명'],
          dtype='object')




```python
kt_notD= kt[['개통일(준공일)', '해지일', '청구일자', '금액', 
            '선납금액', '기타요금', '할인금액', '당월금액', '차월증감액', '연체료',
       '감액료', '청구금액']]
```


```python
KT=pd.concat([kt_notD, kt_d], axis=1)
```


```python
KT
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>개통일(준공일)</th>
      <th>해지일</th>
      <th>청구일자</th>
      <th>금액</th>
      <th>선납금액</th>
      <th>기타요금</th>
      <th>할인금액</th>
      <th>당월금액</th>
      <th>차월증감액</th>
      <th>연체료</th>
      <th>...</th>
      <th>요금항목명_관제서비스료</th>
      <th>요금항목명_신규설치비</th>
      <th>요금항목명_신규설치비</th>
      <th>요금항목명_유지보수료</th>
      <th>요금항목명_이전비</th>
      <th>요금항목명_임대이용료</th>
      <th>요금항목명_임대이용료</th>
      <th>요금항목명_장비구매료</th>
      <th>요금항목명_컨설팅료</th>
      <th>요금항목명_해지위약료</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20150629</td>
      <td>99999999</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20150501</td>
      <td>99999999</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20160202</td>
      <td>99999999</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20160510</td>
      <td>99999999</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20160525</td>
      <td>99999999</td>
      <td>20170210</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>918636</th>
      <td>20190320</td>
      <td>99991231</td>
      <td>20200110</td>
      <td>4200</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4200</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>918637</th>
      <td>20190320</td>
      <td>99991231</td>
      <td>20200110</td>
      <td>1000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1000</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>918638</th>
      <td>20190308</td>
      <td>99991231</td>
      <td>20200110</td>
      <td>1500</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1500</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>918639</th>
      <td>20190917</td>
      <td>99991231</td>
      <td>20200110</td>
      <td>6600</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6600</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>918640</th>
      <td>20180625</td>
      <td>99991231</td>
      <td>20200110</td>
      <td>13000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13000</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>918641 rows × 36 columns</p>
</div>




```python
kt['요금항목명'].unique()
```




    array(['이전비', '관제서비스료', '임대이용료', '유지보수료                              ',
           '임대이용료                              ',
           '장비구매료                              ',
           '신규설치비                              ', 0, '해지위약료',
           '신규설치비                     ',
           '컨설팅료                                '], dtype=object)




```python
KT=pd.concat([kt["계약자명(가입자명)"], KT], axis=1)
```


```python
g=KT[KT['요금항목명_관제서비스료']==1].groupby(KT["계약자명(가입자명)"])
```


```python
# for a, group in g["청구일자"]:
#     print(a)
#     print(group)
```


```python
len(KT["계약자명(가입자명)"].unique())
```




    11700




```python
KT["해지일"]=KT["해지일"].astype(str)
KT["해지일"][9999]
```




    '99999999'




```python
for i in range(len(KT)):
    if '99991231' in KT["해지일"][i] or '99999999' in KT["해지일"][i]:
        KT["이탈"][i]=0 
    else :
        KT["이탈"][i]=1
```


```python
KT
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>계약자명(가입자명)</th>
      <th>개통일(준공일)</th>
      <th>해지일</th>
      <th>청구일자</th>
      <th>금액</th>
      <th>선납금액</th>
      <th>기타요금</th>
      <th>할인금액</th>
      <th>당월금액</th>
      <th>차월증감액</th>
      <th>...</th>
      <th>요금항목명_신규설치비</th>
      <th>요금항목명_신규설치비</th>
      <th>요금항목명_유지보수료</th>
      <th>요금항목명_이전비</th>
      <th>요금항목명_임대이용료</th>
      <th>요금항목명_임대이용료</th>
      <th>요금항목명_장비구매료</th>
      <th>요금항목명_컨설팅료</th>
      <th>요금항목명_해지위약료</th>
      <th>이탈</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>한국식품산업협회 부산지부</td>
      <td>20150629</td>
      <td>99999999</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>(주)일양로지스</td>
      <td>20150501</td>
      <td>99999999</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>(주)윤성에프앤씨</td>
      <td>20160202</td>
      <td>99999999</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>주식회사 한국체인모터</td>
      <td>20160510</td>
      <td>99999999</td>
      <td>20170210</td>
      <td>100000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100000</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>(주)이노디자인</td>
      <td>20160525</td>
      <td>99999999</td>
      <td>20170210</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>918636</th>
      <td>재단법인 포항문화재단</td>
      <td>20190320</td>
      <td>99991231</td>
      <td>20200110</td>
      <td>4200</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4200</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>918637</th>
      <td>재단법인 포항문화재단</td>
      <td>20190320</td>
      <td>99991231</td>
      <td>20200110</td>
      <td>1000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1000</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>918638</th>
      <td>광명도시공사</td>
      <td>20190308</td>
      <td>99991231</td>
      <td>20200110</td>
      <td>1500</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1500</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>918639</th>
      <td>(주)한국야쿠르트</td>
      <td>20190917</td>
      <td>99991231</td>
      <td>20200110</td>
      <td>6600</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6600</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>918640</th>
      <td>김성용</td>
      <td>20180625</td>
      <td>99991231</td>
      <td>20200110</td>
      <td>13000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13000</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>918641 rows × 38 columns</p>
</div>




```python
from datetime import datetime, timedelta
```


```python
def Time(a, b):
    time1=datetime(int(a[0:4]),int(a[4:6]),int(a[6:8]))
    time2=datetime(int(b[0:4]),int(b[4:6]),int(b[6:8]))
    return round((time1-time2).days/30)
```


```python
KT.loc[KT["해지일"]<2000]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>계약자명(가입자명)</th>
      <th>개통일(준공일)</th>
      <th>해지일</th>
      <th>청구일자</th>
      <th>금액</th>
      <th>선납금액</th>
      <th>기타요금</th>
      <th>할인금액</th>
      <th>당월금액</th>
      <th>차월증감액</th>
      <th>...</th>
      <th>요금항목명_신규설치비</th>
      <th>요금항목명_유지보수료</th>
      <th>요금항목명_이전비</th>
      <th>요금항목명_임대이용료</th>
      <th>요금항목명_임대이용료</th>
      <th>요금항목명_장비구매료</th>
      <th>요금항목명_컨설팅료</th>
      <th>요금항목명_해지위약료</th>
      <th>이탈</th>
      <th>기간</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>23170</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>46341</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>69687</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>93261</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>117148</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>135912</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>160365</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>185684</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>211360</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>237316</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>263487</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>289847</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>316642</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>343582</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>370867</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>398506</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>426767</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>455345</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>472676</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>501693</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>530642</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>559626</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>588375</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>617043</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>646040</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>674961</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>704486</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>734194</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>751531</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>768777</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>786046</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>803440</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>820942</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>852414</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>884428</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
  </tbody>
</table>
<p>35 rows × 39 columns</p>
</div>




```python
KT.loc[KT["개통일(준공일)"]<2000]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>계약자명(가입자명)</th>
      <th>개통일(준공일)</th>
      <th>해지일</th>
      <th>청구일자</th>
      <th>금액</th>
      <th>선납금액</th>
      <th>기타요금</th>
      <th>할인금액</th>
      <th>당월금액</th>
      <th>차월증감액</th>
      <th>...</th>
      <th>요금항목명_신규설치비</th>
      <th>요금항목명_유지보수료</th>
      <th>요금항목명_이전비</th>
      <th>요금항목명_임대이용료</th>
      <th>요금항목명_임대이용료</th>
      <th>요금항목명_장비구매료</th>
      <th>요금항목명_컨설팅료</th>
      <th>요금항목명_해지위약료</th>
      <th>이탈</th>
      <th>기간</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>23170</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>46341</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>69687</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>93261</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>117148</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>135912</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>160365</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>185684</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>211360</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>237316</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>263487</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>289847</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>316642</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>343582</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>370867</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>398506</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>426767</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>455345</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>472676</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>501693</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>530642</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>559626</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>588375</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>617043</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>646040</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>674961</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>704486</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>734194</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>751531</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>768777</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>786046</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>803440</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>820942</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>852414</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
    <tr>
      <th>884428</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9999</td>
    </tr>
  </tbody>
</table>
<p>35 rows × 39 columns</p>
</div>




```python
KT["해지일"]=KT["해지일"].astype(str)
KT["개통일(준공일)"]=KT["개통일(준공일)"].astype(str)
```


```python
KT["기간"]=9999
```


```python
for i in range(len(KT)):
    if KT["이탈"][i]==1 and KT["개통일(준공일)"][i]!='0' and KT["해지일"][i]!='0':
        KT["기간"][i]=Time( KT["해지일"][i],KT["개통일(준공일)"][i])
```


```python
KT
```


```python
KT.columns = KT.columns.str.rstrip()
```


```python
KT.columns
```


```python
kt = KT.drop(['계약자명(가입자명)', '개통일(준공일)', '해지일','청구일자', '금액', '선납금액', '기타요금', '할인금액',
       '당월금액', '차월증감액', '연체료', '감액료'], axis=1)
```


```python
kt
```


```python
kt.to_csv("C:/Users/dhrms/Desktop/KT.csv", index=False, encoding='euc-kr')
```


```python

```
