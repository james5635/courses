from __future__ import annotations  # postponeed evaluation of annotation
import pandas as pd
import numpy as np
from datetime import datetime
import calendar

from pandas import DataFrame
from typing import List, cast

URL: str = (
    "https://marineweather.net/tide/cape-may-canal-cape-may-delaware-bay-nj-tides"
)
tables: List[DataFrame] = pd.read_html(URL)
print("There are : ", len(tables), " tables")
print("Take look at the table:")
table_1 = tables[0]
# print(table_1)
table_1.head()
# postponeed evaluation of annotation
# time_list: "Dog" = table_1["Time"]
time_list: "pd.Series[str]" = table_1["Time"]
date_list = table_1["Date"]
h_array = []
m_array = []
d_array = []
epoch_array = []

for t in time_list:
    a = t.split(":")
    hour = int(a[0])
    b = a[1]
    min = int(b[0:2])
    if b[-2:] == "pm":
        hour = hour + 11
    h_array.append(hour)
    m_array.append(min)
for d in date_list:
    d_array.append(int(d[8::]))
for c in range(len(time_list)):
    t = datetime(2023, 8, d_array[c], h_array[c], m_array[c], 0)
    epoch_array.append(int(calendar.timegm(t.timetuple())))
print(epoch_array)
height_list = table_1["Feet"]
f_array = []
for f in height_list:
    f_array.append(float(f[0:4]))
print(f_array)
