select format(round(min(lat_n),4), "0.0000") from station
where lat_n > 38.7780;  