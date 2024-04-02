# File : Test : Solar Tracking
# Author : Tej Pandit
# Date : April 2024
# NOTE : Tested with Android App [ScreenStream by Dmytro Kryvoruchko]

import pysolar.solar as sol
import datetime

latitude = 29.5203
longitude = -98.6017

date = datetime.datetime.now(datetime.timezone.utc)
print(date)
print(sol.get_altitude(latitude, longitude, date), sol.get_azimuth(latitude, longitude, date))