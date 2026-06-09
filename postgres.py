from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine

DB_USER = 'postgres'
DB_PASSWORD = '123'
DB_NAME = 'test'
DB_ECHO = True

engine = create_engine(
f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
,
echo=True,
)
if not database_exists(engine.url):
    create_database(engine.url)