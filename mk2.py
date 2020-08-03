import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
new_gs = gs[gs['Volume'] != 0]          #거래량이 0인 날짜 제외

#그래프 출력
#plt.plot(gs.index, gs['Adj Close'])
#plt.show()



ma5 = new_gs['Adj Close'].rolling(window=5).mean()
ma20 = new_gs['Adj Close'].rolling(window=20).mean()
ma60 = new_gs['Adj Close'].rolling(window=60).mean()
ma120 = new_gs['Adj Close'].rolling(window=120).mean()

#각 주가이동평균 값들을 새로운 컬럼으로 추가
new_gs.insert(len(new_gs.columns), "MA5", ma5)
new_gs.insert(len(new_gs.columns), "MA20", ma20) 
new_gs.insert(len(new_gs.columns), "MA60", ma60) 
new_gs.insert(len(new_gs.columns), "MA120", ma120)

plt.plot(new_gs.index, new_gs['Adj Close'], label="Adj Close")
plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
plt.plot(new_gs.index, new_gs['MA20'], label="MA20")
plt.plot(new_gs.index, new_gs['MA60'], label="MA60")
plt.plot(new_gs.index, new_gs['MA120'], label="MA120")

plt.legend(loc='best')
plt.grid()
plt.show()