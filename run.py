import pandas
import openpyxl
import os
import pandas as pd
from pandas import Series, DataFrame, ExcelWriter
import pandas_datareader.data as web
import datetime
import timedelta
import matplotlib.pyplot as plt
import numpy as np

# 시작 종료 날짜 설정
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2020, 2, 1)

close_list = []          # 종가 종합 리스트
trans_list = []          # 거래대금 종합 리스트
norm_list = []           # normalized close 리스트
trans_deriv_list = []    # 거래대금 미분값 리스트
norm_deriv_list = []     # 정규화 미분값 리스트

# 남북경협 테마주 코드 20개
code = ["017800.KS", "023800.KS", "009270.KS", "001260.KS", "000720.KS",
        "001470.KS", "002100.KS", "001550.KS", "004000.KS", "025860.KS",
        "006280.KS", "015760.KS", "014990.KS", "033240.KS", "004090.KS",
        "058730.KS", "007110.KS", "002150.KS", "005110.KS", "070960.KS", ]

# COVID-19 관련주(올해 2월부터): KeyError
# code = ["065950.KQ", "131370.KQ", "017890.KQ", "133750.KQ", "289010.KQ",
#         "096530.KQ", "011150.KS", "045060.KQ", "084650.KQ", ]

# 정치인 테마주: 안철수(2012년 1월부터): KeyError
# code = ["004770.KS", "053800.KQ", "093640.KQ", "049080.KQ"]

# 정치인 테마주: 이재명
# code = ["045660.KQ", "224110.KQ", "025950.KQ",
#         "208140.KQ", "053160.KQ", "045340.KQ", ]

# 수소차 테마주
# code = ["018880.KS", "081000.KS", "023900.KQ",
#         "012340.KQ", "095190.KQ", "023800.KS", ]

# 5G 테마주: KeyError
# code = ["032500.KQ", "037460.KQ", "138080.KQ",
#         "056360.KQ", "010170.KQ", "100590.KQ", ]

# w = ExcelWriter('e.xlsx')


# 데이터 크롤링 함수
def f(x):
    try:
        frame = web.DataReader(x, "yahoo", start, end)
        # https://emilkwak.github.io/pandas-dataframe-settingwithcopywarning
        # SettingWithCopyWarning 경고가 자꾸 떴던 이유에 대한 링크
        # 아래 코드에 .copy()를 붙여줌으로써 해결됐다.
        new_frame = frame[frame['Volume'] != 0].copy()
        # 거래대금 행 추가
        new_frame['Transaction price'] = new_frame.loc[:, ('Close')] * \
            new_frame.loc[:, ('Volume')]
        # 정규화된 종가 행 추가
        new_frame['Norm_close'] = (new_frame.loc[:, ('Close')] - new_frame.loc[:, ('Close')].min()) / \
            (new_frame.loc[:, ('Close')].max() -
             new_frame.loc[:, ('Close')].min())
        # 정규화된 종가, 거래대금의 미분값 행 추가
        diff_frame = new_frame['Transaction price']
        new_frame['Trans deriv'] = -diff_frame.diff(periods=-1)
        new_frame['Norm deriv'] = -new_frame['Norm_close'].diff(periods=-10)
        # diff(periods=-1): 바로 다음 row값과의 차이
        # diff(periods=-5): 5일단위로 뺄셈
        # 엑셀파일로 저장
        # new_frame.to_excel(w, sheet_name="output" + str(x))
        # w.save()
        return new_frame
    except KeyError:
        pass


# 종목 별 크롤링 실행
k = list(map(f, code))

# 각 종목의 종가, 거래대금 값을 리스트에 추가
for i in k:
    close_list.append(i['Close'])
    trans_list.append(i['Transaction price'])
    norm_list.append(i['Norm_close'])
    trans_deriv_list.append(i['Trans deriv'])
    norm_deriv_list.append(i['Norm deriv'])

