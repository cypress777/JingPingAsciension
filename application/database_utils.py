from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

class DatabaseException(Exception): pass

def init_database(database_name, database):
  try:
    engine = create_engine('sqlite:///{}'.format(database_name),
    connect_args={'check_same_thread': False},
    poolclass=StaticPool, echo=True)

    database.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    database_session = db_session()
    return database_session
  except:
    raise DatabaseException('database init failed')
    return None
      
