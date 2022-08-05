# get sensor name as function of sensor id
get_sensor_name = "SELECT ELEMENT_NAME" \
                  " from NP04_DCS_01.ELEMENTS" \
                  " where ELEMENT_ID=:sensor_id"

# get [timestamp, value] pairs as function of the day and the sensor id
get_value_pairs_for_day = "SELECT ELEMENT_NAME" \
                  " from NP04_DCS_01.ELEMENTS" \
                  " where ELEMENT_ID=:sensor_id"

# get [id, name] pairs for all sensors
get_sensor_id_name_pairs = "SELECT ELEMENT_NAME, ELEMENT_ID" \
                           " from NP04_DCS_01.ELEMENTS"
