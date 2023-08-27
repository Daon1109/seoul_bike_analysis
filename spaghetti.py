
import pandas as pd
#import week_categorizer as we

######################## Data Preprocessing #########################

# integrating data
'''li = []
for i in range(2):          # change it to 5
    print('check1')
    df = pd.read_csv('C:/Coding/Tensorflow/Dataset/seoul_bike/D_22_{mo}.csv'.format(mo=i+8), encoding='cp949')  # encoding: CP949
    li.append(df)
data = pd.concat(li)
print('check2')'''

data = pd.read_csv('C:/Coding/Tensorflow/Dataset/seoul_bike/training.csv', encoding='cp949') #temp

# drop empty&errored columns
'''data.drop("성별", axis=1, inplace=True)
for j in data.iterrows():
    if data['이동거리(M)'].values[j] == 0 or data['이동거리(M)'].values[j] > 25000.00:
        data.drop(j, axis=0, inplace=True)          # dropping row by j(=index)
        print("deleted: row#}".format(j))
    else:
        pass'''     # something's wrong + it takes so much time

######################## Creating Model #########################

inputdata = []      # data for ML
for k, rows in data.iterrows():
    inputdata.append([rows['대여일자'], rows['대여소번호'], rows['연령대']])
#
print(inputdata)
print(k)

# weekend categorizer(append it)
# we.wknd()




# fuck legacy / Aug 23, 2023
'''

import pandas as pd
import converter as conv

# importing & integrating data
data = pd.DataFrame()
for i in range(2):
    df = pd.read_csv('C:/Coding/AI&ML/Dataset/training{n}.csv'.format(n=i+1))
    data = data.append(df, ignore_index=True)

# data(refined) declare
inputdata = []
date = []
weekend = []
borrowtype = []
age = []

# refining data
for i, rows in data.iterrows():
    if rows['대여일자'].isnull()==1 or rows['대여소번호'].isnull()==1 or rows['대여구분코드'].isnull()==1 or rows['연령대'].isnull()==1:
        data = data.drop(data[i])
    else:   
        date = date.append(conv.date(rows['대여일자']))
        weekend = weekend.append(conv.wknd(rows['대여일자']))
        borrowtype = borrowtype.append(conv.btconv(rows['대여구분코드']))
        age = age.append(conv.ageconv(rows['연령대']))

# integrating into inputdata
for i, rows in data.iterrows():
    inputdata.append([date, weekend, rows['대여소번호'], borrowtype, age])



# 학습시키기
# matplotlib 분석
'''