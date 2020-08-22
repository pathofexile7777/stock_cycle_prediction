# 남북경협 관련주들
# 현대엘리베이터: 017800 / 아난티: 025980 / 제이에스티나: 026040 / 좋은사람들: 033340
# 신원: 009270 / 재영솔루텍: 049630 / 남광토건: 001260 / 현대건설: 000720
# 삼부토건: 001470 / 경농: 002100 / 조비: 001550 / 롯데정밀화학: 004000 / 남해화학: 025860
# 녹십자: 006280 / 한국전력: 015760 / 인디에프: 014990 / 인지컨트롤스: 023800
# 자화전자: 033240 / 남화토건: 091590 / 한국석유: 004090 / 다스코: 058730
# 스페코: 013810 / 일신석재: 007110 / 지엔씨에너지: 119850 / 희림: 037440
# 이엑스티: 226360 / 도화엔지니어링: 002150 / 양지사: 030960 / 한창: 005110

from pandas import Series, DataFrame
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

# 시작 종료 날짜 설정
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2019, 12, 31)

close_list = []          # 종가 종합 리스트
trans_list = []          # 거래대금 종합 리스트

# 남북경협 테마주 코드
code = ["017800.KS", "023800.KS", "009270.KS", "001260.KS", "000720.KS", "001470.KS",
        "002100.KS", "001550.KS", "004000.KS", "025860.KS", "006280.KS", "015760.KS",
        "014990.KS", "033240.KS", "004090.KS", "058730.KS", "007110.KS", "002150.KS", "005110.KS"]


# 데이터 크롤링 함수
def f(x):
    frame = web.DataReader(x, "yahoo", start, end)
    new_frame = frame[frame['Volume'] != 0]
    new_frame['Transaction price'] = new_frame['Close'] * new_frame['Volume']
    return new_frame


# 종목 별 크롤링 실행
k = list(map(f, code))

# 각 종목의 종가, 거래대금 값을 리스트에 추가
for i in k:
    close_list.append(i['Close'])
    trans_list.append(i['Transaction price'])


# 테마 별 종가, 거래대금 종합 리스트
close_sum = sum(close_list)
trans_sum = sum(trans_list)

# 종가 리스트의 이동평균선
close_ma5 = close_sum.rolling(window=5).mean()
close_ma20 = close_sum.rolling(window=20).mean()
close_ma60 = close_sum.rolling(window=60).mean()
close_ma120 = close_sum.rolling(window=120).mean()

# 거래대금 리스트의 이동평균선
trans_ma5 = trans_sum.rolling(window=5).mean()
trans_ma20 = trans_sum.rolling(window=5).mean()
trans_ma60 = trans_sum.rolling(window=5).mean()
trans_ma120 = trans_sum.rolling(window=5).mean()

# 종가 리스트의 그래프 생성
#plt.plot(close_sum.index, close_sum, label="close list")
# plt.plot(close_sum.index, close_ma5, label="close_ma5")
# plt.plot(close_sum.index, close_ma20, label="close_ma20")
#plt.plot(close_sum.index, close_ma60, label="close_ma60")
# plt.plot(close_sum.index, close_ma120, label="close_ma120")

# 거래대금 리스트의 그래프 생성
# plt.plot(trans_sum.index, trans_sum, label="trans list")
# plt.plot(trans_sum.index, trans_ma5, label="trans_ma5")
# plt.plot(trans_sum.index, trans_ma20, label="trans_ma20")
plt.plot(trans_sum.index, trans_ma60, label="trans_ma60")
# plt.plot(trans_sum.index, trans_ma120, label="trans_ma120")

plt.legend(loc='best')
plt.grid()
plt.show()

# print(new_frame['sum_of_trans'])

"""print(k)"""


#k = list(map(lambda x:web.DataReader(x, "yahoo", start, end), code))


"""
# 데이터 수집 함수
for i in code:
    gs = web.DataReader(i, "yahoo", start, end)
    new_gs = gs[gs['Volume'] != 0]      # 거래량이 0인 날짜 제외

    # 거래대금 행 추가
    new_gs['Transaction price'] = new_gs['Close'] * new_gs['Volume']

    close += new_gs['Close']
    theme += new_gs['Transaction price']

# 테마의 종합 종가 기준 이동평균선
# ma5 = close['Close'].rolling(window=5).mean()
# ma20 = close['Close'].rolling(window=20).mean()
# ma60 = close['Close'].rolling(window=60).mean()
# ma120 = close['Close'].rolling(window=120).mean()

# 테마의 거래대금 기준 이동평균선
ma5 = theme['Transaction price'].rolling(window=5).mean()
ma20 = theme['Transaction price'].rolling(window=20).mean()
ma60 = theme['Transaction price'].rolling(window=60).mean()
ma120 = theme['Transaction price'].rolling(window=120).mean()

# 종합 종가에 각 이동평균선 컬럼 추가
# close.insert(len(close.columns), "MA5", ma5)
# close.insert(len(close.columns), "MA60", ma60)
# close.insert(len(close.columns), "MA20", ma20)
# close.insert(len(close.columns), "MA120", ma120)

# 종합 거래대금에 각 이동평균선 컬럼 추가
theme.insert(len(theme.columns), "MA5", ma5)
theme.insert(len(theme.columns), "MA20", ma20)
theme.insert(len(theme.columns), "MA60", ma60)
theme.insert(len(theme.columns), "MA120", ma120)



plt.plot(theme.index, theme['Transaction price'], label="Transaction price")
plt.plot(theme.index, theme['MA5'], label="MA5")
#plt.plot(theme.index, theme['MA20'], label="MA20")
#plt.plot(theme.index, theme['MA60'], label="MA60")
plt.plot(theme.index, theme['MA120'], label="MA120")

plt.legend(loc='best')
plt.grid()
plt.show()


# # 종목별 데이터 수집
# for i in code.index:
#     cal(code[i])

# # 각 종목의 거래대금 수집
# # 설정한 날짜의 시작과 끝을 기준으로 반복
#     for i in new_gs.index:
#         theme[i] = 0
#         # 각 종목 별 값 취합
#         for j in code.index:
#             theme[i] =

# 현대엘리베이터
# cal("017800.KS")
# 인지컨트롤스
# cal("023800.KS")
# 신원
# cal("009270.KS")
# 남광토건
# cal("001260.KS")
# 현대건설
# cal("000720.KS")
# 삼부토건
# cal("001470.KS")
# 경농
# cal("002100.KS")
# 조비
# cal("001550.KS")
# 롯데정밀화학
# cal("004000.KS")
# 남해화학
# cal("025860.KS")
# 녹십자
# cal("006280.KS")
# 한국전력
# cal("015760.KS")
# 인디에프
# cal("014990.KS")
# 자화전자
# cal("033240.KS")
# 한국석유
# cal("004090.KS")
# 다스코
# cal("058730.KS")
# 일신석재
# cal("007110.KS")
# 도화엔지니어링
# cal("002150.KS")
# 한창
# cal("005110.KS")
"""
