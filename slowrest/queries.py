# get sensor name as function of sensor id
sensor_name = '''
SELECT ELEMENT_NAME
FROM NP04_DCS_01.ELEMENTS
WHERE ELEMENT_ID=:sensor_id
'''

# get [id, name] pairs for all sensors
sensor_id_name_pairs = '''
SELECT ELEMENT_ID, ELEMENT_NAME
FROM NP04_DCS_01.ELEMENTS
'''

# get [timestamp, value] pairs as function of sensor id, from_ts and to_ts
value_pairs_time_range = '''
SELECT TS, VALUE_NUMBER
FROM NP04_DCS_01.VEVENTSCREEN
WHERE ELEMENT_ID=:sensor_id
  AND TS > :from_ts and TS < :to_ts
ORDER BY TS asc
'''

# same as above. returns time stamp instead of datetime obj. takes ~20% longer (on DB side)
# Also, timestamp is rounded differently and two hours off (timezone effect)
value_pairs_time_range_old = '''
SELECT 
  SUBSTR(
    EXTRACT(DAY FROM (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')) * 24 * 60 * 60 
    + EXTRACT(HOUR FROM (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')) * 60 * 60 
    + EXTRACT(MINUTE FROM (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')) * 60 
    + TRUNC(EXTRACT(SECOND FROM (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')),0),0,15)*1000 
    AS TS, 
  VALUE_NUMBER 
FROM (
  SELECT * 
  FROM NP04_DCS_01.VEVENTSCREEN 
  WHERE ELEMENT_ID = :sensor_id 
    AND TS >= :from_ts 
    AND TS <= :to_ts
  ORDER BY TS ASC
)
'''

