
import pandas as pd
import converter as conv


def preprocessor(df, num): 
    # data preprocessing
    w_datalist = []         # df[]는 리스트마냥 append 안돼서 만듦
    drop_indicator = df['이동거리(M)']

    cnt = 0

    for i in range(len(drop_indicator)):
        print(i)

        # drop
        if int(drop_indicator[i]) == 0:
            df = df.drop(index=i, axis=0)
            print(': dropped')
            cnt = cnt+1
        # converting process
        else:
            w_datalist.append(conv.wknd(str(df['대여일자'][i])))
            df['대여일자'][i] = conv.date(str(df['대여일자'][i]))
            df['대여구분코드'][i] = conv.btconv(str(df['대여구분코드'][i]))
            df['연령대'][i] = conv.ageconv(str(df['연령대'][i]))
    df = df.drop(labels=['성별','대여소'], axis=1)
    df.index = range(0,len(df))         # reset index: df_wknd와 df index 불일치가 에러 원인

    df_wknd = pd.DataFrame({'주말구분':w_datalist})

    df = pd.concat([df,df_wknd], axis=1, sort=True, ignore_index=True)        # integration


    # Result
    print("\n\nDropped {} data\n\n".format(cnt))
    print(df)


    # save preprocessed data
    #df.to_csv("C:/Coding/AI&ML/Projects/seoul_bike_analysis/data/data_preprocessed_month{}.csv".format(num), index = False, encoding='utf-8')
    df.to_csv("C:/Coding/AI&ML/Projects/seoul_bike_analysis/data/preprocessed_debugging.csv", index = False, encoding='utf-8')


'''
#debugging
df_raw = pd.read_csv('C:/Coding/AI&ML/Projects/seoul_bike_analysis/data/rawdata_debugging.csv', encoding='utf-8')
preprocessor(df_raw,1)
'''

'''
[label 해석]
0. 대여일자
1. 대여소번호
2. 대여구분코드
3. 연령대
4. 이용건수
5. 운동량
6. 탄소량
7. 이동거리(M)
8. 이용시간(분)
9. 주말구분
'''
