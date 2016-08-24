#!/usr/bin/env python
# coding=utf-8
import urllib
import pandas
from lxml import objectify
from datetime import datetime
import constants as c

# cbike column names
cbike_columns = [
                    "StationID",
                    "StationName",
                    None,
                    "StationAddress",
                    None,
                    "StationNums1",    # available bikes
                    "StationNums2",    # empty docks
                    "StationLat",
                    "StationLon",
                    None
                ]

# cbike kaohsiung api url 
api_url = "http://www.c-bike.com.tw/xml/stationlistopendata.aspx"
city_name = "kaohsiung"

def fetch():
    
    # process info
    print "Crawling YouBike real-time data of {0}...".format(city_name.upper())
    
    # parse xml and get station elements
    xml = objectify.fromstring(urllib.urlopen(api_url).read())
    fetch_time = datetime.now(c.tz).strftime(c.dt_format)
    xml_stations = xml.find("BIKEStation").getchildren()

    # init cbike dataframe
    cbike_df = pandas.DataFrame(columns=cbike_columns)

    # parse stations
    for xml_station in xml_stations:
        
        # convert xml elements to list
        station_eles = list()
        for cbike_column in cbike_columns:
            station_ele = None
            if cbike_column is not None:
                station_ele = xml_station.find(cbike_column).text
            station_eles.append(station_ele)
        
        # append list to dataframe
        cbike_df.loc[len(cbike_df)] = station_eles
        
    # update fetch time 
    cbike_df[c.ft_cn] = fetch_time
    
    # change to output column names
    cbike_df.columns = c.output_columns
    
    # update total docks column
    cbike_df[c.td_cn] = (cbike_df[c.ab_cn].astype(int) + cbike_df[c.ed_cn].astype(int)).astype(str)
    
    # add cbike prefix to id
    cbike_df[c.id_cn] = cbike_df[c.id_cn].apply(lambda x: "c_" + x.zfill(4))
        
    # finish info
    print "Fetch {0}({1}) data successfully!".format(city_name.upper(), len(cbike_df))
    
    return cbike_df