# 테마 별 종가, 거래대금, 정규화, 미분 종합 리스트
close_sum = sum(close_list)
trans_sum = sum(trans_list)
norm_sum = sum(norm_list)
trans_deriv_sum = sum(trans_deriv_list)
norm_deriv_sum = sum(norm_deriv_list)

# 종가 리스트의 이동평균선
# close_ma5 = close_sum.rolling(window=5).mean()
# close_ma10 = close_sum.rolling(window=10).mean()
# close_ma20 = close_sum.rolling(window=20).mean()
# close_ma60 = close_sum.rolling(window=60).mean()
# close_ma120 = close_sum.rolling(window=120).mean()

# 거래대금 리스트의 이동평균선
# trans_ma5 = trans_sum.rolling(window=5).mean()
# trans_ma10 = trans_sum.rolling(window=10).mean()
# trans_ma20 = trans_sum.rolling(window=20).mean()
# trans_ma60 = trans_sum.rolling(window=60).mean()
# trans_ma120 = trans_sum.rolling(window=120).mean()

# 정규화된 종가 리스트의 이동평균선
# norm_ma5 = norm_sum.rolling(window=5).mean()
# norm_ma10 = norm_sum.rolling(window=10).mean()
# norm_ma15 = norm_sum.rolling(window=15).mean()
norm_ma20 = norm_sum.rolling(window=20).mean()
# norm_ma60 = norm_sum.rolling(window=60).mean()
# norm_ma120 = norm_sum.rolling(window=120).mean()

# 정규화 종가 미분 리스트의 이동평균선
# norm_deriv_ma5 = norm_deriv_sum.rolling(window=5).mean()
# norm_deriv_ma10 = norm_deriv_sum.rolling(window=10).mean()
# norm_deriv_ma15 = norm_deriv_sum.rolling(window=15).mean()
norm_deriv_ma20 = norm_deriv_sum.rolling(window=20).mean()
# norm_deriv_ma60 = norm_deriv_sum.rolling(window=60).mean()
# norm_deriv_ma120 = norm_deriv_sum.rolling(window=120).mean()

# 거래대금 미분 리스트의 이동평균선
# trans_deriv_ma5 = trans_deriv_sum.rolling(window=5).mean()
# trans_deriv_ma10 = trans_deriv_sum.rolling(window=10).mean()
# trans_deriv_ma20 = trans_deriv_sum.rolling(window=20).mean()
# trans_deriv_ma60 = trans_deriv_sum.rolling(window=60).mean()
# trans_deriv_ma120 = trans_deriv_sum.rolling(window=120).mean()

# 종가 리스트의 그래프 생성
# plt.plot(close_sum.index, close_sum, label="close list")
# plt.plot(close_sum.index, close_ma5, label="close_ma5")
# plt.plot(close_sum.index, close_ma10, label="close_ma10")
# plt.plot(close_sum.index, close_ma20, label="close_ma20")
# plt.plot(close_sum.index, close_ma60, label="close_ma60")
# plt.plot(close_sum.index, close_ma120, label="close_ma120")

# 거래대금 리스트의 그래프 생성
# plt.plot(trans_sum.index, trans_sum, label="trans list")
# plt.plot(trans_sum.index, trans_ma5, label="trans_ma5")
# plt.plot(trans_sum.index, trans_ma10, label="trans_ma10")
# plt.plot(trans_sum.index, trans_ma20, label="trans_ma20")
# plt.plot(trans_sum.index, trans_ma60, label="trans_ma60")
# plt.plot(trans_sum.index, trans_ma120, label="trans_ma120")

# 정규화된 종가 리스트의 그래프 생성
# plt.plot(norm_sum.index, norm_sum, label="norm list")
# plt.plot(norm_sum.index, norm_ma5, label="norm_ma5")
# plt.plot(norm_sum.index, norm_ma10, label="norm_ma10")
# plt.plot(norm_sum.index, norm_ma15, label="norm_ma15")
plt.plot(norm_sum.index, norm_ma20, label="norm_ma20")
# plt.plot(norm_sum.index, norm_ma60, label="norm_ma60")
# plt.plot(norm_sum.index, norm_ma120, label="norm_ma120")

