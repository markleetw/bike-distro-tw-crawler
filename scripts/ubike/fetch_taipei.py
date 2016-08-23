# coding=utf-8
import urllib
import StringIO
import gzip
import json
from datetime import datetime
import pandas
import constants as c
 
# taipei ubike api
api_url = "http://data.taipei/youbike"

city_name = "taipei"

def fetch():
    
    # print info
    print "Crawling YouBike real-time data of {0}...".format(city_name.upper())
    
    try:
        # decompress api data and parse to json format
        fetch_time = datetime.now(c.tz).strftime(c.dt_format)
        compressed_str = StringIO.StringIO(urllib.urlopen(api_url).read())
        compressed_str.seek(0)
        decompressed_str = gzip.GzipFile(fileobj=compressed_str, mode="rb").read()
        json_data = json.loads(decompressed_str)["retVal"]

        # convert json to dataframe
        ubike_df = pandas.DataFrame(json_data).T[c.ubike_columns]
        ubike_df[c.ft_cn] = fetch_time
        ubike_df.columns = c.output_columns
        
        # add ubike prefix to id
        ubike_df[c.id_cn] = "u_" + ubike_df[c.id_cn].astype(str)

        # finish info
        print "Fetch {0}({1}) data successfully!".format(city_name.upper(), len(ubike_df))
        
        return ubike_df
    except Exception as e:
        print e
        return None

