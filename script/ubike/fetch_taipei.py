# coding=utf-8
import urllib
import StringIO
import gzip
import json
from datetime import datetime
import pandas
from constants import *
 
# taipei ubike api
api_url = "http://data.taipei/youbike"

city_name = "taipei"

def fetch():
    
    # print info
    print "Crawling YouBike real-time data of {0}...".format(city_name.upper())
    
    try:
        # decompress api data and parse to json format
        fetch_time = datetime.now(tz).strftime(dt_format)
        compressed_str = StringIO.StringIO(urllib.urlopen(api_url).read())
        compressed_str.seek(0)
        decompressed_str = gzip.GzipFile(fileobj=compressed_str, mode="rb").read()
        json_data = json.loads(decompressed_str)["retVal"]

        # convert json to dataframe
        ubike_df = pandas.DataFrame(json_data).T[ubike_columns]
        ubike_df["fetch_time"] = fetch_time
        ubike_df.columns = output_columns
        
        # add ubike prefix to id
        ubike_df["id"] = "u_" + ubike_df["id"].astype(str)

        # finish info
        print "Fetch {0}({1}) data successfully!".format(city_name.upper(), len(ubike_df))
        
        return ubike_df
    except Exception as e:
        print e
        return None

