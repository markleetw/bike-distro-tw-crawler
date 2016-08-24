#!/usr/bin/env python
# coding=utf-8
import pytz

# timezone and datetime format
tz = pytz.timezone('Asia/Taipei')
dt_format = "%Y%m%d%H%M%S"

# id column name
id_cn = "id"

# fetch time column name
ft_cn = "fetch_time"

# total docks column name
td_cn = "total_docks"

# available bikes column name
ab_cn = "available_bikes"

# empty docks column name
ed_cn = "empty_docks"

# output column names
output_columns = [
                    id_cn,
                    "name",
                    "area",
                    "address",
                    td_cn,
                    ab_cn,
                    ed_cn,
                    "lat",
                    "lng",
                    "last_update_time",
                    ft_cn
                ]

# ubike column names
ubike_columns = [
                    "sno",      # station number: 0001
                    "sna",      # name: 捷運市政府站(3號出口)
                    "sarea",    # area: 信義區
                    "ar",       # address
                    "tot",      # total dock number
                    "sbi",      # available bike number
                    "bemp",     # empty dock number
                    "lat",
                    "lng", 
                    "mday"      # last update time
                ]
