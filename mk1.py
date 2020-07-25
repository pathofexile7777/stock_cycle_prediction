#남북경협 관련주들
#현대엘리베이터: 017800 / 아난티: 025980 / 제이에스티나: 026040 / 좋은사람들: 033340
#신원: 009270 / 재영솔루텍: 049630 / 남광토건: 001260 / 현대건설: 000720
#삼부토건: 001470 / 경농: 002100 / 조비: 001550 / 롯데정밀화학: 004000 / 남해화학: 025860
#녹십자: 006280 / 한국전력: 015760 / 인디에프: 014990 / 인지컨트롤스: 023800
#자화전자: 033240 / 남화토건: 091590 / 한국석유: 004090 / 다스코: 058730
#스페코: 013810 / 일신석재: 007110 / 지엔씨에너지: 119850 / 희림: 037440
#이엑스티: 226360 / 도화엔지니어링: 002150 / 양지사: 030960 / 한창: 005110

from bs4 import BeautifulSoup
import urllib.request as req
import requests
import pandas
import datetime
import matplotlib.pyplot as plt
from matplotlib import style


def crawl(code, year):
    date = datetime.datetime.now()                  # 현재 날짜
    period = float(year) * 365
    bring = float(period) / 1.47                    # 366일 = 248(1년 기준)
    url = f"http://fchart.stock.naver.com/sise.nhn?symbol={code}&timeframe=day&count={bring}&requestType=0"
    request_result = requests.get(url)
    soup = BeautifulSoup(request_result.content, 'html.parser')
    all_data = soup.select('chartdata')
    stockName = all_data[0].attrs['name']
    stockData = soup.select('item')
    data_dict = {}                                  # 데이터 dict
    date_list = []                                  # 날짜 list
    started_list = []                               # 시가 list
    highest_list = []                               # 고가 list
    lowest_list = []                                # 저가 list
    Modified_list = []                              # 수정종가 list
    quantity_list = []                              # 거래량 list
    daegeum_list = []                               # 거래대금 list

    for i in range(len(stockData)):
        int = str(stockData[i])[12:-9]
        int_split = int.split('|')
        date = pandas.to_datetime(int_split[0])
        starting_price = float(int_split[1])        # 시가
        highest_price = float(int_split[2])         # 고가
        lowest_price = float(int_split[3])          # 저가
        ModCP = float(int_split[4])                 # 수정종가
        quantity = float(int_split[5])              # 거래량
        daegeum = ModCP * quantity                  # 거래대금
        date_list.append(date)
        started_list.append(starting_price)
        highest_list.append(highest_price)
        lowest_list.append(lowest_price)
        Modified_list.append(ModCP)
        quantity_list.append(quantity)
        daegeum_list.append(daegeum)
    data_dict['시가'] = started_list
    data_dict['고가'] = highest_list
    data_dict['저가'] = lowest_list
    data_dict['수정종가'] = Modified_list
    data_dict['거래량'] = quantity_list
    data_dict['거래대금'] = daegeum_list

    df = pandas.DataFrame(data_dict, index=date_list)
    print(df)

    filename = f'{stockName}_{str(date_list[0])[:10]}-{str(date)[:10]}'
    df.to_csv('{0}.csv'.format(filename), encoding='ms949')
    print('\n{0} 저장 완료'.format(filename))

    style.use('ggplot')
    plt.plot(date_list, Modified_list)
    plt.show()


crawl('025980', '3')
