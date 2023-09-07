import oracledb
import pprint
import os

sql_sensors = '''
SELECT ELEMENT_ID, ELEMENT_NAME
FROM NP04_DCS_01.ELEMENTS
'''

sql_tables = '''
SELECT owner, table_name
FROM ALL_TABLES
'''

sql_views = '''
SELECT owner, VIEW_NAME
FROM ALL_VIEWS
'''

c = oracledb.connect(
  user=os.environ['FLASK_credentials__user'],
  password=os.environ['FLASK_credentials__password'],
  dsn=os.environ['FLASK_credentials__dsn']
)

db = c.cursor()

# query = db.execute(sql_sensors)
# query = db.execute(sql_tables)
query = db.execute(sql_views)

d = dict(query.fetchall())

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(d)
