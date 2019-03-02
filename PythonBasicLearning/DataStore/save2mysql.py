import sqlalchemy as db

# MySQL-connector-python
engine = db.create_engine("mysql+mysqlconnector://yunye:804104937@localhost/yunye",pool_recycle=3600)

metadata = db.MetaData()
"""MySQL Data Types
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR
"""

"""create an table
from sqlalchemy import MetaData, Integer, Table, Column, text
from sqlalchemy.dialects.mysql import TIMESTAMP
Table('mytable', metadata,
      Column('gid', Integer, primary_key=True, autoincrement=False),
      Column('id', Integer, nullable=False),
      Column('email_address', String, nullable=False),
      Column('createdata', TIMESTAMP),
      mysql_engine='InnoDB',
      mysql_charset='utf8mb4',
      mysql_key_block_size="1024"
     )
"""
"""INSERT…ON DUPLICATE KEY UPDATE (Upsert)
from sqlalchemy.dialects.mysql import insert

insert_stmt = insert(my_table).values(
    id='some_existing_id',
    data='inserted value')

on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
    data=insert_stmt.inserted.data,
    status='U'
)
on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
    {"data": "some data", "updated_at": func.current_timestamp()},
)
on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
    [
        ("data", "some data"),
        ("updated_at", func.current_timestamp()),
    ],
)

conn.execute(on_duplicate_key_stmt)
"""
#https://docs.sqlalchemy.org/en/latest/core/tutorial.html

bcy_detail_user = db.Table('bcy_detail_user', metadata, autoload=True, autoload_with=engine)
query_user = db.select([bcy_detail_user])

bcy_detail_post = db.Table('bcy_detail_post', metadata, autoload=True, autoload_with=engine)
query_post = db.select([bcy_detail_post])

bcy_img = db.Table('bcy_img', metadata, autoload=True, autoload_with=engine)
query_img = db.select([bcy_img])

proxies_pool = db.Table('proxies_pool', metadata, autoload=True, autoload_with=engine)
query_proxies = db.select([proxies_pool])


with engine.connect() as conn:
	result = conn.execute("show tables;").fetchall()
	result1 = conn.execute(query_user).fetchall()

print(result)
print(result1)

metadata.drop_all()
from sqlalchemy.dialects.mysql import insert
insert()