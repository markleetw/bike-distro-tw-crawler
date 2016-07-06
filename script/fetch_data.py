# coding=utf-8
from ubike import fetch_taipei as ubike_taipei
from ubike import fetch_others as ubike_others
from cbike import fetch_kaohsiung as cbike_kaohsiung
from constants import output_columns
import pandas

# put spiders in here
spiders = [
            ubike_taipei,
            ubike_others,
            cbike_kaohsiung
          ]

# init dataframe
df = pandas.DataFrame(columns=output_columns)

for spider in spiders:
    df = df.append(spider.fetch(), ignore_index=True)

df.to_csv("df.csv", sep="\t", encoding="utf-8")
