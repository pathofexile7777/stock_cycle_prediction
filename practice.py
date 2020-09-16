from pandas import Series, DataFrame

kakao = Series([92600, 12345, 23456, 23623, 60404])


kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low':  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(
    daeshin, columns=['open', 'high', 'low', 'close'], index=date)

day_data = daeshin_day.loc['16.02.24']

print(daeshin_day.columns)
print(daeshin_day.index)
