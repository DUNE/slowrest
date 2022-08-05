# get sensor name as function of sensor id
sensor_name = "SELECT ELEMENT_NAME" \
                  " from NP04_DCS_01.ELEMENTS" \
                  " where ELEMENT_ID=:sensor_id"

# get [id, name] pairs for all sensors
sensor_id_name_pairs = "SELECT ELEMENT_NAME, ELEMENT_ID" \
                       " from NP04_DCS_01.ELEMENTS"

# get [timestamp, value] pairs as function of sensor id, from_ts and to_ts
value_pairs_time_range = "select TS, VALUE_NUMBER" \
                         " from NP04_DCS_01.VEVENTSCREEN" \
                         " where ELEMENT_ID=:sensor_id" \
                         " and TS > :from_ts and TS < :to_ts" \
                         " order by TS asc"

# same as above. returns time stamp instead of datetime obj. takes ~20% longer (on DB side)
value_pairs_time_range2 = "select substr(extract(day from (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')) * 24 * 60 * 60 + extract(hour from (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')) * 60 * 60 + extract(minute from (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')) * 60 + trunc(extract(second from (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')),0),0,15)*1000 as TS, VALUE_NUMBER from (select * from NP04_DCS_01.VEVENTSCREEN order by TS asc) where ELEMENT_ID=:sensor_id and TS >= :from_ts and TS <= :to_ts" 
