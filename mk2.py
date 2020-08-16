# 남북경협 관련주들
# 현대엘리베이터: 017800 / 아난티: 025980 / 제이에스티나: 026040 / 좋은사람들: 033340
# 신원: 009270 / 재영솔루텍: 049630 / 남광토건: 001260 / 현대건설: 000720
# 삼부토건: 001470 / 경농: 002100 / 조비: 001550 / 롯데정밀화학: 004000 / 남해화학: 025860
# 녹십자: 006280 / 한국전력: 015760 / 인디에프: 014990 / 인지컨트롤스: 023800
# 자화전자: 033240 / 남화토건: 091590 / 한국석유: 004090 / 다스코: 058730
# 스페코: 013810 / 일신석재: 007110 / 지엔씨에너지: 119850 / 희림: 037440
# 이엑스티: 226360 / 도화엔지니어링: 002150 / 양지사: 030960 / 한창: 005110

import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt


def cal(code):
    gs = web.DataReader(code, "yahoo", "2017-01-01", "2019-12-31")
    new_gs = gs[gs['Volume'] != 0]  # 거래량이 0인 날짜 제외

    ma5 = new_gs['Adj Close'].rolling(window=5).mean()
    ma20 = new_gs['Adj Close'].rolling(window=20).mean()
    ma60 = new_gs['Adj Close'].rolling(window=60).mean()
    ma120 = new_gs['Adj Close'].rolling(window=120).mean()

    # 각 주가이동평균 값들을 새로운 컬럼으로 추가
    new_gs.insert(len(new_gs.columns), "MA5", ma5)
    new_gs.insert(len(new_gs.columns), "MA20", ma20)
    new_gs.insert(len(new_gs.columns), "MA60", ma60)
    new_gs.insert(len(new_gs.columns), "MA120", ma120)

    plt.plot(new_gs.index, new_gs['Adj Close'], label="Adj Close")
    #plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
    plt.plot(new_gs.index, new_gs['MA20'], label="MA20")
    #plt.plot(new_gs.index, new_gs['MA60'], label="MA60")
    plt.plot(new_gs.index, new_gs['MA120'], label="MA120")

    plt.legend(loc='best')
    plt.grid()
    plt.show()


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
cal("005110.KS")
