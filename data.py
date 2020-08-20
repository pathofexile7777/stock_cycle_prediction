import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2019, 12, 22)
end = datetime.datetime(2019, 12, 31)

code = ("017800.KS", "004090.KS")

gs = web.DataReader(code[0], "yahoo", start, end)
new_gs = gs[gs['Volume'] != 0]  # 거래량이 0인 날짜 제외

theme = new_gs['Open']
print(theme)

# for i in new_gs.index:
# tp = new_gs.loc[i]['Close'] * new_gs.loc[i]['Volume']
# print(tp)
# new_gs.loc[i]['Transaction price'] = tp
new_gs['Transaction price'] = new_gs['Close'] * new_gs['Volume']

# print(new_gs)
