select 
format(round(sqrt(square(min(lat_n)-max(lat_n)) + square(min(long_w) - max(long_w))),4),'0.0000')
from station;