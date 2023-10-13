
import pandas as pd
import preprocess as prep


# data preprocessing
df_debug = pd.read_csv('C:/Coding/AI&ML/Projects/seoul_bike_analysis/data/rawdata_debugging.csv', encoding='utf-8')
prep.preprocessor(df_debug,0)


# use this after debugging
'''
# data preprocessing
for i in range(8,13):
    df_raw = pd.read_csv('C:/Coding/AI&ML/Projects/seoul_bike_analysis/data/D_22_{}.csv'.format(i), encoding='utf-8')
    prep.preprocessor(df_raw, i)
df_8 = pd.read_csv('C:/Coding/AI&ML/Projects/seoul_bike_analysis/data/data_preprocessed_month8.csv', encoding='utf-8')
df_9 = pd.read_csv('C:/Coding/AI&ML/Projects/seoul_bike_analysis/data/data_preprocessed_month9.csv', encoding='utf-8')
df_10 = pd.read_csv('C:/Coding/AI&ML/Projects/seoul_bike_analysis/data/data_preprocessed_month10.csv', encoding='utf-8')
df_11 = pd.read_csv('C:/Coding/AI&ML/Projects/seoul_bike_analysis/data/data_preprocessed_month11.csv', encoding='utf-8')
df_12 = pd.read_csv('C:/Coding/AI&ML/Projects/seoul_bike_analysis/data/data_preprocessed_month12.csv', encoding='utf-8')
df = pd.concat([df_8,df_9,df_10,df_11,df_12], axis=0)
'''


# preprocessed data(integrated)
df = pd.read_csv('C:/Coding/AI&ML/Projects/seoul_bike_analysis/data/preprocessed_debugging.csv', encoding='utf-8')
print(df)
