# coding=utf-8
import pytz

# timezone and datetime format
tz = pytz.timezone('Asia/Taipei')
dt_format = "%Y%m%d%H%M%S"

# output column names
output_columns = [
                    "id",
                    "name",
                    "area",
                    "address",
                    "total_docks",
                    "available_bikes",
                    "empty_docks",
                    "lat",
                    "lng",
                    "last_update_time",
                    "fetch_time"
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