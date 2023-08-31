select format(round(long_w,4), '0.0000') from station 
where lat_n = (select min(lat_n) from station where lat_n > 38.7780);