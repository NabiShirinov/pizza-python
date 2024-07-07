from sqlalchemy import create_engine
from sqlalchemy import declarative_base,sessionmaker

engine = create_engine('postgresql://postgres:nabi@localhost/pizza',
    echo = True                   
)

Base = declarative_base()

Session = sessionmaker()