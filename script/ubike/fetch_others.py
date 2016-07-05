# coding=utf-8
import urllib
import re
import json
import sys
import pandas
from datetime import datetime
from constants import *

# YouBike url
ubike_url = "http://taipei.youbike.com.tw/cht/f12.php"
ubike_city_param = "?loc="
ubike_cities = ["ntpc", "taichung", "chcg", "tycg"]

def fetch():
    
    # init dataframe
    ubike_df = pandas.DataFrame(columns=output_columns)

    for ubike_city in ubike_cities:
        # process info
        print "Crawling YouBike real-time data of {0}...".format(ubike_city.upper())
        
        try:
            # fetch data and parse to json
            fetch_time = datetime.now(tz).strftime(dt_format)
            ubike_html = urllib.urlopen(ubike_url + ubike_city_param + ubike_city).read()
            encoded_data = re.search("\\w*='(.*)';\\w*=JSON.parse", ubike_html).group(1)
            decoded_data = urllib.unquote(encoded_data)
            json_data = json.loads(decoded_data)

            # convert from json to dataframe and add fetch_time column
            city_df = pandas.DataFrame(json_data).T[ubike_columns]
            city_df["fetch_time"] = fetch_time
            city_df.columns = output_columns

            # concat dataframe
            ubike_df = ubike_df.append(city_df, ignore_index=True)

            # finish info
            print "Fetch {0}({1}) data successfully!".format(ubike_city.upper(), len(city_df))
        except Exception as e:
            print e
    
    # add ubike prefix to id
    ubike_df["id"] = "u_" + ubike_df["id"].astype(str)
    return ubike_df
