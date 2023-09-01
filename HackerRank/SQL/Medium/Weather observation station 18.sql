select 
    format(round(abs(min(lat_n) - max(lat_n)) + abs(min(long_w)-max(long_w)),4),'0.0000')
from station;