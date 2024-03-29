# get sensor name as function of sensor id
sensor_name = '''
SELECT ELEMENT_NAME
FROM __PREFIX__.ELEMENTS
WHERE ELEMENT_ID=:sensor_id
'''

# Latest entries for given set of element_ids
sensors_current_value = '''
    WITH RANKEDROWS AS (
        SELECT
            ELEMENT_ID,
            VALUE_NUMBER,
            TS,
            ROW_NUMBER() OVER (
                PARTITION BY ELEMENT_ID
            ORDER BY
                TS DESC
            ) AS row_num
        FROM
            __PREFIX__.VEVENTSCREEN
        WHERE
            ELEMENT_ID IN ({})
        AND TS >= (SYSDATE - 1/2)
    )
    SELECT
        ELEMENT_ID,
        VALUE_NUMBER,
        TS
    FROM
        RANKEDROWS
    WHERE
        row_num = 1
'''

# get [id, name] pairs for all sensors
sensor_id_name_pairs = '''
SELECT ELEMENT_ID, ELEMENT_NAME
FROM __PREFIX__.ELEMENTS
'''

# get [timestamp, value] pairs as function of sensor id, from_ts and to_ts
value_pairs_time_range = '''
SELECT TS, VALUE_NUMBER
FROM __PREFIX__.VEVENTSCREEN
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

test_ts = '''
SELECT TS, VALUE_NUMBER
FROM NP04_DCS_01.VEVENTSCREEN
WHERE ELEMENT_ID=:sensor_id
  AND TS > :from_ts and TS < :to_ts
ORDER BY TS asc
FETCH FIRST 2 ROWS ONLY
'''

test_raw = '''
SELECT 
  SUBSTR(
    EXTRACT(DAY FROM (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')) * 24 * 60 * 60 
    + EXTRACT(HOUR FROM (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')) * 60 * 60 
    + EXTRACT(MINUTE FROM (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')) * 60 
    + EXTRACT(SECOND FROM (TS - TIMESTAMP '1970-01-01 00:00:00' AT TIME ZONE 'UTC')), 0, 15) * 1000 
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
FETCH FIRST 2 ROWS ONLY
'''
