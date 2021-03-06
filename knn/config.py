__author__ = 'wenli'
"""
All constants should go here.
"""

import os

DIR = os.path.dirname(__file__)
EXAMPLE_DATA = DIR+"/data/example_data.csv" # small data files (ideally < 5 MB) should be stored in data folder
TRIP_DATA_1 = DIR+"/data/trip_data_1.csv" # Large data files can be outside your directory structure
TRIP_DATA_2 = DIR+"/data/trip_data_2.csv" # Large data files can be outside your directory structure
TRAIN_DATA = DIR+"/data/train_data.csv" # contains every 20th trip from trip_data_2.csv

FILE_FORMAT ={
    '0':'medallion',
    '1':'hack_license',
    '2':'vendor_id',
    '3':'rate_code',
    '4':'store_and_fwd_flag',
    '5':'pickup_datetime',
    '6':'dropoff_datetime',
    '7':'passenger_count',
    '8':'trip_time_in_secs',
    '9':'trip_distance',
    '10':'pickup_longitude',
    '11':'pickup_latitude',
    '12':'dropoff_longitude',
    '13':'dropoff_latitude'
}

F_FIELDS  = [8,10,11,12,13] # Float fields
S_FIELDS = [5,] # String fields