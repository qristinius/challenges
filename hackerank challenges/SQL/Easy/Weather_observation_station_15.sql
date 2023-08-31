select format(round(LONG_W,4),'0.0000') from station 
where LAT_N=(select max(LAT_N) from station where LAT_N < 137.2345);