# 정규화 종가 미분 리스트의 그래프 생성
# plt.plot(norm_deriv_sum.index, norm_deriv_sum, label="norm_deriv list")
# plt.plot(norm_deriv_sum.index, norm_deriv_ma5, label="norm_deriv_ma5")
# plt.plot(norm_deriv_sum.index, norm_deriv_ma10, label="norm_deriv_ma10")
# plt.plot(norm_deriv_sum.index, norm_deriv_ma20, label="norm_deriv_ma20")
# plt.plot(norm_deriv_sum.index, norm_deriv_ma60, label="norm_deriv_ma60")
# plt.plot(norm_deriv_sum.index, norm_deriv_ma120, label="norm_deriv_ma120")

# 정규화 종가 미분 리스트의 그래프 생성
# plt.plot(trans_deriv_sum.index, trans_deriv_sum, label="trans_deriv list")
# plt.plot(trans_deriv_sum.index, trans_deriv_ma5, label="trans_deriv_ma5")
# plt.plot(trans_deriv_sum.index, trans_deriv_ma10, label="trans_deriv_ma10")
# plt.plot(trans_deriv_sum.index, trans_deriv_ma20, label="trans_deriv_ma20")
# plt.plot(trans_deriv_sum.index, trans_deriv_ma60, label="trans_deriv_ma60")
# plt.plot(trans_deriv_sum.index, trans_deriv_ma120, label="trans_deriv_ma120")

####################################### 15일선 #######################################
red_close_list = pd.DataFrame(index=range(0, 2), columns=['Date', 'value'])
count = 0
_begin = 0
_end = 0
beginDate = 0
endDate = 0

for i in norm_deriv_ma20.index:
    if(norm_deriv_ma20[i] >= 0.04):
        if count == 0:
            beginDate = i
        else:
            endDate = i
        red_close_list.append(norm_ma20)
        # red_close_list.loc[i] = norm_ma20[i]
        count += 1
        _end = norm_deriv_ma20[i]
    elif(_end - _begin >= 2 and count >= 10 and norm_deriv_ma20[i] < 0.04 and norm_deriv_ma20[i] > -0.3):
        red_close_list.append(norm_ma20[i])
    else:
        red_close_list.append(None)
        count = 0
        _begin = 0
        _end = 0
        # while 1:
        #     if beginDate == endDate:
        #         break
        #     del red_close_list[beginDate]
        #     if red_close_list[beginDate + timedelta.Timedelta(days=1)] == None:
        #         while red_close_list[beginDate] != None:
        #             beginDate = beginDate + timedelta.Timedelta(days=1)
        #     else:
        #         beginDate = beginDate + timedelta.Timedelta(days=1)
        red_close_list[red_close_list.columns.difference([beginDate, endDate])]

plt.plot(norm_sum.index, red_close_list, color='red')
######################################################################################

plt.legend(loc='best')
plt.grid()
plt.show()


"""
# 현대엘리베이터:        017800.KS
# 인지컨트롤스:          023800.KS
# 신원:                 009270.KS
# 남광토건:             001260.KS
# 현대건설:             000720.KS
# 삼부토건:             001470.KS
# 경농:                 002100.KS`
# 조비:                 001550.KS
# 롯데정밀화학:         004000.KS
# 남해화학:             025860.KS
# 녹십자:               006280.KS
# 한국전력:             015760.KS
# 인디에프:             014990.KS
# 자화전자:             033240.KS
# 한국석유:             004090.KS
# 다스코:               058730.KS
# 일신석재:             007110.KS
# 도화엔지니어링:       002150.KS
# 한창:                005110.KS
# 용펑리조트:           070960.KS
# 대아티아이:           045390.KS
"""
