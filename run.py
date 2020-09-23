import pandas
import openpyxl
import os
from pandas import Series, DataFrame, ExcelWriter
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np

# 시작 종료 날짜 설정
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2019, 12, 31)

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
# "045390.KS", ]

# w = ExcelWriter('e.xlsx')


# 데이터 크롤링 함수
def f(x):
    frame = web.DataReader(x, "yahoo", start, end)
    new_frame = frame[frame['Volume'] != 0]
    # 거래대금 행 추가
    new_frame['Transaction price'] = new_frame['Close'] * new_frame['Volume']
    # 정규화된 종가 행 추가
    new_frame['Norm_close'] = (new_frame['Close'] - new_frame['Close'].min()) / \
        (new_frame['Close'].max() - new_frame['Close'].min())
    # 정규화된 종가, 거래대금의 미분값 행 추가
    diff_frame = new_frame['Transaction price']
    new_frame['Trans deriv'] = -diff_frame.diff(periods=-1)
    new_frame['Norm deriv'] = -new_frame['Norm_close'].diff(periods=-5)
    # diff(periods=-1): 바로 다음 row값과의 차이
    # diff(periods=-5): 5일단위로 뺄셈
    # 엑셀파일로 저장
    # new_frame.to_excel(w, sheet_name="output" + str(x))
    # w.save()
    return new_frame


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
norm_ma15 = norm_sum.rolling(window=15).mean()
# norm_ma20 = norm_sum.rolling(window=20).mean()
# norm_ma60 = norm_sum.rolling(window=60).mean()
# norm_ma120 = norm_sum.rolling(window=120).mean()

# 정규화 종가 미분 리스트의 이동평균선
# norm_deriv_ma5 = norm_deriv_sum.rolling(window=5).mean()
# norm_deriv_ma10 = norm_deriv_sum.rolling(window=10).mean()
norm_deriv_ma15 = norm_deriv_sum.rolling(window=15).mean()
# norm_deriv_ma20 = norm_deriv_sum.rolling(window=20).mean()
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
plt.plot(norm_sum.index, norm_ma15, label="norm_ma15")
# plt.plot(norm_sum.index, norm_ma20, label="norm_ma20")
# plt.plot(norm_sum.index, norm_ma60, label="norm_ma60")
# plt.plot(norm_sum.index, norm_ma120, label="norm_ma120")

# 정규화 종가 미분 리스트의 그래프 생성
# plt.plot(norm_deriv_sum.index, norm_deriv_sum, label="norm_deriv list")
# plt.plot(norm_deriv_sum.index, norm_deriv_ma5, label="norm_deriv_ma5")
# plt.plot(norm_deriv_sum.index, norm_deriv_ma10, label="norm_deriv_ma10")


####################################### 10일선 #######################################
# red_close_list = []
# count = 0

# for i in norm_deriv_ma10.index:
#     if(norm_deriv_ma10[i] > 0.1):
#         red_close_list.append(norm_ma10[i])
#         count += 1
#     elif(count >= 5 and norm_deriv_ma10[i] < 0.1 and norm_deriv_ma10[i] > -0.1):
#         red_close_list.append(norm_ma10[i])
#     else:
#         red_close_list.append(None)
#         count = 0

# plt.plot(norm_sum.index, red_close_list, color='red')
######################################################################################

####################################### 15일선 #######################################
red_close_list = []
count = 0

for i in norm_deriv_ma15.index:
    if(norm_deriv_ma15[i] > 0.1):
        red_close_list.append(norm_ma15[i])
        count += 1
    elif(count >= 10 and norm_deriv_ma15[i] < 0.1 and norm_deriv_ma15[i] > -0.01):
        red_close_list.append(norm_ma15[i])
    else:
        red_close_list.append(None)
        count = 0

plt.plot(norm_sum.index, red_close_list, color='red')
######################################################################################


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

plt.legend(loc='best')
plt.grid()
plt.show()


"""print(k)"""


"""
# 현대엘리베이터:        017800.KS
# 인지컨트롤스:          023800.KS
# 신원:                 009270.KS
# 남광토건:             001260.KS
# 현대건설:             000720.KS
# 삼부토건:             001470.KS
# 경농:                 002100.KS
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
