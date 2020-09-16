import pandas
import openpyxl
import os
from pandas import Series, DataFrame
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np

start = datetime.datetime(2019, 12, 11)
end = datetime.datetime(2019, 12, 31)

print(type(start))
